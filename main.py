#Mass Dm By Szordrin#6870
import discord

client = discord.Client()

@client.event
async def on_connect():
  for user in client.user.friends:
    try:
      await user.send("Best https://github.com/Skiddedz/AstarothSpammerXLS")#ADD HERE THAT YOU WANNA SEND TO YOUR FRIENDS
      print(f"messaged: {user.name}")
    except:
       print(f"couldnt message: {user.name}")

client.run('Nzg1MTI5MTA1MTA3NTgyOTg2.YYbXHA.waKlLHuHNDdiLMIm96TXGzRWgyA', bot=False)#ADD YOUR TOKEN HERE NOT ANY BOT TOKEN