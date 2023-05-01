import ast
import importlib

from aiogram import types

import requests_t
from core import dp, bot

importlib.import_module('handlers.callback_handlers')


@dp.callback_query_handler()
async def handle_query(call: types.CallbackQuery):
    if (call.data.startswith("['key'")):
        keyFromCallBack = ast.literal_eval(call.data)[1]
        #print('utf-8 - ', len(keyFromCallBack.encode('utf-8')))
        await bot.send_message(chat_id=call.message.chat.id,
                               text="Задача: " + requests_t.get_task(keyFromCallBack))
