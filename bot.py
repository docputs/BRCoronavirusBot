import telebot
from configparser import ConfigParser
from telebot import types as t
import dadosapi
import database

config = ConfigParser()
config.read('bot.conf')

TOKEN = config['BRCORONAVIRUSBOT']['TOKEN']

bot = telebot.TeleBot(TOKEN)

botoes = t.ReplyKeyboardMarkup(row_width=1)
botao1 = t.KeyboardButton('Dados recentes')
botao2 = t.KeyboardButton('Dados por estado')
botoes.add(botao1, botao2)

estados = t.InlineKeyboardMarkup()
AC = t.InlineKeyboardButton('AC', callback_data='AC')
AL = t.InlineKeyboardButton('AL', callback_data='AL')
AP = t.InlineKeyboardButton('AP', callback_data='AP')
AM = t.InlineKeyboardButton('AM', callback_data='AM')
BA = t.InlineKeyboardButton('BA', callback_data='BA')
CE = t.InlineKeyboardButton('CE', callback_data='CE')
DF = t.InlineKeyboardButton('DF', callback_data='DF')
ES = t.InlineKeyboardButton('ES', callback_data='ES')
GO = t.InlineKeyboardButton('GO', callback_data='GO')
MA = t.InlineKeyboardButton('MA', callback_data='MA')
MT = t.InlineKeyboardButton('MT', callback_data='MT')
MS = t.InlineKeyboardButton('MS', callback_data='MS')
MG = t.InlineKeyboardButton('MG', callback_data='MG')
PA = t.InlineKeyboardButton('PA', callback_data='PA')
PB = t.InlineKeyboardButton('PB', callback_data='PB')
PR = t.InlineKeyboardButton('PR', callback_data='PR')
PE = t.InlineKeyboardButton('PE', callback_data='PE')
PI = t.InlineKeyboardButton('PI', callback_data='PI')
RJ = t.InlineKeyboardButton('RJ', callback_data='RJ')
RN = t.InlineKeyboardButton('RN', callback_data='RN')
RS = t.InlineKeyboardButton('RS', callback_data='RS')
RO = t.InlineKeyboardButton('RO', callback_data='RO')
RR = t.InlineKeyboardButton('RR', callback_data='RR')
SC = t.InlineKeyboardButton('SC', callback_data='SC')
SP = t.InlineKeyboardButton('SP', callback_data='SP')
SE = t.InlineKeyboardButton('SE', callback_data='SE')
TO = t.InlineKeyboardButton('TO', callback_data='TO')
estados.row(AC, AL, AP, AM, BA)
estados.row(CE, DF, ES, GO, MA)
estados.row(MT, MS, MG, PA, PB)
estados.row(PR, PE, PI, RJ, RN)
estados.row(RS, RO, RR, SC, SP)
estados.row(SE, TO)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(msg):
    bot.send_message(chat_id=msg.chat.id,
                     text='Aperte o botão <b>Dados recentes</b> para obter o balanço mais recente'
                          ' de Coronavírus no Brasil\n\n'
                          'Para receber notificações diárias, clique em /cadastrar',
                     reply_markup=botoes,
                     parse_mode='HTML')


@bot.message_handler(commands=['cadastrar'])
def register(msg):
    chatid = msg.chat.id
    userid = msg.from_user.id
    if database.register(chatid, userid):
        bot.send_message(chat_id=msg.chat.id, text='Usuário cadastrado com sucesso!')
    else:
        bot.send_message(chat_id=msg.chat.id, text='Usuário já está cadastrado.')


@bot.message_handler(func=lambda m: m.text == 'Dados recentes')
def send_brazil_recent_cases(msg):
    titulo = '\U0001F6A8 <b>Dados recentes de Covid-19 no Brasil</b>\n\n'
    cases = dadosapi.brazil_recent_cases()
    texto = titulo + cases
    bot.send_message(chat_id=msg.chat.id, text=texto, reply_markup=botoes, parse_mode='HTML')


@bot.message_handler(func=lambda m: m.text == 'Dados por estado')
def send_state_options(msg):
    bot.send_message(chat_id=msg.chat.id,
                     text='<b>Clique no estado desejado</b>\n\n',
                     parse_mode='HTML',
                     reply_markup=estados)


@bot.callback_query_handler(func=lambda call: True)
def send_state_recent_cases(call):
    texto = dadosapi.state_recent_cases(call.data)
    bot.edit_message_text(chat_id=call.message.chat.id,
                          message_id=call.message.message_id,
                          text=texto,
                          parse_mode='HTML')


bot.polling(timeout=20, none_stop=True)