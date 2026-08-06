# Telegram-бот, уведомляющий о проверке работ в Devman

Telegram-бот, уведомляющий о проверке работ в Devman.

## Запуск

Для запуска бота у вас должен быть установлен Python 3.8.9.

- Установите зависимости командой:
  ```
  pip install -r requirements.txt
  ```
- Определите настройки Telegram-бота и доступа к Devman в специальном файле ".env".  
Для этого создайте файл ".env" рядом с "main.py" и запишите туда данные в формате: ПЕРЕМЕННАЯ=значение.  
    Потребуются следущие переменные:  
    - `TG_BOT_TOKEN` — API-токен Telegram-бота.
    - `TG_CHAT_ID` — числовой ID Telegram-пользователя, которому будут приходить уведомления от бота. Чтобы получить свой chat_id, напишите в Telegram специальному боту: [@userinfobot](https://telegram.me/userinfobot).
    - `DEVMAN_API_TOKEN` —  ваш персональный токен для аутентификации в API Девмана. Чтобы получить свой токен, перейдите в документацию [API Девмана](https://dvmn.org/api/docs/).
    
    Пример заполнения файла:
    ```
    TG_BOT_TOKEN=958423683:AAEAtJ5Lde5YYfkjergber
    TG_CHAT_ID=1234567890
    DEVMAN_API_TOKEN=Token 8d1234fc678e4b09865ab3d2f135a905e17f2455
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