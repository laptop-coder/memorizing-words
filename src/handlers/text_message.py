from telegram import Update
from telegram.ext import ContextTypes

from src.services.send_list_of_random_words_message import (
    send_list_of_random_words_message,
)
from src.services.send_user_answer_check_message import send_user_answer_check_message


async def handle_text_message(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    if update.message is not None:
        if str(update.message.text).isdigit():
            # User inputed number of words
            await send_list_of_random_words_message(context, update)
        elif str(update.message.text).replace("\n", "").isalpha():
            # User inputed list of words
            await send_user_answer_check_message(context, update)
