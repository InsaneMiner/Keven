import os

import discord
from discord.ext import commands
import re


bot = commands.Bot(command_prefix='!')


@bot.command()
async def Ping(ctx):
    await ctx.send(f"Pong <@{ctx.author.id}>")

@bot.command()
async def say(ctx, *args):
    await ctx.send(" ".join(args))
