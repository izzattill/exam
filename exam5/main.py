from aiogram import Bot, Dispatcher, filters, types ,F
import asyncio
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bot=Bot(token="7173336488:AAEH9JJplkLSosIb7Sxxv1NWd9tkGL4c4RQ")
dp = Dispatcher(bot=bot)

main_button = InlineKeyboardMarkup(inline_keyboard=[
[InlineKeyboardButton(text="Uzbek tili", callback_data="uzbek"), InlineKeyboardButton(text="Русский язык", callback_data="rus")]
])

main_button3=ReplyKeyboardMarkup(keyboard=[
    [types.KeyboardButton(text="Отправить контакт",request_contact=True)]
],resize_keyboard=True)

main_button4=ReplyKeyboardMarkup(keyboard=[
    [types.KeyboardButton(text="Kontaktni jo'natish",request_contact=True)]
],resize_keyboard=True)

buttons = [
    [types.KeyboardButton(text="Kurslar"),types.KeyboardButton(text="Biz haqimizda"),types.KeyboardButton(text="Yordam")],
    [types.KeyboardButton(text="Til"),types.KeyboardButton(text="Korzinka")]
]
main_button1=types.ReplyKeyboardMarkup(keyboard=buttons,resize_keyboard=True)



buttons_ru = [
    [types.KeyboardButton(text="Курсы"),types.KeyboardButton(text="О нас"),types.KeyboardButton(text="Поддержка")],
    [types.KeyboardButton(text="Язык"),types.KeyboardButton(text="Корзинка")]
]
mainru_button1=types.ReplyKeyboardMarkup(keyboard=buttons_ru,resize_keyboard=True)

kurslar_button=InlineKeyboardMarkup(inline_keyboard=[
[InlineKeyboardButton(text="Rus tili", callback_data="rustili"), InlineKeyboardButton(text="Ingiliz tili", callback_data="ingtili"),InlineKeyboardButton(text="Koreys tili",callback_data="koreystili"),
 InlineKeyboardButton(text="Arab tili",callback_data="arabtili"),InlineKeyboardButton(text="Nemis tili",callback_data="nemistili")]
])

kurslarru_button=InlineKeyboardMarkup(inline_keyboard=[
[InlineKeyboardButton(text="Русский", callback_data="rustili1"), InlineKeyboardButton(text="Английский", callback_data="ingtili1"),InlineKeyboardButton(text="Корейский",callback_data="koreystili1"),
 InlineKeyboardButton(text="Арабский",callback_data="arabtili1"),InlineKeyboardButton(text="Немецкий",callback_data="nemistili1")]
])

Korzinka=InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Hammasini olish",callback_data="olish"),InlineKeyboardButton(text="Bekor qilish",callback_data="atmen"),InlineKeyboardButton(text="Chiqish",callback_data="orqagachiqish")]
])

Корзинка=InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Купить все",callback_data="olish1"),InlineKeyboardButton(text="Отменить продукты",callback_data="atmen1"),InlineKeyboardButton(text="Выход",callback_data="orqagachiqish1")]
])

ingtili_button = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Olish", callback_data="ingbuy"), InlineKeyboardButton(text="Bekor qilish", callback_data="ingcancel")]
])

rustili_button = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Olish", callback_data="rusbuy"), InlineKeyboardButton(text="Bekor qilish", callback_data="ruscancel")]
])

koreystili_button = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Olish", callback_data="koreysbuy"), InlineKeyboardButton(text="Bekor qilish", callback_data="koreyscancel")]
])

arabtili_button = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Olish", callback_data="arabbuy"), InlineKeyboardButton(text="Bekor qilish", callback_data="arabcancel")]
])

nemistili_button = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Olish", callback_data="nemisbuy"), InlineKeyboardButton(text="Bekor qilish", callback_data="nemiscancel")]
])

ingtili1_button = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Купить", callback_data="ingbuy1"), InlineKeyboardButton(text="Не Купить", callback_data="ingcancel1")]
])

