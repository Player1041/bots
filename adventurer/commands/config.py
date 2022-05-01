import disnake
from disnake.ext import commands

class Config(commands.Cog):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot



def setup(bot):
    bot.add_cog(Config(bot))
    print("Loaded Configuration Settings!")