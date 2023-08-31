import logging
import os

from telegram import Update, ForceReply, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, ApplicationBuilder, Updater, CommandHandler, ConversationHandler, MessageHandler, filters
from dotenv import load_dotenv
import requests

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

logger = logging.getLogger(__name__)


SERVER_URL = "http://127.0.0.1:8080/ru-gpt/"

START_TEXT = r"""Я могу попытаться сымитировать абитуриентов ФПМИ МФТИ, которые что\-то пишут в чате\.

Чтобы пользоваться ботом просто отправьте сообщение\.

Команды:
/start или /help \- показать это сообщение

😎"""

DETAILS_TEXT = """"""


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data['context'] = ""
    await update.message.reply_text(
        START_TEXT,
        parse_mode='MarkdownV2'
    )

async def details(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        DETAILS_TEXT,
        parse_mode='MarkdownV2'
    )

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.message.text

    context.user_data['context'] += message

    len_ = len(context.user_data['context'])
    if len_ > 200:
        context.user_data['context'] = context.user_data['context'][-200:]

    res = requests.post(SERVER_URL, json={'inputs': context.user_data["context"]})
    res = res.json()

    print(res)

    if res["status"]:
        reply = res["outputs"][0]
        context.user_data['context'] += reply
    else:
        context.user_data['context'] = ""
        reply = "что-то сломалось. попробуйте еще раз)"

    await update.message.reply_text(reply)


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Log the error and send a telegram message to notify the developer."""
    logger.error("Exception while handling an update:", exc_info=context.error)


def main() -> None:
    """Run the bot"""

    load_dotenv()

    app = ApplicationBuilder().token(os.environ["TG_BOT_TOKEN"]).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("details", details))
    app.add_handler(CommandHandler("help", start))

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))


    app.add_error_handler(error_handler)

    # Start the bot
    app.run_polling()

if __name__ == '__main__':
    main()
