from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from src.config import BOT_TOKEN


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hello")


def main() -> None:
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("hello", hello))
    app.run_polling()


if __name__ == "__main__":
    main()
