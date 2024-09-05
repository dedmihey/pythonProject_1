from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb_ = InlineKeyboardMarkup()
button_ = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button_2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb_.add(button_)
kb_.add(button_2)

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Купить')
        ],
        [KeyboardButton(text='Рассчитать'),
         KeyboardButton(text='Информация')
         ]
    ], resize_keyboard=True
)

buy_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Продукт 1', callback_data='product_buying')],
        [InlineKeyboardButton(text='Продукт 2', callback_data='product_buying')],
        [InlineKeyboardButton(text='Продукт 3', callback_data='product_buying')],
        [InlineKeyboardButton(text='Продукт 4', callback_data='product_buying')]
    ]
)


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    for i in range(1, 5):
        await message.answer(f'Название: Product {i} | Описание: описание {i} | Цена: {i * 100}')
        with open(f'files/{i}.jpg', 'rb') as img:
            await message.answer_photo(img)
    await message.answer('Выберите товар для покупки', reply_markup=buy_kb)
@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт')
    await call.answer()

@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию', reply_markup=kb_)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('Ккал = 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')
    await call.answer()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет', reply_markup=start_kb)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст: ')
    await call.answer()
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    # data = await state.get_data()
    await message.answer('Введите свой рост: ')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    # data = await state.get_data()
    await message.answer('Введите свой вес: ')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    calories = 10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) + 5
    await message.answer(f'Ваша норма калорий {calories}')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
