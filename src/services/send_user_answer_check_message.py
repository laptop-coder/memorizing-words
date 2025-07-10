from telegram import Update
from telegram.ext import ContextTypes

from src.message_texts import RIGHT, WRONG


async def send_user_answer_check_message(
    context: ContextTypes.DEFAULT_TYPE, update: Update
):
    if update.message is not None and context.user_data is not None:
        list_of_words = context.user_data.get("list_of_words")
        if list_of_words is not None:
            user_answer = str(update.message.text).split("\n")
            if [item.lower() for item in list_of_words] == [
                item.lower() for item in user_answer
            ]:
                await update.message.reply_text(RIGHT)
                context.user_data.pop("list_of_words")
            else:
                await update.message.reply_text(WRONG)