rustili1_button = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Купить", callback_data="rusbuy1"), InlineKeyboardButton(text="Не Купить", callback_data="ruscancel1")]
])

koreystili1_button = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Купить", callback_data="koreysbuy1"), InlineKeyboardButton(text="Не Купить", callback_data="koreyscancel1")]
])

arabtili1_button = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Купить", callback_data="arabbuy1"), InlineKeyboardButton(text="Не Купить", callback_data="arabcancel1")]
])

nemistili1_button = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Купить", callback_data="nemisbuy1"), InlineKeyboardButton(text="Не Купить", callback_data="nemiscancel1")]
])

basket=[]
basket1=[]


class Registration(StatesGroup):
    first_name=State()
    last_name=State()
    phone_number=State()
class Registration_ru(StatesGroup):
    first_name=State()
    last_name=State()
    phone_number=State()


@dp.message(filters.Command("start"))
async def start(message: types.Message, state: FSMContext):
    await state.set_state(Registration.first_name)
    await message.answer("Til tanlang , Выберите язык",reply_markup=main_button)

@dp.message(Registration.first_name)
async def first_name(message: types.Message, state: FSMContext):
    await state.update_data(first_name=message.text)
    await state.set_state(Registration.last_name)
    await message.answer("Familiyangiz?")


@dp.message(Registration.last_name)
async def first_name(message: types.Message, state: FSMContext):
    await state.update_data(last_name=message.text)
    await state.set_state(Registration.phone_number)
    await message.answer("Nomer kiriting",reply_markup=main_button4)

@dp.message(Registration.phone_number)
async def first_name(message: types.Message, state: FSMContext):
    await state.update_data(phone_number=message.contact.phone_number)
    data = await state.get_data()
    await message.answer(f"Ism: {data['first_name']}\nFamiliya: {data['last_name']}\nTelefon: {data['phone_number']}",reply_markup=main_button1)
    await state.clear()

@dp.message(Registration.phone_number)
async def phone_number_function(message: types.Message, state: FSMContext):
    await state.update_data(phone_number=message.contact.phone_number)
    await message.answer("Xush kelibsiz")
    await state.clear()

@dp.message(Registration_ru.first_name)
async def first_name(message: types.Message, state: FSMContext):
    await state.update_data(first_name=message.text)
    await state.set_state(Registration_ru.last_name)
    await message.answer("Фамилия?")


@dp.message(Registration_ru.last_name)
async def first_name(message: types.Message, state: FSMContext):
    await state.update_data(last_name=message.text)
    await state.set_state(Registration_ru.phone_number)
    await message.answer("Номер телефона",reply_markup=main_button3)

@dp.message(Registration_ru.phone_number)
async def first_name(message: types.Message, state: FSMContext):
    await state.update_data(phone_number=message.contact.phone_number)
    data = await state.get_data()
    await message.answer(f"Имя: {data['first_name']}\nФамилия: {data['last_name']}\nВаш номер: {data['phone_number']}",reply_markup=mainru_button1)
    await state.clear()

@dp.message(Registration_ru.phone_number)
async def phone_number_function(message: types.Message, state: FSMContext):
    await state.update_data(phone_number=message.contact.phone_number)
    await message.answer("Добро пожаловать")
    await state.clear()

@dp.callback_query(F.data=="uzbek")
async def uzbek(call:types.CallbackQuery):
    await call.message.answer("Xush kelibsiz ismingizni kiriting")

@dp.callback_query(F.data=="rus")
async def rus(call:types.CallbackQuery, state: FSMContext):
    await state.set_state(Registration_ru.first_name)
    await call.message.answer("Добро пожаловать введите ваше имя")

@dp.message(F.text=="Kurslar")
async def kurs(message:types.Message):
    await message.answer("Qaysi kursimizni tanlaysiz?",reply_markup=kurslar_button)

