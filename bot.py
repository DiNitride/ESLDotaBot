#
#
# ESL Dota 2 Offical Server Bot
# Written and updated by DiNitride
#
#

# Importing things
import discord
from discord.ext import commands
from utils import checks

# Set's bot's desciption and prefixes in a list
description = "A bot for the ESL Dota 2 Offical Discord Sever"
bot = commands.Bot(command_prefix=['!','?','esldota2/'], description=description)

#################
##Startup Stuff##
#################

bot.remove_command('help')

@bot.event
async def on_ready():
    # Outputs login data to console
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_status(discord.Game(name="!join / !leave"))

    # Outputs the state of loading the modules to the console
    # So I know they have loaded correctly
    bot.load_extension("modules.moderation")
    print("Loaded Moderation")
    bot.load_extension("modules.subscriptions")
    print("Loaded Subscriptions")

####################
##Misc and Testing##
####################

# Command to update the bot's profile picture
@bot.command(hidden=True)
@checks.is_admin()
async def updateimage():
    #Loads and sets the bot's profile image
    with open("logo.jpg","rb") as logo:
        await bot.edit_profile(avatar=logo.read())

# Ping Pong
# Testing the response of the bot
@bot.command(hidden=True)
async def ping():
    """Pong"""
    await bot.say("Pong")
    print("Ping Pong")

############################
##FANCY TOKEN LOGIN STUFFS##
############################

with open("token.txt","r") as token:
    bot.run(token.read())
