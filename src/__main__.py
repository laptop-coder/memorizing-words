from telegram.ext import ApplicationBuilder, MessageHandler, filters

from src.config import BOT_TOKEN
from src.handlers.text_message import handle_text_message


def main() -> None:
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text_message)
    )
    app.run_polling()


if __name__ == "__main__":
    main()
