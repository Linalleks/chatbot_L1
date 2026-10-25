# Telegram-бот, уведомляющий о проверке работ в Devman

Telegram-бот, уведомляющий о проверке работ в Devman.

## Запуск

Для запуска бота у вас должен быть установлен Python3.9.

- Установите зависимости командой:
  ```
  pip install -r requirements.txt
  ```
- Определите настройки Telegram-бота и доступа к Devman в специальном файле ".env".  
Для этого создайте файл ".env" рядом с "main.py" и запишите туда данные в формате: ПЕРЕМЕННАЯ=значение.  
    Потребуются следущие переменные:  
    - `DEVMAN_API_TOKEN` —  ваш персональный токен для аутентификации в API Девмана. Чтобы получить свой токен, перейдите в документацию [API Девмана](https://dvmn.org/api/docs/).  

    - `TG_BOT_TOKEN` — API-токен Telegram-бота для уведомлений о проверке работ в Devman.
    - `TG_CHAT_ID` — числовой ID Telegram-пользователя (ученика), которому будут приходить уведомления от бота. Пользователь должен сначала нажать «Start» или отправить боту любое сообщение, чтобы чат стал валидным. Иначе бот не сможет написать первым и скрипт не будет корректно работать. Чтобы получить свой chat_id, напишите в Telegram специальному боту: [@userinfobot](https://telegram.me/userinfobot).  

    - `LOG_TG_BOT_TOKEN` — API-токен Telegram-бота для уведомлений с логами о работе оновного бота (`TG_BOT_TOKEN`).
    - `LOG_TG_ADMIN_ID` — числовой ID Telegram-пользователя (админа), которому будут приходить уведомления от бота (`LOG_TG_BOT_TOKEN`). Пользователь должен сначала нажать «Start» или отправить боту любое сообщение, чтобы чат стал валидным. Иначе бот не сможет написать первым и скрипт не будет корректно работать. Чтобы получить свой chat_id, напишите в Telegram специальному боту: [@userinfobot](https://telegram.me/userinfobot).  

    Следущие переменные для определения прокси-сервера (при необходимости):  
    - `PROXY_PROTOCOL` — протокол, по которому работает прокси-сервер (например, http, https, socks4, socks5).
    - `PROXY_IP` — IP-адрес (или hostname) прокси-сервера.
    - `PROXY_PORT` — порт, на котором слушает прокси.
    - `PROXY_USER` — (при необходимости) логин для аутентификации на прокси.
    - `PROXY_PASSWORD` — (при необходимости) пароль для аутентификации на прокси.

    Пример заполнения файла:
    ```
    # API Devman
    DEVMAN_API_TOKEN=Token 8d1234fc678e4b09865ab3d2f135a905e17f2455

    # API TG
    # Main Bot
    TG_BOT_TOKEN=958423683:AAEAtJ5Lde5YYfkjergber
    TG_CHAT_ID=1234567890
    # Logger Bot
    LOG_TG_BOT_TOKEN=895423638:AEAtJ5LdAre5YYerfkjegb
    LOG_TG_ADMIN_ID=3894120567

    # PROXY
    PROXY_PROTOCOL=http
    PROXY_IP=0.0.0.127
    PROXY_PORT=1028
    PROXY_USER=user
    PROXY_PASSWORD=password
    ```
- Запустите бота командой:
  ```
  python main.py
  ```
  Если настройки в файле ".env" введены верно, бот работает.


#### Полезные ссылки о ботах и пользователях в Telegram:
- [Как регистрировать бота](https://way23.ru/регистрация-бота-в-telegram.html)
- [Отец ботов](https://telegram.me/BotFather)
- [Как узнать ID в Telegram](https://skyeng.ru/it-industry/it/kak-uznat-id-v-telegram-prosto-i-bystro/)


#### Документация API Девмана:
- [API Девмана](https://dvmn.org/api/docs/)


## Цели проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).