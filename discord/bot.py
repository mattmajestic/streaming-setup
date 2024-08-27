# bot.py
import discord
from discord.ext import commands
from services.github_service import get_latest_github_commit

# Initialize Discord bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command(name='welcome')
async def welcome(ctx):
    await ctx.send('Welcome to the Majestic Coding Server! 🎉👇 Go down below to introduce yourself and check out my YouTube, Twitch & GitHub. 📺🎮💻')

@bot.command(name='github')
async def github(ctx):
    try:
        commit = get_latest_github_commit()
        message = (
            f"Repository: {commit.repo}\n"
            f"Message: {commit.message}\n"
            f"SHA: {commit.sha}\n"
            f"Author: {commit.author}\n"
            f"Date: {commit.date}\n"
            f"URL: {commit.url}"
        )
        await ctx.send(message)
    except Exception as e:
        await ctx.send(f"Failed to fetch the latest commit: {e}")

async def start_discord_bot(discord_bot_key):
    await bot.start(discord_bot_key)
