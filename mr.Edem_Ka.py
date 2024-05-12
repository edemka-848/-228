import discord
from discord.ext import commands
from discord import app_commands
import time
import os


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.event
async def on_message(message):
    if message.author == client.user:
        return
    
    elif message.content.startswith('Hello'):
        await message.channel.send(f'Привет! Я бот mr.Edem_Ka!')
        time.sleep(1)
        await message.channel.send('Меня создали, что бы расказать тебе про глобальное потепление.') 
        time.sleep(1)
        await message.channel.send('А ещё о том, как ты можешь помочь ему предотвращению.')
        time.sleep(1)
        await message.channel.send('Хочу тебя предупредить! Никогда не пиши мне "мусор". Я не люблю мусор!')
        time.sleep(1)
        await message.channel.send('Приступим!')
        time.sleep(1)
        ##########################
        await message.channel.send('Глобальное потепление — долгосрочное повышение средней температуры климатической системы Земли. По мнению подавляющего большинства учёных, основной причиной глобального потепления является человеческая деятельность.')
        time.sleep(3)
        ##########################
        await message.channel.send('Ты можешь помочь предотвращению глобального потепления. Просто вывполняй ниже указанные пункты.')
        time.sleep(3)
        ##########################
        await message.channel.send('1.Уменьшите потребление продуктов животного происхождение. Поскольку приготовление и транспортировка мяса животных и продуктов животного происхождения потребляют много энергии, воды и других ресурсов, ограничив их потребление, можно снизить свой углеродный след.')
        with open('images/1.jpg', 'rb') as f:
            picture = discord.File(f)
        await message.channel.send(file=picture)
        time.sleep(3)
        ##########################
        await message.channel.send('2.Покупайте продукцию местного производства. Ограничив потребление продуктов, которые привозят к вам издалека, вы не только поможете местной экономике, но и уменьшите свой суммарный углеродный след.')
        with open('images/2.jpg', 'rb') as f:
            picture = discord.File(f)
        await message.channel.send(file=picture)
        time.sleep(3)
        ##########################
        await message.channel.send('3.Перерабатывайте и повторно используйте все, что сможете. Поскольку для создания определенных материалов с нуля требуется много энергии, переработка и повторное использование позволяют уменьшить затраты энергии, необходимые для производства новых товаров.')
        with open('images/3.jpg', 'rb') as f:
            picture = discord.File(f)
        await message.channel.send(file=picture)
        ##########################
        await message.channel.send('4.Ограничьте количество автомобильных поездок. Поскольку выхлопные газы автомобилей — один из самых существенных факторов глобального потепления, чем меньше вы будете садиться за руль, тем больше пользы это принесет')
        with open('images/4.jpg', 'rb') as f:
            picture = discord.File(f)
        await message.channel.send(file=picture)
        time.sleep(3)
        ##########################
        await message.channel.send('5.Поддерживайте свой автомобиль в надлежащем состоянии. Если вы не представляете себе жизнь без автомобиля, постарайтесь хотя бы минимизировать его воздействие на окружающую среду.')
        with open('images/5.jpg', 'rb') as f:
            picture = discord.File(f)
        await message.channel.send(file=picture)
        time.sleep(3)
        ##########################
        await message.channel.send('Пожалуйста, соблюдай эти пунткты!Сохраняй природу и не вреди ей!')
        time.sleep(1)
        ##########################
        await message.channel.send('Так же ты можешь пройти небольшой квест по предотвращению глобальногот потепления')
        with open('images/6.jpg', 'rb') as f:
            picture = discord.File(f)
        await message.channel.send(file=picture)
        time.sleep(1)
        await message.channel.send('Чтобы пройти квест введи "/test". Удачи!')

    elif message.content.startswith('мусор'):
        await message.channel.send('Я предупреждал!')
        time.sleep(1)
        await message.channel.send('3!')
        time.sleep(1)
        await message.channel.send('2!')
        time.sleep(1)
        await message.channel.send('1!')
        time.sleep(1)
        while True:
            await message.channel.send('Сохраняй природу!')
            time.sleep(2)

    if message.content.startswith('/test'):
        await message.channel.send('Привет! Представляю вам квиз "Способы предотвращения глобального потепления"!')
    
        
########################### 1 ВОПРОС ###########################

        await message.channel.send("Актуальна ли тема глобального потепления в наще время(да или нет)?")

########################### 2 ВОПРОС ###########################

        await message.channel.send("Поможет ли переход на велосипед для предотвращения глобального потепления(да или нет?)?")

########################### 3 ВОПРОС ###########################

        await message.channel.send("Важно ли перерабатывать и использовать повторно мусор(да или нет?)?")

########################### 4 ВОПРОС ###########################

        await message.channel.send("Выхлопы машин влият на глобальное потепление(да или нет?)?")

########################### 5 ВОПРОС ###########################

        await message.channel.send("Понравился ли вам квиз?(да или нет?)")

        await message.channel.send("Вот все вопросы! А теперь напиши ответ через запятые без пробелов пример (да,нет,да,нет,нет). Если ответ неправильный, то я не отвечу!") 
@client.event


async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith('да,да,да,да,да'):                  
        await message.channel.send("твой результат:")
        await message.channel.send("5")
    elif message.content.startswith != ('да,да,да,да,да'):
        await message.channel.send("твой результат:")
        await message.channel.send("Он меня не удовлетворяет, попробуй ещё раз!")
        

            
bot.run("MTIyMzkxNjUyMDc0NTM0MTAzOA.GDx8PV.acCV-g7Pn8Opdf1w49xMfdgSo1SSta0nZhYmOQ")