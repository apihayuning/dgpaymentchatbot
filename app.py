import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, Update, ReplyKeyboardRemove, ForceReply
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext, MessageHandler, Filters
import requests
import json
from flask import Flask
import asyncio

loop = asyncio.get_event_loop()
app = Flask(__name__)

@app.route('/')
def index():
    
    # keyboard
    smartcontract_key = [
        [InlineKeyboardButton("✅ SC DGP ERC 20", callback_data='erc_20'), InlineKeyboardButton("✅ SC DGP BEP 20", callback_data='bep_20')]
    ]

    project_key = [
        [InlineKeyboardButton("➡️ Crypto Trading Bot", url='https://dgpbot.com'),
        InlineKeyboardButton("➡️ NFT Marketplace", url='https://dgpstar.com')],

        [InlineKeyboardButton("➡️ E-Commerce", url='https://dgpmall.com'),
        InlineKeyboardButton("➡️ Virtual Video Meeting", url='https://dgpmeet.com')],

        [InlineKeyboardButton("➡️ Cryptok", url='https://play.google.com/store/apps/details?id=com.dgp.cryptok'),
        InlineKeyboardButton("➡️ DGP Wallet", url='https://dgpwallet.com')]
    ]

    tokenomic_key = [
        [InlineKeyboardButton("➡️ Tokenomic by.Decrypt ", url="https://decrypt.co/resources/tokenomics")]
    ]

    whitepaper_key = [
        [InlineKeyboardButton("➡️ HOME", url="https://dgpaytech.com"),
        InlineKeyboardButton("➡️ ABOUT", url="https://dgpaytech.com/about"),
        InlineKeyboardButton("➡️ BLOG", url="https://dgpaytech.com/blog")],

        [InlineKeyboardButton("➡️ FAQ's", url="https://dgpaytech.com/faq"),
        InlineKeyboardButton("➡️ CONTACT", url="https://dgpaytech.com/contact")]
    ]

    exchange_key = [
        [InlineKeyboardButton("➡️ Digifinex Exchange", url="https://www.digifinex.com/en-ww/trade/USDT/DGP")]
    ]

    partnership_key = [
        [InlineKeyboardButton("➡️ Partnership", url="https://t.me/dgpayclub")]
    ]

    cryptomarket_key = [
        [InlineKeyboardButton("➡️ Coinmarketcap", url="https://coinmarketcap.com/currencies/dgpayment/"),
        InlineKeyboardButton("➡️ Coingecko", url="https://www.coingecko.com/en/coins/dgpayment")]
    ]

    socialmedia_key = [
        [InlineKeyboardButton("➡️ Facebook", url="https://www.facebook.com/DGPayment-100442665153362/"),
        InlineKeyboardButton("➡️ Twitter", url="https://twitter.com/dgpayment")],

        [InlineKeyboardButton("➡️ Telegram", url="https://t.me/DGPayment"),
        InlineKeyboardButton("➡️ Youtube", url="https://www.youtube.com/channel/UCgFkaATk15TJ_0E9KWZ77Aw/videos")]
    ]

    news_key = [
        [InlineKeyboardButton("➡️ News", url="https://www.youtube.com/channel/UCgFkaATk15TJ_0E9KWZ77Aw/videos")]
    ]

    def start(update: Update, context: CallbackContext) -> None:
        """Sends a message with three inline buttons attached."""
        query = update.callback_query

        def openKeyboard():
            rkeyboard = [
                [KeyboardButton('ℹ️ About Us')],
                [KeyboardButton('📝 Smart Contract'), KeyboardButton('📆 Project'), KeyboardButton('📈 Tokenomic')],
                [KeyboardButton('📑 Whitepaper'), KeyboardButton('📊 Exchange'), KeyboardButton('🔗 Partnership')],
                [KeyboardButton('💰 Crypto Market'), KeyboardButton('📢 Social Media'), KeyboardButton('🌐 News')],
                [KeyboardButton('🔀 DGPayment Price')]
            ]

            reply_kmarkup = ReplyKeyboardMarkup(rkeyboard)
            update.message.reply_text(text='🌟 Welcome, thanks for join our community group DGPayment. Let explore what info do you need by click /start 🌟', reply_markup=reply_kmarkup, parse_mode=telegram.ParseMode.MARKDOWN)
        
        if '/start' == update.message.text:
            openKeyboard()

        # reply_markup = InlineKeyboardMarkup(keyboard)
        # update.message.reply_text('Main Menu', reply_markup=reply_markup)

    def button(update: Update, context: CallbackContext) -> None:
        """Parses the CallbackQuery and updates the message text."""

        query = update.callback_query
        query.answer()

        # smartContract
        if 'erc_20' == query.data:
            query.message.reply_text(text="<b>Smartcontract ERC 20</b>\n\n0x927159670C50042109d7C0f4aEd0Cee89452433E", parse_mode=telegram.ParseMode.HTML)
            
        elif 'bep_20' == query.data:
            query.message.reply_text(text="<b>Smartcontract DGP BEP 20</b>\n\n0x8C497b82EE394aE209f455C99B32b78E4A15Dc26", parse_mode=telegram.ParseMode.HTML)
        
        elif 'how_is_work03' == query.data:
            query.message.reply_text(text="<b>Add your NFTs</b>\n\nUpload your work (image, video, audio, or 3D art), add a title and description, and customize your NFTs with properties, stats, and unlockable content.", parse_mode=telegram.ParseMode.HTML)

        elif 'how_is_work04' == query.data:
            query.message.reply_text(text="<b>List them for sale</b>\n\nChoose between auctions, fixed-price listings, and declining-price listings. You choose how you want to sell your NFTs, and we help you sell them!", parse_mode=telegram.ParseMode.HTML)
            
        elif 'dca_set_re_buy' == query.data:
            query.message.reply_text(text="<b>How to Dollar-Cost Averaging (DCA), Set Re-buy</b>\n\nThis means that if you are in a signal and price drops, bot will automatically rebuy the coin to lower your average buy price. Dollar-Cost averaging is a really helpful method to exit the signal as early as possible. However, it should be noted that this might also get you in a position with huge loss. Decide carefully how many times to buyback again.\n\n<b>→ Settings → Re-buy → Click how many times you want to re-buy.</b>", parse_mode=telegram.ParseMode.HTML)

    def mainButton(update: Update, context: CallbackContext) -> None:

        if 'ℹ️ About Us' == update.message.text:
            # update.message.delete(10)
            update.message.reply_text('♻️ <b>About DGPayment</b> ♻️\n\nDGPayment is an innovative global payment processor and platform that allows users to buy and sell products using cryptocurrencies with ease and confidence. It guarantees fast, safe and secure transactions.\n\n➡️<b>Lets Start</b> youtu.be/fAGHFJm_LfE', parse_mode=telegram.ParseMode.HTML)

        elif '📝 Smart Contract' == update.message.text:
            # update.message.delete(10)
            reply_markup = InlineKeyboardMarkup(smartcontract_key)
            update.message.reply_text("♻️ <b>Smart Contract</b> ♻️", parse_mode=telegram.ParseMode.HTML, reply_markup=reply_markup)
        
        elif '📆 Project' == update.message.text:
            # update.message.delete(10)
            reply_markup = InlineKeyboardMarkup(project_key)
            update.message.reply_text('♻️ <b>Dgpayment Projects</b> ♻️', reply_markup=reply_markup, parse_mode=telegram.ParseMode.HTML)

        elif '📈 Tokenomic' == update.message.text:
            # update.message.delete(10)
            # reply_markup = InlineKeyboardMarkup(tokenomic_key)
            update.message.reply_text('♻️ <b>Tokenomic Usecase</b> ♻️\n\n➡️ Activated DGPBOT\n➡️ Activated VIRTUAL MEETING PLATFORM DGP\n➡️ Create Advertising on Cryptok for Business', parse_mode=telegram.ParseMode.HTML)

        elif '📑 Whitepaper' == update.message.text:
            # update.message.delete(10)
            reply_markup = InlineKeyboardMarkup(whitepaper_key)
            update.message.reply_text('♻️ <b>Whitepaper</b> ♻️', parse_mode=telegram.ParseMode.HTML, reply_markup=reply_markup)

        elif '📊 Exchange' == update.message.text:
            # update.message.delete(10)
            reply_markup = InlineKeyboardMarkup(exchange_key)
            update.message.reply_text('♻️ <b>Exchange</b> ♻️', parse_mode=telegram.ParseMode.HTML, reply_markup=reply_markup)

        elif '🔗 Partnership' == update.message.text:
            # update.message.delete(10)
            reply_markup = InlineKeyboardMarkup(partnership_key)
            update.message.reply_text('♻️ <b>Partnership</b> ♻️', parse_mode=telegram.ParseMode.HTML, reply_markup=reply_markup)

        elif '💰 Crypto Market' == update.message.text:
            reply_markup = InlineKeyboardMarkup(cryptomarket_key)
            update.message.reply_text('♻️ <b>Crypto Market Cap</b> ♻️', parse_mode=telegram.ParseMode.HTML, reply_markup=reply_markup)

        elif '📢 Social Media' == update.message.text:
            reply_markup = InlineKeyboardMarkup(socialmedia_key)
            update.message.reply_text('♻️ <b>Social Media</b> ♻️', parse_mode=telegram.ParseMode.HTML, reply_markup=reply_markup)

        elif '🌐 News' == update.message.text:
            reply_markup = InlineKeyboardMarkup(news_key)
            update.message.reply_text('♻️ <b>News</b> ♻️', parse_mode=telegram.ParseMode.HTML, reply_markup=reply_markup)

        elif '🔀 DGPayment Price' == update.message.text:
            # resp = requests.get("https://api.digifinex.com/kline/history?symbol=DGP_USDT&resolution=15&from=1634132700&to=1634133058")
            # resp_ = json.loads(resp.text)
            
            resp = requests.get("https://api.coinmarketcap.com/data-api/v3/tools/price-conversion?amount=1&convert_id=825&id=7864")
            resp_ = json.loads(resp.text)["data"]["quote"][0]["price"]
            update.message.reply_text('♻️ <b>DGPayment Price</b> ♻️\n\n<b>DGP_USDT {}</b>'.format(resp_), parse_mode=telegram.ParseMode.HTML)

    async def main():
        updater = Updater("2068122090:AAEZdUKZuj-8sHAPwU_ypUaotGh-cMf2V5Y", request_kwargs={'read_timeout': 6, 'connect_timeout': 7})
        
        updater.dispatcher.add_handler(CommandHandler('start', start))
        updater.dispatcher.add_handler(CallbackQueryHandler(button))
        updater.dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), mainButton))
        
        updater.start_polling()

    loop.run_until_complete(main())

    return "success.."
