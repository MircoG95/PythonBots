import discord
import random

class MyClient(discord.Client):
    #Einloggen
    async def on_ready(self):
        print("Ich habe mich eingeloggt.")

    #Wenn Naricht gepostet wird
    async def on_message(self, message):
        if message.author == client.user:      #Sicherstellung das bot nicht auf sich selbst reagiert
            return


        if message.content.startswith("hello bot"):      #wenn die naricht mit (hallo bot beginnt)
           await  message.channel.send("Hello!") # await = warten bis die naricht gesendet ist bevor es weiter geht
      

        #help
        if message.content == ".help":
            await message.channel.send('''Für Roulette: .roulette BID eingeben, wobei BID = \n black \n red \n number \n Für Ping einfach .Ping eingeben''')



        #Ping/Pong
        if message.content == ".ping":
            await message.channel.send("Pong!")    


        #Roulette
        if message.content.startswith(".roulette"):
            bid = message.content.split(' ')[1]
            bid_param = -3
            if bid.lower() == "black":
                bid_param = -1
            elif bid.lower() == "red":
                bid_param = -2
            else:
                try:
                    bid_param = int(bid)
                except:
                    bid_param = -3
            if bid_param == -3:
                await message.channel.send('Ungültige Eingabe')
                return
            result = random.randint(0,36)
            print(result)
            if bid_param == -1:
                won = result%2 == 0 and not result == 0
            elif bid_param == -2:
                won = result%2 == 1
            else:
                won = result == bid_param
            if won:
                await message.channel.send(f'$$$ Du hast gewonnen!!! Die zahl ist {result} $$$')
            else:
                await message.channel.send(f'Leider verloren :( Die zahl war {result}')

    
        print(f"Naricht von {message.author} enthält {message.content}") 

client = MyClient()
client.run() #<---- Put the Token here


