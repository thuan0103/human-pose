from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, filters, MessageHandler
import sys
sys.path.append('.')
from database import class_information

token: Final = '7160275331:AAGCdfWMeNOhlMPLOY0lrIrLNcRBILM0qLQ'
BOT_USERNAME: Final = '@Chatbotstuden_bot'

chat = {}

async def start(update: Update, context:ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    if user_id not in chat:
        chat[user_id] = {'messager':[]}
    chat[user_id]['messager'].append('/start')
    print(chat)
    await update.message.reply_text("Xin chào đây là chat bot hỗ trợ quản lý lớp học IUH, bạn cần giúp gì")

async def check_class_information(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    if user_id not in chat:
        chat[user_id] = {'messager':[]}
    chat[user_id]['messager'].append('/check_class_information')
    print(chat)
    await update.message.reply_text("Cho tôi thông tin về lớp bạn muốn kiểm tra")

def handle_response(text: str, user_id) -> str:
    with open("key_word/check_class_inf.txt",'r',encoding = 'utf-8') as file_check:
        check_class = [line.strip() for line in file_check]

    processed: str = text.lower()
    if len(chat[user_id]['messager']) >= 6:
        chat[user_id]['messager'].pop(0)

    if '/check_class_information' in chat[user_id]['messager'][len(chat[user_id]['messager'])-1]:
        a = class_information.Class_Information().check_information(teacher=processed)
        if a == False:
            return "không có thông tin về lớp này"
        else:
            return a
    else:
        for check in check_class:
            if check in processed:
                return "Cung cấp thông tin về lớp muốn kiểm tra(Ví dụ: tên lớp, giảng viên hoặc phòng học ) " 

        if 'hello' in processed:
            return "Xin chào"
        elif 'goodbye' in processed:
            return "Tạm biệt"
        else:
            return "Tôi không hiểu tin nhắn"

   
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text
    user_id = update.message.from_user.id
    print(f'User ({update.message.chat.id}) in {message_type}:"{text}"')
    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text, user_id)
            await update.message.reply_text(response)
        else:
            return
    else:
        response: str = handle_response(text, user_id)
        await update.message.reply_text(response)
    print("Bot:", response)
if __name__ == "__main__":
    print("Starting bot...")
    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("check_class_information", check_class_information))  
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling(poll_interval=3)
