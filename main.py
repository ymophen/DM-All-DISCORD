#Mass Dm By Szordrin9999
import discord

client = discord.Client()

@client.event
async def on_connect():
  for user in client.user.friends:
    try:
      await user.send("Example")#ADD HERE THAT YOU WANNA SEND TO YOUR FRIENDS
      print(f"messaged: {user.name}")
    except:
       print(f"couldnt message: {user.name}")

client.run('ur discord token', bot=False)#ADD YOUR TOKEN HERE NOT ANY BOT TOKEN
