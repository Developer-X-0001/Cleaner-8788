from discord.ext import commands

import statcord
import config


class StatcordPost(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.key = config.STATCORD_TOKEN
        self.api = statcord.Client(self.bot,self.key)
        self.api.start_loop()


    @commands.Cog.listener()
    async def on_command(self,ctx):
        self.api.command_run(ctx)


async def setup(bot: commands.Bot):
    await bot.add_cog(StatcordPost(bot))