@dp.message(F.text=="Biz haqimizda")
async def haqimizda(message:types.Message):
    await message.answer_photo(photo="https://pbs.twimg.com/profile_images/1184522829028417537/2P8Xcul__400x400.jpg",
                               caption="https://www.ulife.uz/educationCenter/38")

@dp.message(F.text=="Yordam")
async def yordam(message:types.Message):
    await message.answer("+998930007543")

@dp.message(F.text=="Курсы")
async def kurs(message:types.Message):
    await message.answer("Какой из наших курсов вы выберете?",reply_markup=kurslarru_button)

@dp.message(F.text=="О нас")
async def haqimizda1(message:types.Message):
    await message.answer_photo(photo="https://pbs.twimg.com/profile_images/1184522829028417537/2P8Xcul__400x400.jpg",
                               caption="https://www.ulife.uz/educationCenter/38")

@dp.message(F.text=="Поддержка")
async def yordam1(message:types.Message):
    await message.answer("+998930007543")

@dp.message(F.text=="Язык")
async def til1(message:types.Message):
    await message.answer("Вы хотите изменить язык?",reply_markup=main_button)

@dp.callback_query(F.data=="rustili")
async def rustili1(call:types.CallbackQuery):
    await call.message.answer_photo("https://play-lh.googleusercontent.com/RsnY6w5tdQvXq5faBa8EfubZWuGXSd-Slgk44Dg4VWXONJNcEh1MNpo178dEiv-7iA=w240-h480-rw",
                              caption="65.000 so'm",reply_markup=rustili_button)

@dp.callback_query(F.data=="rusbuy")
async def rusbuy_function(call:types.CallbackQuery):
    await call.message.answer("Korzinkaga qo'shildi!",reply_markup=kurslar_button)
    basket.append("Rus tili")

@dp.callback_query(F.data=="ruscancel")
async def ruscancel_function(call:types.CallbackQuery):
    await call.message.answer("❌")
    await call.message.answer("Yana qaysi kurslarimiz sizga ma'qul?", reply_markup=kurslar_button)

@dp.callback_query(F.data=="ingtili")
async def ingtili(call:types.CallbackQuery):
    await call.message.answer_photo("https://lh5.googleusercontent.com/proxy/oZ5O1ydDQwn812xUhOty7q2yUy0n1t-vowz-4AUi-a8eCptHL5gdmjORpVP_WFaUwAOR8cKiq_9KB-CC_-GyglT9Sb1iXLFxNHkNwA1b6qRJv2NSsvvPPPtb8GJ9NY0w-OIdfz_C",
                              caption="80.000 so'm",reply_markup=ingtili_button)

@dp.callback_query(F.data=="ingbuy")
async def ingbuy_function(call:types.CallbackQuery):
    await call.message.answer("Korzinkaga qo'shildi!",reply_markup=kurslar_button)
    basket.append("Ingiliz tili")

@dp.callback_query(F.data=="ingcancel")
async def ingcancel_function(call:types.CallbackQuery):
    await call.message.answer("❌")
    await call.message.answer("Yana qaysi kurslarimiz sizga ma'qul?", reply_markup=kurslar_button)

@dp.callback_query(F.data=="koreystili")
async def koreystili(call:types.CallbackQuery):
    await call.message.answer_photo("https://kitobxon.com/img_knigi/5115.jpg",
                              caption="50.000 so'm",reply_markup=koreystili_button)

@dp.callback_query(F.data=="koreysbuy")
async def koreysbuy_function(call:types.CallbackQuery):
    await call.message.answer("Korzinkaga qo'shildi!",reply_markup=kurslar_button)
    basket.append("Koreys tili")

@dp.callback_query(F.data=="koreyscancel")
async def koreyscancel_function(call:types.CallbackQuery):
    await call.message.answer("❌")
    await call.message.answer("Yana qaysi kurslarimiz sizga ma'qul?", reply_markup=kurslar_button)

