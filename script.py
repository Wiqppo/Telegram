from aiogram  import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import  Message, InlineKeyboardButton,InlineKeyboardMarkup
from aiogram import  Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio

BOT_API_TOKEN = '7611787847:AAGwBCY3nPiHMbmheUIVekYhN4Dt9OQfPMA'

bot = Bot(token = BOT_API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage = storage)
router = Router()

@router.message(Command('start'))
async def cmd_start_2(message: Message):
    await message.answer('Запуск сообщения по команде /start Используя фильтр Command()')



@router.message(Command('catalog'))
async def catalog_com(message: Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Каталог товаров", callback_data="catalog")],
        [InlineKeyboardButton(text="партнерство", callback_data="reviews")],
        [InlineKeyboardButton(text="Часто задаваемые вопросы", callback_data="materials")],
        [InlineKeyboardButton(text="Cвязаться с нами", callback_data="contact")]
    ])
    await message.answer('Выбор:', reply_markup=keyboard)

@router.callback_query(lambda c: c.data in ['contact','materials','reviews','catalog'])
async def handle_callback_query(callback_query: types.callback_query):
    data = callback_query.data
    if data == 'contact':
        await callback_query.message.answer('qwerty')
    if data == 'materials':
        await callback_query.message.answer('asdf')
    if data == 'reviews':
        await callback_query.message.answer('zxcv')
    if data == 'catalog':
        await callback_query.message.answer('tgby')

@dp.message_handler(text = ['hello','hi'])
async def hello(message: Message):
    if message.text == "Привет":
        await bot.send_message(message.from_user.id, f"Hello" )

@router.message(text = 'hi')



dp.include_router(router)

async def main():
    await bot.delete_webhook()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
