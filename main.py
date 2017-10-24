#test
import telebot
import config
from datetime import datetime
import threading
import os

a = datetime.now()

try:
    os.mkdir('./logs/', mode=0o777, dir_fd=None)
except OSError:
    pass
try:
    os.mkdir('./logs/'+str(a.year)+'/', mode=0o777, dir_fd=None)
except OSError:
    pass

if a.month == 1:
    month = './logs/'+str(a.year)+'/Январь.txt'
elif a.month == 2:
    month = './logs/'+str(a.year)+'/Февраль.txt'
elif a.month == 3:
    month = './logs/'+str(a.year)+'/Март.txt'
elif a.month == 4:
    month = './logs/'+str(a.year)+'/Апрель.txt'
elif a.month == 5:
    month = './logs/'+str(a.year)+'/Май.txt'
elif a.month == 6:
    month = './logs/'+str(a.year)+'/Июнь.txt'
elif a.month == 7:
    month = './logs/'+str(a.year)+'/Июль.txt'
elif a.month == 8:
    month = './logs/'+str(a.year)+'/Август.txt'
elif a.month == 9:
    month = './logs/'+str(a.year)+'/Сентябрь.txt'
elif a.month == 10:
    month = './logs/'+str(a.year)+'/Октябрь.txt'
elif a.month == 11:
    month = './logs/'+str(a.year)+'/Ноябрь.txt'
elif a.month == 12:
    month = './logs/'+str(a.year)+'/Декабрь.txt'

#month = str(a.month) + '.txt'
date_format = ['\n---- ',str(a.day),'-',str(a.month),'-',str(a.year),' Запуск Скрипта! ----\n\n' ]
bot = telebot.TeleBot(config.token)
TF = open(month, 'a', encoding = 'utf-8')

#TF.write(str(a.day)+'-'+str(a.month)+'-'+str(a.year)+'\n')
TF.writelines(date_format)
TF.close()

bot.send_message(config.karaz159, 'Запущен!')

@bot.message_handler(commands = ['end'])
def end_of_time(message):
    TF = open(month, 'a', encoding = 'utf-8')
    TF.write('Конец дня, надеюсь\n')
    TF.close()
    print('выключаюсь!')
    raise SystemError# по уебански, конечно, но по другому не работает

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    TF = open(month, 'a', encoding = 'utf-8')
    time = datetime.now()
    answer = [str(time.hour),':', str(time.minute),' ',message.text,'\n']
    TF.writelines(answer)
    TF.close()
    bot.send_message(message.chat.id, 'Записано!')

bot.polling(none_stop = True)
