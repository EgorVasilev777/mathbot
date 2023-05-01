from aiogram import types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup

import requests_t


class Keyboard:
    @staticmethod
    def start() -> ReplyKeyboardMarkup:
        start = types.ReplyKeyboardMarkup(resize_keyboard=True)

        topic = types.KeyboardButton("📖 Просмотр тем")

        start.add(topic)

        return start

    @staticmethod
    def cancel() -> ReplyKeyboardMarkup:
        cancel = types.ReplyKeyboardMarkup(resize_keyboard=True)
        cancel_bt = types.KeyboardButton("Отмена")
        cancel.add(cancel_bt)
        return cancel

    @staticmethod
    def get_chapters():
        stringList = requests_t.get_themes()
        markup = types.InlineKeyboardMarkup()
        for key, value in stringList.items():
            markup.add(types.InlineKeyboardButton(text=value,
                                                  callback_data="['key', '" + key + "']"))
        return markup

    @staticmethod
    def remove_keyboard() -> ReplyKeyboardRemove:
        return ReplyKeyboardRemove()
