import discord
from redbot.core import commands

class Fu_reply(commands.Cog):
    """Auto-replies to my friends' classic phrase"""
    def __init__(self, bot):
        self.bot = bot

    @commands.guild_only()
    @commands.Cog.listener()
    async def on_message_without_command(self, message: discord.Message):
        if message.author.bot:
            return
        if message.content.lower() == "fucking benny":
            await message.channel.send("fucking " + format(message.author.display_name))
            return