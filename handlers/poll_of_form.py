from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardRemove

from keyboards.simple_row import make_row_keyboard


router = Router()


available_ics_names = ['CPU', 'Chips', 'Cards']
available_ics_counts = ['10 шт', '100 шт', '1000 шт']


class OrderIcs(StatesGroup):
    choosing_ics_names = State()
    choosing_ics_counts = State()


@router.message(Command("ics"))
async def cmd_ics(message: Message, state: FSMContext):
    await message.answer(
        text="Выберите товар",
        reply_markup=make_row_keyboard(available_ics_names)
    )
    await state.set_state(OrderIcs.choosing_ics_names)


@router.message(
    OrderIcs.choosing_ics_names,
    F.text.in_(available_ics_names)
)
async def ics_chosen(message: Message, state: FSMContext):
    await state.update_data(chosen_ics=message.text.lower())
    await message.answer(
        text="Спасибо, теперь выберите количество",
        reply_markup=make_row_keyboard(available_ics_counts)
    )
    await state.set_state(OrderIcs.choosing_ics_counts)


@router.message(OrderIcs.choosing_ics_names)
async def ics_chosen_incorrectly(message: Message):
    await message.answer(
        text="Извините, мы не знаем такого товара.\n\n"
            "Пожалуйста, выберите одно из названий из списка ниже:",
        reply_markup=make_row_keyboard(available_ics_names)
    )


@router.message(OrderIcs.choosing_ics_counts, F.text.in_(available_ics_counts))
async def ics_count_chosen(message: Message, state: FSMContext):
    user_data = await state.get_data()
    await message.answer(
        text=f"Ваш заказ:   \n\n"
        f"Название: {user_data['chosen_ics']} \n"
        f"Количество: {message.text.lower()}",

        reply_markup=ReplyKeyboardRemove()
    )
    print(user_data)
    await state.clear()


@router.message(OrderIcs.choosing_ics_counts)
async def ics_count_incorrectly(message: Message):
    await message.answer(
        text="У нас есть несколько размеров партий.\n\n"
             "Пожалуйста, выберите один из вариантов из списка ниже:",
        reply_markup=make_row_keyboard(available_ics_counts)
    )




