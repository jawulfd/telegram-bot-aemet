from dataclasses import dataclass
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

import aemet
import conf_management as ConfMgt
import config_gifs as gifs

import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.WARNING)


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_html(
        rf"Bienvenido {user.mention_html()}!"
    )


async def weather(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    result_text = ''
    if len(context.args) > 1:
        if context.args[1].isdigit():
            ok, result_text = aemet.get_weather(ConfMgt.get_aemet_token(), context.args[0], context.args[1])
        else:
            await update.message.reply_text('Introduce un dia numerico: /weather city day(int)')
            ok = False
    elif len(context.args) == 1:
        ok, result_text = aemet.get_weather(ConfMgt.get_aemet_token(), context.args[0], 0)
    else:
        ok, result_text = aemet.get_weather(ConfMgt.get_aemet_token(), 'MOJADOS', 0)

    if not ok:
        await update.message.reply_text('Error al conectar con AEMET')
    else:
        await update.message.reply_text(result_text)


async def tester(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    typo = ''
    model = ''
    if len(context.args) > 0:
        typo = context.args[0]
        model = context.args[1] if len(context.args) >= 2 else ''

    if typo != '':
        if model == '':
            await update.message.reply_text('No has definido un personaje')
        elif (typo_lower := f'{typo.lower()}_gifs') not in gifs.items():
            await update.message.reply_text('La serie definida no esta disponible')
        elif (model_upper := model.upper()) in gifs.get(typo_lower):
            await update.message.reply_animation(gifs.get(typo_lower)[model_upper])
        else:
            await update.message.reply_text('El personaje definido no se ha encontrado')
    else:
        await update.message.reply_text(text="Testing updater")


@dataclass
class TelegramC:
    message: str = None
    animation: str = None
    token: str = ConfMgt.get_telegram_token()
    logger = logging.getLogger(__name__)

    def run_bot(self):
        application = Application.builder().token(self.token).build()

        # Command handlers
        start_handler = CommandHandler('start', self.start)
        hello_handler = CommandHandler('hello', hello)
        weather_handler = CommandHandler('weather', weather)
        tester_handler = CommandHandler('tester', tester)
        help_handler = CommandHandler('help', self.helper)
        fiesta_handler = CommandHandler('fiesta', self.fiesta_function)

        polls_filter = MessageHandler(filters=filters.POLL, callback=self.poll_function)
        gif_filter = MessageHandler(filters=filters.Document.GIF, callback=self.gif_function)
        mp4_filter = MessageHandler(filters=filters.Document.MP4, callback=self.gif_function)

        # Add the handlers to the bot
        application.add_handler(start_handler)
        application.add_handler(hello_handler)
        application.add_handler(weather_handler)
        application.add_handler(tester_handler)
        application.add_handler(help_handler)
        application.add_handler(fiesta_handler)

        application.add_handler(polls_filter)
        application.add_handler(gif_filter)
        application.add_handler(mp4_filter)

        # log all errors
        application.add_error_handler(self.error_handler)

        # Starting the bot
        application.run_polling(allowed_updates=Update.ALL_TYPES)

    async def error_handler(self, update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Log Errors caused by Updates."""
        self.logger.warning('Update "%s" caused error "%s"', update, context.error)

    async def helper(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Display a help message"""
        self.message = "Use /start, /hello, /tester or /weather to use this bot."

        await update.message.reply_text(self.message)

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        self.message = "Bienvenido al bot de Sailor Seiya!"
        await update.message.reply_text(self.message)

    async def fiesta_function(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        self.animation = "https://tenor.com/9sHL.gif"
        await update.message.reply_animation(self.animation)

    async def poll_function(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        self.message = "Deja ya las encuestitas, pesad@"
        await update.message.reply_text(self.message)

    async def gif_function(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        self.message = "Ya está el Boomer mandando GIFs sin parar"
        await update.message.reply_text(self.message)
