"""
Copyright © Krypton 2019-Present - https://github.com/kkrypt0nn (https://krypton.ninja)
Description:
🐍 A simple template to start to code your own and personalized Discord bot in Python

Version: 6.4.0
"""

import discord
from discord.ext import commands
from discord.ext.commands import Context
import pyotp

totp = pyotp.TOTP('ps62mqkfws23ystsncwqwpxudqpltzrx')
totp.now()

# Here we name the cog and create a new class for the cog.
class TOTP(commands.Cog, name="totp"):
    def __init__(self, bot) -> None:
        self.bot = bot

    # Here you can just add your own commands, you'll always need to provide "self" as first parameter.

    @commands.hybrid_command(
        name="totp",
        description="Generates a TOTP code.",
    )
    async def coinflip(self, context: Context) -> None:
        """
        Make a coin flip, but give your bet before.

        :param context: The hybrid command context.
        """
        embed = discord.Embed(
            description=f"TOTP is `{totp.now()}`!",
            color=0xBEBEFE,
        )
        await context.send(embed=embed)


# And then we finally add the cog to the bot so that it can load, unload, reload and use it's content.
async def setup(bot) -> None:
    await bot.add_cog(TOTP(bot))
