import requests
import os 
import sys
import json
from requests.auth import HTTPDigestAuth
#import bs4 as BS
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys, ActionChains
from prettytable import PrettyTable
from tkinter import *
import telebot
from telebot import types
'''
root = Tk()     # создаем корневой объект - окно
root.title("ASIC#INFO")     # устанавливаем заголовок окна
root.geometry("300x250")    # устанавливаем размеры окна
'''

url_inf = 'http://192.168.1.23/cgi-bin/minerStatus.cgi'
url_config = 'http://192.168.1.23/cgi-bin/minerConfiguration.cgi'
bot = telebot.TeleBot('5294703958:AAG1-Ggk4-C2qaa99PiPiN0fraj5rlK7QlE');


# s = str ([i.text for i in inf.temperature()] )  

#bot.infinity_polling()       



@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Привет')

@bot.message_handler(commands=['b'])
def button_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("TEMP")
    btn2 = types.KeyboardButton("Gh/s")
    btn3 = types.KeyboardButton("Mode")
    btn4 = types.KeyboardButton("All")
    markup.add(btn1,btn2,btn3,btn4)
    bot.send_message(message.chat.id,'___',reply_markup=markup)
    
    
@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text=="TEMP":
        inf = Info(url_inf)
        #inf.out_table()
        #s = str ([i.text for i in inf.temperature()])
        s = '   '.join([i.text for i in inf.temperature()])
        bot.send_message(message.chat.id,s)
    elif message.text=="Gh/s":
        inf = Info(url_inf)
        #inf.out_table()
        #s = str ([i.text for i in inf.temperature()])
        s = '\n'.join([i.text for i in inf.rate()])
        bot.send_message(message.chat.id,s)
    elif message.text=="Mode":
        inf = Info(url_config)
        #inf.out_table()
        #s = str ([i.text for i in inf.temperature()])
        s = '   '.join([i for i in inf.mode()])
        bot.send_message(message.chat.id,s)
    elif message.text=="All":
        inf = Info(url_inf)
        #inf.out_table()
        #s = str ([i.text for i in inf.temperature()])
        s = '\n'.join([i.text for i in inf.rate()])
        bot.send_message(message.chat.id,s)
        
        s = '   '.join([i.text for i in inf.temperature()])
        bot.send_message(message.chat.id,s)
        
                
        inf = Info(url_config)
        #inf.out_table()
        #s = str ([i.text for i in inf.temperature()])
        s = '   '.join([i for i in inf.mode()])
        bot.send_message(message.chat.id,s)


class Info():
    def __init__(self,url):
        self.url = url
        self.r = requests.get(self.url, auth=HTTPDigestAuth('root', 'root'))
        self.soup = BeautifulSoup (self.r.text, 'lxml')
    def pars(self):
        r = requests.get(self.url, auth=HTTPDigestAuth('root', 'root'))
        soup = BeautifulSoup (r.text, 'lxml')
    def temperature(self):
        list_tag_temp = self.soup.find_all(id="cbi-table-1-temp2")
        return list_tag_temp
         #for i in list_tag_temp:
         #   print(i.text)
    def chain(self):
        list_tag_chain = self.soup.find_all(id="cbi-table-1-chain")
        return list_tag_chain 
        #for i in list_tag_chain:
        #      print(i.text)
    def asic(self):
        list_tag_asic = self.soup.find_all(id="cbi-table-1-asic")
        return list_tag_asic
    def frequency(self):
        list_tag_frequency = self.soup.find_all(id="cbi-table-1-frequency")
        return list_tag_frequency
    def rate(self):
        list_tag_rate = self.soup.find_all(id="cbi-table-1-rate")
        return list_tag_rate
    #def hw(self):
      #  list_tag_hw = soup.find_all(id="cbi-table-1-hw")
      #  return list_tag_hw
    def out_table(self):
        
        print('Chain#', 'ASIC#' , 'Frequ', 'GH/S' , '       Temp', sep='\t')
        for i in range(len(self.chain())):
            print(self.chain()[i].text, self.asic()[i].text ,self.frequency()[i].text,self.rate()[i].text,self.temperature()[i].text, sep = '\t')
    def mode(self):
        #url = 'http://192.168.1.23/cgi-bin/minerConfiguration.cgi'
        #r = requests.get(url, auth=HTTPDigestAuth('root', 'root'))
        #soup = BeautifulSoup (r.text, 'lxml')
        t = self.soup.find_all('script')
        y = str(t[3])
        mode = ''
        print(y.find('bitmain-fan-pwm'))
        print('PMW mode', y[503:505])
        print('Mode power', y[608:611])
        if y[608:611] == '244':
            mode = '- 2 Th/s'
        elif y[608:611] == '245':
            mode = '- 2.5 Th/s'
        elif y[608:611] == '246':
            mode = '- 3 Th/s'
        elif y[608:611] == '240':
            mode = 'LowPower'
        elif y[608:611] == '243':
            mode = '- 1.5 Th/s'
        elif y[608:611] == '242':
            mode = '- 1 Th/s'
            
        t = ['PMW',y[503:505],'Power mode',mode]
        return t

inf = Info(url_inf)
inf.out_table()
s = str ([i.text for i in inf.temperature()])

bot.polling(none_stop=True, interval=0)


'''
s = [i.text+'\n' for i in inf.temperature() ]   
label = Label(text=s) # создаем текстовую метку
text = Text(width=25, height=5, bg="darkgreen", fg='white', wrap=WORD)
text.insert(1.0,s)
text.pack()
label.pack()    # размещаем метку в окне
print('d')
root.mainloop()   
'''
            
    
