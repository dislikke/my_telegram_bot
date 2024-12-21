import telebot
from telebot import types

# Токен вашего бота
TOKEN = '8165685490:AAH4Y6WT2UNzeSO845xqbGq2kTdSILzgguw'
bot = telebot.TeleBot(TOKEN)

chat_id = None
keyboard = None


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global chat_id, keyboard
    chat_id = message.from_user.id
    keyboard = types.InlineKeyboardMarkup()
    buttonsinit(message)

    if message.text == "привет":
        bot.send_message(message.from_user.id, "Ага, привет")

    if message.text == "/start":
        bot.send_message(chat_id, text="Чем могу помочь?", reply_markup=keyboard)

    if message.text == "Фотография":
        bot.send_photo(chat_id, caption="вот ваше фото", photo="https://via.placeholder.com/300")
        bot.send_message(chat_id, text="Чем могу помочь?", reply_markup=keyboard)

    if message.text == "Форматированное сообщение":
        bot.send_message(chat_id, "Вот *форматированное* сообщение с *жирным* и _курсивом_", parse_mode='Markdown')

    if message.text == "Аудио сообщение":
        audio_url = 'https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3'
        bot.send_audio(chat_id, audio_url)

    if message.text == "Голосовое сообщение":
        bot.send_voice(chat_id,
                       voice=open('voice_note.ogg', 'rb'))  # Предполагается, что файл с голосовым сообщением есть

    if message.text == "Видео сообщение":
        video_url = 'https://www.w3schools.com/html/movie.mp4'
        bot.send_video(chat_id, video_url)

    if message.text == "Медиа группа":
        media = [types.InputMediaPhoto('https://via.placeholder.com/300'),
                 types.InputMediaVideo('https://www.w3schools.com/html/movie.mp4')]
        bot.send_media_group(chat_id, media)

    if message.text == "Местоположение":
        bot.send_location(chat_id, latitude=55.7558, longitude=37.6173)  # Пример для Москвы

    if message.text == "Контакт":
        bot.send_contact(chat_id, phone_number="+79160000000", first_name="Иван", last_name="Иванов")

    if message.text == "Опрос":
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Да', 'Нет')
        bot.send_message(chat_id, "Согласны ли вы?", reply_markup=markup)


def buttonsinit(message):
    key_photo = types.InlineKeyboardButton(text='Фото', callback_data='photo')
    key_formatted = types.InlineKeyboardButton(text='Форматированное сообщение', callback_data='formatted')
    key_audio = types.InlineKeyboardButton(text='Аудио сообщение', callback_data='audio')
    key_voice = types.InlineKeyboardButton(text='Голосовое сообщение', callback_data='voice')
    key_video = types.InlineKeyboardButton(text='Видео сообщение', callback_data='video')
    key_media_group = types.InlineKeyboardButton(text='Медиа группа', callback_data='media_group')
    key_location = types.InlineKeyboardButton(text='Местоположение', callback_data='location')
    key_contact = types.InlineKeyboardButton(text='Контакт', callback_data='contact')
    key_poll = types.InlineKeyboardButton(text='Опрос', callback_data='poll')

    keyboard.add(key_photo, key_formatted, key_audio, key_voice)
    keyboard.add(key_video, key_media_group, key_location, key_contact, key_poll)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "photo":
        bot.send_photo(chat_id, caption="вот ваше фото", photo="https://via.placeholder.com/300")

    if call.data == "formatted":
        bot.send_message(chat_id, "Вот *форматированное* сообщение с *жирным* и _курсивом_", parse_mode='Markdown')

    if call.data == "audio":
        audio_url = 'https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3'
        bot.send_audio(chat_id, audio_url)

    if call.data == "voice":
        bot.send_voice(chat_id,
                       voice=open('voice_note.ogg', 'rb'))  # Предполагается, что файл с голосовым сообщением есть

    if call.data == "video":
        video_url = 'https://www.w3schools.com/html/movie.mp4'
        bot.send_video(chat_id, video_url)

    if call.data == "media_group":
        media = [types.InputMediaPhoto('https://via.placeholder.com/300'),
                 types.InputMediaVideo('https://www.w3schools.com/html/movie.mp4')]
        bot.send_media_group(chat_id, media)

    if call.data == "location":
        bot.send_location(chat_id, latitude=55.7558, longitude=37.6173)  # Пример для Москвы

    if call.data == "contact":
        bot.send_contact(chat_id, phone_number="+79160000000", first_name="Иван", last_name="Иванов")

    if call.data == "poll":
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Да', 'Нет')
        bot.send_message(chat_id, "Согласны ли вы?", reply_markup=markup)

    bot.send_message(chat_id, text="Чем еще могу помочь?", reply_markup=keyboard)


bot.polling(none_stop=True, interval=0)


