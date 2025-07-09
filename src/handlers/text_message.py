from telegram import Update
from telegram.ext import ContextTypes

from src.message_texts import NUMBER_OUT_OF_RANGE
from src.services.countdown_timer_message import countdown_timer_message
from src.services.create_list_of_random_words import create_list_of_random_words


async def handle_text_message(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    if (
        update.effective_chat is not None
        and update.effective_message is not None
        and update.message is not None
    ):
        if str(update.message.text).isdigit():
            number_of_words = int(str(update.message.text))

            if number_of_words not in range(1, 101):
                await update.message.reply_text(NUMBER_OUT_OF_RANGE)
                return

            # Delete the user message with the number of words
            await context.bot.delete_message(
                update.effective_chat.id,
                update.effective_message.message_id,
            )

            # Send the list of random words
            list_of_random_words_message = await update.message.reply_text(
                "\n".join(create_list_of_random_words(number_of_words))
            )

            await countdown_timer_message(context, number_of_words + 1, update)

            # Delete the message with the list of random words when the time on
            # the timer is up
            await context.bot.delete_message(
                update.effective_chat.id,
                list_of_random_words_message.message_id,
            )
