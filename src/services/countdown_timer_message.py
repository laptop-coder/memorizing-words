from time import sleep

from telegram import Update
from telegram.ext import ContextTypes


async def countdown_timer_message(
    context: ContextTypes.DEFAULT_TYPE, seconds: int, update: Update
):
    if update.effective_chat is not None and update.message is not None:
        # Initial value (send message)
        message = await update.message.reply_text(str(seconds))
        # Decrease value (edit message)
        for i in range(seconds - 1, -1, -1):
            sleep(1)
            await context.bot.edit_message_text(
                str(i),
                update.effective_chat.id,
                message.message_id,
            )
        # Time is up (delete message)
        await context.bot.delete_message(
            update.effective_chat.id,
            message.message_id,
        )
