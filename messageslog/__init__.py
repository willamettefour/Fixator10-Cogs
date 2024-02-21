from .messageslog import MessagesLog
import discord

__red_end_user_data_statement__ = ("This cog does not persistently store data or metadata about users.")

async def setup(bot):
    cog = MessagesLog(bot)
    await cog.initialize()
    if discord.__version__[0] == "2":
        await bot.add_cog(cog)
    else:
        bot.add_cog(cog)