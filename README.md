# moodle-to-telegram
Moodle to Telegram bot messages via Google Calendar

1. Get your export url from Moodle
https://moodle.org/calendar/export.php
2. Choose All events and Custom datetime e.g. 10/6/2020-11/1/2021
Get url like this one (contains .ics file usually): https://your-moodle.com/calendar/export_execute.php?userid=USER_ID&authtoken=AUTH_TOKEN&preset_what=all&preset_time=custom
3. Go to https://calendar.google.com/calendar/
. Other calendars -> From URL -> Paste your url
We are subscribed to calendar
4. install packages: 
```
pip install -r requirements.txt
```
5. create your bot in botFather 
https://telegram.me/BotFather

6.get your credentials (e.g.token and add them to config.py)
