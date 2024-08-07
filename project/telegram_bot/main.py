import telebot
import logging
from config.config_logging import setup_logging, start_scheduler
from config.config_bot import bot
from service.service_bot_main import init_bot_service
from service.service_demon import init_demons

# Setup logging
setup_logging()
start_scheduler()

init_bot_service()
init_demons()


if __name__ == "__main__":
    try:
        bot.polling(none_stop=True)
    except telebot.apihelper.ApiException as e:
        logging.exception("Telegram API Error: %r", e)
    except Exception as e:
        logging.exception("Error occurred while polling: %r", e)
