from time import sleep

import requests
import telegram
from environs import Env
from requests.exceptions import ConnectionError, ReadTimeout


def send_message_to_TG(token, chat_id, checked_lessons):
    bot = telegram.Bot(token=token)
    for lesson in checked_lessons:
        if lesson["is_negative"]:
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


def main(devman_api_token):
    headers = {'Authorization': devman_api_token}
    params = {}
    retries_limit = 5
    retries = 0
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
                    env.str('TG_BOT_TOKEN'),
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
    main(env.str('DEVMAN_API_TOKEN'))
