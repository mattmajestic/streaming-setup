# bot.py
import time
import asyncio
import discord
from discord.ext import commands
from services.github_service import latest_github_commit
from services.youtube_service import latest_youtube_release

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
        commit = latest_github_commit()
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
        
@bot.command(name='youtube')
async def youtube(ctx):
    try:
        release = latest_youtube_release()
        message = (
            f"Latest YouTube Video:\n"
            f"Title: {release.title}\n"
            f"URL: {release.url}"
        )
        await ctx.send(message)
    except Exception as e:
        await ctx.send(f"Failed to fetch the latest YouTube video: {e}")

async def start_discord_bot(discord_bot_key):
    await asyncio.sleep(5)  # Adding a delay before starting the bot
    try:
        await bot.start(discord_bot_key)
    except discord.errors.HTTPException as e:
        if e.status == 429:  # Check for rate limit error
            print("Rate limit hit, retrying after a delay...")
            await asyncio.sleep(60)  # Wait for a minute before retrying
            await start_discord_bot(discord_bot_key)
        else:
            raise e
