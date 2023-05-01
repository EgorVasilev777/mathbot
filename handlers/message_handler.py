import keyboard
from aiogram.dispatcher.filters import Command

from core import bot, dp, keyboard


@dp.message_handler(Command("start"), state=None)
async def welcome(message):
    # joinedFile = open("user.txt", "r")
    # joinedUsers = set()
    # for line in joinedFile:
    #     joinedUsers.add(line.strip())
    #
    # if not str(message.chat.id) in joinedUsers:
    #     joinedFile = open("user.txt", "a")
    #     joinedFile.write(str(message.chat.id) + "\n")
    #     joinedUsers.add(message.chat.id)
    # if requests_t.check_user(chat_id=str(message.chat.id)) == '':
    #     await bot.send_message(message.chat.id,
    #                            f"Привет, *{message.from_user.first_name},* боюсь, что вы не можете воспользоваться функционалом чат-бота.\n \nОбратитесь в поддержку, чтобы вас добавили.",
    #                            reply_markup=keyboard.remove_keyboard(), parse_mode='Markdown')
    # else:
    await bot.send_message(message.chat.id,
                           f"Привет, *{message.from_user.first_name},* выбери дальнейшеее действие:",
                           reply_markup=keyboard.start(), parse_mode='Markdown')


@dp.message_handler(content_types=['text'])
async def get_message(message):
    if message.text == "📖 Просмотр тем":
        await bot.send_message(message.chat.id, text="Список тем: ",
                               reply_markup=keyboard.get_chapters(),
                               parse_mode='Markdown')
