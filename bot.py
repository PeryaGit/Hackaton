import telebot
import openai

# Токены для Telegram и OpenAI
TELEGRAM_TOKEN = '6811423118:AAF7laasgizPMEToLjUVM8XVEmewajI3dyg'
OPENAI_API_KEY = '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'

bot = telebot.TeleBot(TELEGRAM_TOKEN)
openai.api_key = OPENAI_API_KEY

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, "Привет! Задай мне вопрос, и я отвечу с помощью ChatGPT.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": message.text}]
        )
        bot.reply_to(message, response.choices[0].message['content'])
    except Exception as e:
        print(f"Ошибка: {e}")  # Это покажет ошибку в консоли
        bot.reply_to(message, "Извините, произошла ошибка при обработке вашего запроса.")

bot.polling() == True