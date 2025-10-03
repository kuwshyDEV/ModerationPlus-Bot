import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

kuwshy = commands.Bot(command_prefix="$", intents=intents)

@kuwshy.event
async def on_ready():
    print("----------------------------------------")
    print(f"Logged in as {kuwshy.user.name} ({kuwshy.user.id})")
    print("----------------------------------------")
    
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            cog_name = f"cogs.{filename[:-3]}"
            try:
                await kuwshy.load_extension(cog_name)
                print(f"✓ Loaded {cog_name}")
            except Exception as e:
                print(f"✗ Failed to load {cog_name}: {e}")

    try:
        synced = await kuwshy.tree.sync()
        print(f"✓ Synced {len(synced)} command(s)")
        print("----------------------------------------")
    except Exception as e:
        print(f"✗ Failed to sync commands: {e}")

@kuwshy.event
async def on_interaction(interaction: discord.Interaction):
    try:
        if interaction.type == discord.InteractionType.component:
            pass
    except Exception as e:
        print(f"Interaction error: {e}")

@kuwshy.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
    print(f"Error: {error}")

# Run the bot
if __name__ == "__main__":
    token = os.getenv("DISCORD_TOKEN")
    if not token:
        print("Error: DISCORD_TOKEN not found in .env file")
    else:
        kuwshy.run(token)
