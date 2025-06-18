
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram import Router, F,html
from aiogram.fsm.context import FSMContext
from states.register import RegisterState
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError


from keyboards.inline.button import courses_ibtn
from keyboards.reply.button import confirm_button, share_contact, menu
from utils.db.database import User, session
from aiogram.utils.i18n import gettext as _
from aiogram.utils.i18n import get_i18n as __





register_router=Router()

@register_router.message(F.text =="/register")
async def command_register(message:Message,state: FSMContext):
    await message.answer(_("Toliq ismingizni kiriting"))
    await state.set_state(RegisterState.fullname)

@register_router.message(RegisterState.fullname)
async def register_fullname(message:Message,state:FSMContext):
    fullname = message.text
    await state.update_data(fullname=fullname)
    await message.answer(_("Telefon raqamingizni kiriting yoki knopkani bosing"),reply_markup=share_contact())
    await state.set_state(RegisterState.phone)



@register_router.message(RegisterState.phone)
async def register_phone(message: Message, state: FSMContext):
    phone = message.contact.phone_number if message.contact else message.text
    await state.update_data(phone=phone)
    data = await state.get_data()
    fullname = data.get('fullname', 'N/A')
    await message.answer(
        _("Ismingiz: {fullname}\nTelefon raqamingiz: {phone}\n\nMa'lumotlaringizni tasdiqlaysizmi?").format(fullname=html.bold(fullname),phone=html.bold(phone)),
        reply_markup=confirm_button()
    )
    await state.set_state(RegisterState.confirm)

# @register_router.message(RegisterState.phone)
# async def register_phone(message:Message,state:FSMContext):
#     phone = message.contact.phone_number
#     if message.contact:
#         phone = message.contact.phone
#     await state.update_data(phone=phone)
#     datas = await state.get_data()
#     id = message.from_user.id
#     chat_id = message.from_user.id
#     fullname = datas.get('fullname','N/A')
#     phone = datas.get('phone' , 'N/A')
#     confirm = datas.get('confirm' , 'N/A')
#     await message.answer("malumotlaringizni tasdiqlaysizmi ",reply_markup=confirm_button())
#     await state.set_state(RegisterState.confirm)


@register_router.message(RegisterState.confirm)
async def register_confirm(message: Message, state: FSMContext):
    confirm = message.text
    if confirm.casefold() ==_( 'ha'):
        datas = await state.get_data()
        chat_id = message.from_user.id
        fullname = datas.get('fullname', 'N/A')
        phone = datas.get('phone', 'N/A')

        existing_user = session.execute(select(User).where(User.chat_id == chat_id)).scalar_one_or_none()
        if existing_user:
            await message.answer(_("Siz allaqachon ro'yxatdan o'tgansiz."))
            await state.clear()
            return

        new_user = User(chat_id=chat_id, fullname=fullname, phone=phone)
        try:
            session.add(new_user)
            session.commit()
        except SQLAlchemyError as e:
            await message.answer(_("Xatolik yuz berdi: "))
            session.rollback()
            return

        await message.answer(_("Ro'yxatdan o'tdingiz ✅"), reply_markup=ReplyKeyboardRemove())
        await message.answer(_("Botdan foydalanishingiz mumkin"), reply_markup=menu())
        await state.clear()

    elif confirm.casefold() == _('yoq'):
        await message.answer(_("Sog‘ salomat bo‘ling. Qaytadan ro‘yxatdan o‘tish uchun /register buyrug‘ini bosing!"))
        await state.clear()

    else:
        await message.reply(_("Iltimos, 'ha' yoki 'yo‘q' deb tasdiqlang."))




# @register_router.message(RegisterState.confirm)
# async def register_confirm(message:Message,state:FSMContext):
#     confirm = message.text
#     if confirm.casefold()=='ha':
#         datas = await state.get_data()
#         id = datas.get('id','N/A')
#         chat_id = message.from_user.id
#         fullname = datas.get('fullname','N/A')
#         phone = datas.get('phone','N/A')
#         confirm = datas.get('confirm','N/A')
#         new_user = User(chat_id=chat_id, fullname=fullname, phone=phone)
#         try:
#             session.add(new_user)
#             session.commit()
#         except Exception as e:
#             await message.answer(f"Xatolik yuz berdi: {e}")
#             session.rollback()
#             return
#         await message.answer("marhamt",reply_markup=ReplyKeyboardRemove())
#         await message.answer ('botdan foydalanishingiz mumkin',reply_markup=courses_ibtn())
#         await state.clear()
#         return
#
#     elif confirm.casefold()=='yoq':
#         await message.answer('sog salomat boling , qaytadan royxatdan otish uchun /register tugmasini bosing !')
#         await state.clear()
#
#     else:
#         await message.reply('ha yoki yoq bilan tasdinglang')

