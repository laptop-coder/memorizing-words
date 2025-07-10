from telegram import Update
from telegram.ext import ContextTypes


async def handle_show_answer_command(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    if context.user_data is not None and update.effective_chat is not None:
        list_of_words = context.user_data.get("list_of_words")
        if list_of_words is not None:
            await context.bot.send_message(
                update.effective_chat.id, "\n".join(list_of_words)
            )
