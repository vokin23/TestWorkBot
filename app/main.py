import asyncio
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram import Bot, Dispatcher, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup


from app.api import get_weather
from app.keyboards.inline_keyboard_markup import start_buttons, weather_buttons
from app.settings import token

bot = Bot(token=token)

db = Dispatcher()


class Weather(StatesGroup):
    today = State()
    weak = State()


@db.message(CommandStart())
async def start(message: Message):
    await message.answer(f'<b>Доброго времени суток, {message.from_user.full_name}!</b>\n'
                         f'Выберите действие ниже:', reply_markup=start_buttons, parse_mode='HTML')


@db.callback_query(F.data == 'weather')
async def weather(callback_query: Message):
    await callback_query.message.edit_text('Выберите действие ниже:', reply_markup=weather_buttons)


@db.callback_query(F.data == 'today')
async def today(callback_query: Message, state: FSMContext):
    await callback_query.answer('Введите название города, погоду в котором хотите узнать')
    await callback_query.message.answer('Введите название города, погоду в котором хотите узнать')
    await state.set_state(Weather.today)


@db.message(F.data == 'weak')
async def weak(callback_query: Message, state: FSMContext):
    await callback_query.answer('Данный функционал в доработке')
    await callback_query.message.answer('Введите название города, погоду в котором хотите узнать')
    await state.set_state(Weather.weak)


@db.message(StateFilter(Weather.today))
async def get_today_weather(message: Message, state: FSMContext):
    await message.answer(await get_weather(message.text))
    await state.clear()


@db.message(StateFilter(Weather.weak))
async def get_weak_weather(message: Message, state: FSMContext):
    await message.answer(f'Данный функционал в доработке')
    await state.clear()


async def main():
    await db.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
