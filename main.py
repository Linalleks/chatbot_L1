import requests
import telegram
from environs import Env
from requests.exceptions import ConnectionError, ReadTimeout

env = Env()
env.read_env()

TG_BOT_TOKEN = env.str('TG_BOT_TOKEN')
TG_CHAT_ID = env.str('TG_CHAT_ID')
DEVMAN_API_TOKEN = env.str('DEVMAN_API_TOKEN')


def send_message_to_TG(checked_lessons):
    bot = telegram.Bot(token=TG_BOT_TOKEN)
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
            chat_id=TG_CHAT_ID,
            text=text,
            parse_mode=telegram.ParseMode.MARKDOWN_V2
        )


def main():
    headers = {'Authorization': DEVMAN_API_TOKEN}
    params = {}
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
                send_message_to_TG(checked_lessons['new_attempts'])
                params = {}
        except ReadTimeout:
            continue
        except ConnectionError:
            continue


if __name__ == '__main__':
    main()
