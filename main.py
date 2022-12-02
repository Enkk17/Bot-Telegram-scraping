import requests
import emoji
import time
import matplotlib
from telegram import *
from telegram.ext import *
from requests import *
import os
from bs4 import BeautifulSoup
import pandas as pd
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import *




    # classifica piloti
def scraping_piloti():
    while True:
        #sito web
        url = 'insert site'
        #richiesta sito
        page = requests.get(url)
        #soup
        soup = BeautifulSoup(page.text, 'lxml')
        #dataframe
        df = pd.read_html(str(soup), flavor='bs4', header=[0])[0]
        df.drop(["Unnamed: 0", "Unnamed: 6"], axis=1, inplace=True)
        df.index=df.index+1
        df.head()
        df.plot.bar(x="Driver", y="PTS");
        dati_piloti = df[["Driver", "PTS"]]
        return dati_piloti
        time.sleep(3)

    # classifica costruttori
def scraping_costruttori():
    while True:
        #sito
        url2 = 'insert site'
        #richiesta sito
        page2 = requests.get(url2)
        #soup
        soup2 = BeautifulSoup(page2.text, 'lxml')
        #dataframe
        df2 = pd.read_html(str(soup2), flavor='bs4', header=[0])[0]
        dati_team = df2
        dati_team.drop(["Unnamed: 0", "Unnamed: 4"], axis=1, inplace=True)
        df2.index=df2.index+1
        df2.head()
        df2.plot.bar(x="Team", y="PTS");
        dati_team=df2[["Team","PTS"]]
        return dati_team
        time.sleep(3)
def scraping_motogp():
    while True:
        url3='insert site'
        page3=requests.get(url3)
        soup3=BeautifulSoup(page3.text, 'lxml')
        df3=pd.read_html(str(soup3),flavor='bs4', header=[0])[0]
        dati_motogp=df3
        dati_motogp.drop(["Unnamed: 24", "Unnamed: 25"], axis=1, inplace=True)
        df3.index=df3.index+1
        df3.head()
        df3.plot.bar(x="Pilota",y="Punti")
        dati_motogp=df3[["Pilota","Punti"]]
        dati_motogp.columns = ["Rider","PTS"]
        return dati_motogp
        time.sleep(3)



#prossima gare

# print
# print(race)


#PARTE BOT
updater = Updater("insert token bot",
                  use_context=True)
TOKEN = "insert bot telegram"


def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        emoji.emojize("Welcome! Thank you for use this bot! :red_heart: \n Write /help for more information"))

def about(update: Update, context:CallbackContext):
    update.message.reply_text('''Written by a guy who wants to expand his knowledge on programming and as a hobby, the project was born as a non-profit, it was born for the convenience of knowing without downloading apps or visiting websites the most information on the F1 World Championship.''')


def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands :-
    /stats_driver - To get the 2022 Driver Standings 
    /stats_constructor - To get the 2022 Constructor  Standings
    /motogp - To get the 2022 MotoGp Driber Constructor
    /about- To get more information for this project """)


def stats_driver(update: Update, CallbackContext):
    update.message.reply_text(
        f"RIDERS RANKING\n<pre>{scraping_piloti()}</pre>", parse_mode='html')


def stats_constructor(update: Update, CallbackContext):
    update.message.reply_text(
        emoji.emojize(" \u2757 FOR A CORRECT DISPLAY OF THE RANKING, PUT THE SCREEN HORIZONTAL \u2757"))
    update.message.reply_text(
        f"TEAM RANKING\n<pre>{scraping_costruttori()}</pre>",parse_mode='html')

def motogp(update: Update, CallbackContext):
    update.message.reply_text(
        f"RIDERS RANKING\n<pre>{scraping_motogp()}</pre>", parse_mode='html')

    return 1



updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('stats_driver', stats_driver))
updater.dispatcher.add_handler(CommandHandler('motogp', motogp))
updater.dispatcher.add_handler(CommandHandler('stats_constructor', stats_constructor))
updater.dispatcher.add_handler(CommandHandler('about', about))
updater.dispatcher.add_handler(CommandHandler('start',start))


updater.start_polling()



