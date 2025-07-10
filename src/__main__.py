from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

from src.config import BOT_TOKEN
from src.handlers.text_message import handle_text_message
from src.handlers.show_answer_command import handle_show_answer_command
from src.handlers.start_command import handle_start_command


def main() -> None:
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", handle_start_command))
    app.add_handler(CommandHandler("show_answer", handle_show_answer_command))
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text_message)
    )
    app.run_polling()


if __name__ == "__main__":
    main()
