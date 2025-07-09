from telegram import Update
from telegram.ext import ContextTypes

from src.services.send_list_of_random_words_message import (
    send_list_of_random_words_message,
)


async def handle_text_message(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    if update.message is not None and str(update.message.text).isdigit():
        await send_list_of_random_words_message(context, update)
