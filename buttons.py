from telebot import types as t


class Buttons:
    botoes = t.ReplyKeyboardMarkup(row_width=1)
    botao1 = t.KeyboardButton('Dados recentes')
    botao2 = t.KeyboardButton('Dados por estado')
    botao3 = t.KeyboardButton('Dados por cidade')
    botoes.add(botao1, botao2, botao3)


class Estados:
    estados = t.InlineKeyboardMarkup(row_width=5)
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
    SIGLAS = t.InlineKeyboardButton('SIGLAS', callback_data='SIGLAS')
    estados.row(AC, AL, AP, AM, BA)
    estados.row(CE, DF, ES, GO, MA)
    estados.row(MT, MS, MG, PA, PB)
    estados.row(PR, PE, PI, RJ, RN)
    estados.row(RS, RO, RR, SC, SP)
    estados.row(SE, TO, SIGLAS)


class CidadeRepetida:
    def __init__(self, uf, cidade):
        self.uf = uf
        self.markup = t.InlineKeyboardMarkup()
        self.cont = len(uf)
        self.cid = cidade

    @property
    def reply_markup(self):
        buttons = [
            self.markup.add(
                t.InlineKeyboardButton(f'{self.cid} ({uf})', callback_data=f'{self.cid}*{uf}')) for uf in self.uf
        ]
        return self.markup