@dp.callback_query(F.data=="arabtili")
async def arabtili(call:types.CallbackQuery):
    await call.message.answer_photo("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTuBRlaYktp2LLsJAV1QdXRNyQujrNwc9tZFw&s",
                              caption="50.000 so'm",reply_markup=arabtili_button)

@dp.callback_query(F.data=="arabbuy")
async def arabbuy_function(call:types.CallbackQuery):
    await call.message.answer("Korzinkaga qo'shildi!",reply_markup=kurslar_button)
    basket.append("Arab tili")

@dp.callback_query(F.data=="arabcancel")
async def arabcancel_function(call:types.CallbackQuery):
    await call.message.answer("❌")
    await call.message.answer("Yana qaysi kurslarimiz sizga ma'qul?", reply_markup=kurslar_button)

@dp.callback_query(F.data=="nemistili")
async def nemistili(call:types.CallbackQuery):
    await call.message.answer_photo("https://avatars.mds.yandex.net/get-games/2977039/2a0000017e06256148692ad46ed29ee882f1/orig",
                              caption="150.000 so'm",reply_markup=nemistili_button)

@dp.callback_query(F.data=="nemisbuy")
async def arabbuy_function(call:types.CallbackQuery):
    await call.message.answer("Korzinkaga qo'shildi!",reply_markup=kurslar_button)
    basket.append("Nemis tili")

@dp.callback_query(F.data=="nemiscancel")
async def arabcancel_function(call:types.CallbackQuery):
    await call.message.answer("❌")
    await call.message.answer("Yana qaysi kurslarimiz sizga ma'qul?", reply_markup=kurslar_button)

@dp.callback_query(F.data=="rustili1")
async def rustili1(call:types.CallbackQuery):
    await call.message.answer_photo("https://play-lh.googleusercontent.com/RsnY6w5tdQvXq5faBa8EfubZWuGXSd-Slgk44Dg4VWXONJNcEh1MNpo178dEiv-7iA=w240-h480-rw",
                              caption="65.000 сум",reply_markup=rustili1_button)

@dp.callback_query(F.data=="rusbuy1")
async def rusbuy_function(call:types.CallbackQuery):
    await call.message.answer("Добавлено в корзину!",reply_markup=kurslarru_button)
    basket.append("Русский")

@dp.callback_query(F.data=="ruscancel1")
async def ruscancel_function(call:types.CallbackQuery):
    await call.message.answer("❌")
    await call.message.answer("Yana qaysi kurslarimiz sizga ma'qul?", reply_markup=kurslarru_button)

@dp.callback_query(F.data=="ingtili1")
async def ingtili1(call:types.CallbackQuery):
    await call.message.answer_photo("https://lh5.googleusercontent.com/proxy/oZ5O1ydDQwn812xUhOty7q2yUy0n1t-vowz-4AUi-a8eCptHL5gdmjORpVP_WFaUwAOR8cKiq_9KB-CC_-GyglT9Sb1iXLFxNHkNwA1b6qRJv2NSsvvPPPtb8GJ9NY0w-OIdfz_C",
                              caption="80.000 сум",reply_markup=ingtili1_button)

@dp.callback_query(F.data=="ingbuy1")
async def ingbuy1_function(call:types.CallbackQuery):
    await call.message.answer("Добавлено в корзину!",reply_markup=kurslarru_button)
    basket.append("Английский")

@dp.callback_query(F.data=="ingcancel1")
async def ingcancel1_function(call:types.CallbackQuery):
    await call.message.answer("❌")
    await call.message.answer("Какой из наших других курсов вам нравится??", reply_markup=kurslarru_button)

@dp.callback_query(F.data=="koreystili1")
async def koreystili1(call:types.CallbackQuery):
    await call.message.answer_photo("https://kitobxon.com/img_knigi/5115.jpg",
                              caption="50.000 сум",reply_markup=koreystili1_button)

