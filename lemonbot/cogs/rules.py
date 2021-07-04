import logging

from discord import Embed
from discord.ext.commands import Bot, Cog, Context, group

from lemonbot import constants


log = logging.getLogger(__name__)

class Rules(Cog):
    """The rules for the server"""

    def __init__(self, bot: Bot):
        """Initialze this cog with the Bot instance."""
        self.bot = Bot

    @group(name='rules', aliases=('rule', 'r'))
    async def rules(self, ctx: Context):
        """Show the Discord and Minecraft server rules."""
        embed = Embed(
            colour=1416344,
            description=(
               "This is the rules of this discord server and the "
               "minecraft realm."
            ),
        )

        embed.set_author(
            name='Rules',
            icon_url=constants.LOGO
        )

        embed.add_field(
            name="Discord Server Rules.",
            value='-----------------',
        )

        for i, rule in enumerate(constants.DISCORD_RULES, start=1):
            embed.add_field(
                name=f'Rule {i}',
                value=rule,
                inline=False,
        )

        await ctx.send(embed=embed)


def setup(bot: Bot) -> None:
    """
    Load the minecraft cog
    """
    bot.add_cog(Rules(bot))
    log.info("Cog loaded: Minecraft")
