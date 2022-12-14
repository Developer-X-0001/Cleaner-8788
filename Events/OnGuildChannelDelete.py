import aiosqlite
import discord
import typing
from discord import app_commands
from discord.ext import commands

class OnGuildJoin(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel: discord.TextChannel):
        async with self.bot.database.execute(f"SELECT channel_id FROM AuditChannels WHERE guild_id = {channel.guild.id}") as cursor:
            data = await cursor.fetchone()
        if data is None:
            pass
        else:
            if channel.id == data[0]:
                await self.bot.database.execute(f"DELETE FROM AuditChannels WHERE guild_id = {channel.guild.id}")
                await self.bot.database.commit()
            else:
                pass

async def setup(bot: commands.Bot):
    await bot.add_cog(
        OnGuildJoin(bot))