@dp.callback_query(F.data=="koreysbuy1")
async def koreysbuy1_function(call:types.CallbackQuery):
    await call.message.answer("Добавлено в корзину!",reply_markup=kurslarru_button)
    basket.append("Корейский")

@dp.callback_query(F.data=="koreyscancel1")
async def koreyscancel1_function(call:types.CallbackQuery):
    await call.message.answer("❌")
    await call.message.answer("Какой из наших других курсов вам нравится??", reply_markup=kurslarru_button)

@dp.callback_query(F.data=="arabtili1")
async def arabtili1(call:types.CallbackQuery):
    await call.message.answer_photo("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTuBRlaYktp2LLsJAV1QdXRNyQujrNwc9tZFw&s",
                              caption="50.000 so'm",reply_markup=arabtili1_button)

@dp.callback_query(F.data=="arabbuy1")
async def arabbuy1_function(call:types.CallbackQuery):
    await call.message.answer("Добавлено в корзину!",reply_markup=kurslarru_button)
    basket.append("Арабский")

@dp.callback_query(F.data=="arabcancel1")
async def arabcancel1_function(call:types.CallbackQuery):
    await call.message.answer("❌")
    await call.message.answer("Какой из наших других курсов вам нравится??", reply_markup=kurslarru_button)

@dp.callback_query(F.data=="nemistili1")
async def nemistili1(call:types.CallbackQuery):
    await call.message.answer_photo("https://avatars.mds.yandex.net/get-games/2977039/2a0000017e06256148692ad46ed29ee882f1/orig",
                              caption="150.000 сум",reply_markup=nemistili1_button)

@dp.callback_query(F.data=="nemisbuy1")
async def nemisbuy1_function(call:types.CallbackQuery):
    await call.message.answer("Добавлено в корзину!",reply_markup=kurslarru_button)
    basket.append("Немецкий")

@dp.callback_query(F.data=="nemiscancel1")
async def nemiscancel1_function(call:types.CallbackQuery):
    await call.message.answer("❌")
    await call.message.answer("Какой из наших других курсов вам нравится??", reply_markup=kurslarru_button)

@dp.message(F.text=="Korzinka")
async def korzinka_function(message:types.Message):
    await message.answer(f"{basket}",reply_markup=Korzinka)

@dp.callback_query(F.data=="orqagachiqish")
async def orqagachiqish_function(call:types.CallbackQuery):
    await call.message.answer("Какой из наших других курсов вам нравится??",reply_markup=kurslar_button)

@dp.callback_query(F.data=="olish")
async def olish_function(call:types.CallbackQuery):
    await call.message.answer("Karta raqamingizni kiriting")

@dp.message(F.text)
async def wiki1(message: types.Message):
    wiki1(message.text)
    await message.answer("Qabul qilindi✅",reply_markup=main_button)

@dp.callback_query(F.data=="atmen")
async def atmen_function(call:types.CallbackQuery):
    await call.message.answer("Botdan foydalanganingiz uchun rahmat😊",reply_markup=main_button)

@dp.message(F.text=="Корзинка")
async def korzinka1_function(message:types.Message):
    await message.answer(f"{basket}",reply_markup=Корзинка)

@dp.callback_query(F.data=="orqagachiqish1")
async def orqagachiqish1_function(call:types.CallbackQuery):
    await call.message.answer("Вам нужен еще один из наших курсов??",reply_markup=kurslarru_button)

@dp.callback_query(F.data=="olish1")
async def olish1_function(call:types.CallbackQuery):
    await call.message.answer("Введите номер вашей карты")

@dp.message(F.text)
async def wiki1(message: types.Message):
    wiki1(message.text)
    await message.answer("Получено✅",reply_markup=main_button)

@dp.callback_query(F.data=="atmen1")
async def atmen_function(call:types.CallbackQuery):
    await call.message.answer("Спасибо за использование бота😊",reply_markup=main_button)

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())