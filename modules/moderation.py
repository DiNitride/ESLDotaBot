import discord
from discord.ext import commands
from utils import checks


class Moderation():
    def __init__(self, bot):
        self.bot = bot

    # Changes the bot's game
    @checks.is_admin()
    @commands.command(hidden=True,pass_conext=True)
    async def changegame(self, *, game: str):
        """Updates the Bot's game"""
        await self.bot.change_status(discord.Game(name=game))
        await self.bot.say("Game updated.")
        print("Updated Bot's Game")

    # Bans a member
    @checks.is_admin()
    @commands.command(hidden=True)
    async def ban(self, member: discord.Member = None):
        """Bans a member"""

        # Checks a user is being kicked
        if member is None:
            return

        # Bans the user
        await self.bot.ban(member, delete_message_days=1)
        #Prints to console
        print("{0.name} has been banned".format(member))

    # Kicks a member
    @checks.is_admin()
    @commands.command(hidden=True)
    async def kick(self, member: discord.Member = None):
        """Kicks a member"""

        # Checks a user is being kicked
        if member is None:
            return

        # Kicks the user
        await self.bot.kick(member)
        # Prints to console
        print("{0.name} has been banned".format(member))

    # Softbans a member
    @checks.is_admin()
    @commands.command(hidden=True,pass_context=True)
    async def softban(self, ctx, member: discord.Member = None):
        """Softbans a member"""
        server = ctx.message.server

        # Checks that there is someone to ban
        if member is None:
            return

        # Bans then unbans the user
        await self.bot.ban(member, delete_message_days=1)
        await self.bot.unban(server, member)
        # Outputs to console
        print("{0.name} has been softbanned".format(member))

def setup(bot):
    bot.add_cog(Moderation(bot))
