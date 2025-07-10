from telegram import Update
from telegram.ext import ContextTypes

from src.message_texts import START


async def handle_start_command(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    if update.effective_chat is not None:
        await context.bot.send_message(update.effective_chat.id, START)
