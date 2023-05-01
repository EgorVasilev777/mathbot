import importlib
from aiogram.utils import executor
from core import dp

importlib.import_module('handlers.message_handler')
importlib.import_module('handlers.callback_handlers')

if __name__ == '__main__':
    print('Боевой шмель!')
executor.start_polling(dp)
