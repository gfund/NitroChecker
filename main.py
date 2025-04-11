
import os #used to access .env file 

import discord

import discord.ext
from discord.ext import commands
############SETUP#################


intents = discord.Intents.default()
intents.members = True
intents.messages=True
bot = commands.Bot(command_prefix='!',intents=intents)
#############ENDSETUP##############
############EVENTS#################
@bot.event
async def on_ready():
 #change status
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Out for You"))

@bot.event
async def on_message(message):
 
  await bot.process_commands(message)
##############ENDEVENTS#############

#COMMANDS 
#----------------------------
#just incase but not really neccessary
@bot.command()
async def ping(ctx):
    await ctx.send((str((bot.latency*1000))) + "ms")

#helper function to check nitro
def quickChecker(nitro): 
        import requests
        # discord link
        url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
        response = requests.get(url) # Get the response from discord if any
        print(response)
        if response.status_code == 200: # If the responce went through
          return True
           
        else: 
            return False # Tell the main function there was not a code found


@bot.command()
async def nitrocheck(ctx,*,code):
  code=code.replace("https://discord.gift/","")
  if(quickChecker(code)):
    await ctx.send("VALID!")
  else: 
    await ctx.send("INVALID!")




#RUN BOT CODE

#<---you can put a webserver here if you want to keep the bot online longer(make sure to uncomment)
    
#get the token from .env 
TOKEN=os.environ.get("DISCORD_BOT_SECRET")
#RUN
bot.run(TOKEN)
