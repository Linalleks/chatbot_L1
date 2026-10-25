import logging
from time import sleep
from urllib.parse import quote

import requests
import telegram
from environs import Env
from telegram.error import TelegramError
from requests.exceptions import ConnectionError, ReadTimeout
from telegram.utils.request import Request

logger = logging.getLogger('tg_bot')


class TGLogsHandler(logging.Handler):

    def __init__(self, tg_bot, chat_id):
        super().__init__()
        self.chat_id = chat_id
        self.tg_bot = tg_bot

    def emit(self, record):
        try:
            log_entry = self.format(record)
            self.tg_bot.send_message(
                chat_id=self.chat_id,
                text=log_entry,
                parse_mode=telegram.ParseMode.MARKDOWN_V2
            )
        except TelegramError:
            self.handleError(record)
        except Exception:
            self.handleError(record)


def build_proxy_url(protocol, ip, port, user=None, password=None):
    if not (protocol and ip and port):
        return None
    if user and password:
        auth = f'{quote(user, safe="")}:{quote(password, safe="")}@'
    else:
        auth = ''
    return f'{protocol}://{auth}{ip}:{port}'


def send_message_to_TG(bot, chat_id, checked_lessons):
    try:
        for lesson in checked_lessons:
            if lesson['is_negative']:
                text = (
                    f'У Вас проверили работу [{lesson["lesson_title"]}]({lesson["lesson_url"]})\n\n'
                    'К сожалению, в работе нашлись ошибки\.'
                )
            else:
                text = (
                    f'У Вас проверили работу [{lesson["lesson_title"]}]({lesson["lesson_url"]})\n\n'
                    'Преподавателю все понравилось, можно приступать к следующему уроку\!'
                )
            bot.send_message(
                chat_id=chat_id,
                text=text,
                parse_mode=telegram.ParseMode.MARKDOWN_V2
            )
            logger.info('Бот направил сообщение о проверке работы')
    except Exception as e:
        logger.exception(
            'Бот упал с ошибкой:\n%s',
            e,
            exc_info=True,
        )


def main():
    headers = {'Authorization': env.str('DEVMAN_API_TOKEN')}
    params = {}
    retries_limit = 5
    retries = 0
    proxy_url = build_proxy_url(
        env.str('PROXY_PROTOCOL', default=None),
        env.str('PROXY_IP', default=None),
        env.int('PROXY_PORT', default=None),
        env.str('PROXY_USER', default=None),
        env.str('PROXY_PASSWORD', default=None),
    )
    request = Request(proxy_url=proxy_url)

    bot = telegram.Bot(token=env.str('TG_BOT_TOKEN'), request=request)
    logger_bot = telegram.Bot(token=env.str('LOG_TG_BOT_TOKEN'), request=request)

    logger.setLevel(logging.INFO)
    logger.addHandler(TGLogsHandler(logger_bot, env.int('LOG_TG_ADMIN_ID')))
    logger.info(f'Бот [{bot.first_name}]({bot.link}) запущен')

    while True:
        try:
            response = requests.get(
                'https://dvmn.org/api/long_polling/',
                headers=headers,
                params=params
            )
            response.raise_for_status()

            checked_lessons = response.json()

            if checked_lessons['status'] == 'timeout':
                params = {'timestamp': checked_lessons['timestamp_to_request']}
            else:
                send_message_to_TG(
                    bot,
                    env.str('TG_CHAT_ID'),
                    checked_lessons['new_attempts']
                )
                params = {}
            retries = 0
        except ReadTimeout:
            continue
        except ConnectionError:
            retries += 1
            if retries < retries_limit:
                connection_delay = retries
            else:
                connection_delay = 7200
            sleep(connection_delay)
            continue


if __name__ == '__main__':
    env = Env()
    env.read_env()
    main()
