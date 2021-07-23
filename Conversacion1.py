#Tarea 1 - Conversacion
import telebot 

bot = telebot.TeleBot('1883937208:AAEcgBcQnAmqmw0Pd8Ezfex0NXO8RuaoJIs')

@bot.message_handler(commands=['hola', 'hi', 'hello']) #definimos el comando
def info(mensaje):
    bot.reply_to(mensaje, "Hola, Como estas")
    print("Hola")

@bot.message_handler(commands=['edad', 'años'])
def info(mensaje):
    bot.reply_to(mensaje, "Tegno 100 años de conciencia")
    print("Edad")

@bot.message_handler(commands=['ubicacion', 'vives', 'ubicación'])
def info(mensaje):
    bot.reply_to(mensaje, "Tengo alojamiento en San pedro sula, en un ordenador")
    print("Ubicacion")

@bot.message_handler(commands=['nombre', 'mote'])
def info(mensaje):
    bot.reply_to(mensaje, "No tengo nombre como tal, pero me llaman Vindel07_Bot")
    print("Nombre")

bot.polling()