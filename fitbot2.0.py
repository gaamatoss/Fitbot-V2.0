#-*-coding:utf-8-*-
import telepot
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
import sys, time
from pprint import pprint


bot = telepot.Bot('645022029:AAHo-4iy2-uOltiq3zTiSi-UM6r4bXw-MaQ')


def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Dicas", callback_data="dicas")],
        [InlineKeyboardButton(text="Treinos", callback_data="treinos")]
    ])

    bot.sendMessage(chat_id, ["Ola monstrao, em que posso te ajudar? "], reply_markup=keyboard)
    

def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor= 'callback_query')
    print("Callback Query: ", query_id, from_id, query_data)

    if query_data == "dicas":
        bot.sendMessage(from_id, "1. SAIA DE CASA E DESFRUTE A NATUREZA\n 2. FAÇA EXERCÍCIOS REGULARMENTE\n 3. ENCONTRE MAIS TEMPO PARA OS AMIGOS E FAMILIARES\n 4. APRENDA A SER GRATO\n 5. PRATIQUE A MEDITAÇÃO E GANHE MAIS QUALIDADE DE VIDA\n 6. PROCURE TER UMA BOA NOITE DE SONO\n 7. FAÇA CARIDADE\n 9. TENHA UM HOBBY\n 10. RIA SEMPRE E RIA MUITO\n 11. ABRACE AS PESSOAS\n 12. TENHA UMA ATITUDE POSITIVA PERANTE A VIDA\n")

    elif query_data == "treinos":
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Membros Superiores", callback_data='m1')],
            [InlineKeyboardButton(text="Membros inferiores", callback_data='m2')],
            [InlineKeyboardButton(text="Abdominais", callback_data='ab')],
        ])
        bot.sendMessage(from_id, ["Escolha qual o tipo de exercicio: "], reply_markup=keyboard)
    elif query_data == 'm1':
       bot.sendMessage(from_id,"Aqui está uma playlist com os melhores exercícios -->''https://www.youtube.com/watch?v=VP56-dVhe54&list=PLf6kfIcLZWMcsQXpxn2Dc4RcMQLbo1xa1")

    elif query_data == 'm2':
       bot.sendMessage(from_id, "Aqui está uma playlist com os melhores exercícios -->''https://www.youtube.com/watch?v=wK3MCwoY3K4")

    elif query_data == 'ab':
       bot.sendMessage(from_id, "Aqui está uma playlist com os melhores exercícios -->''https://www.youtube.com/watch?v=AFuXQ-RQSXM")
        

bot.message_loop({'chat': on_chat_message,'callback_query': on_callback_query})


while 1:
    time.sleep(3)
