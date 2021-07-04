import logging

from discord import Embed
from discord.ext.commands import Bot, Cog, Context, group


from lemonbot.constants import Channels, Users, LOGO

log = logging.getLogger(__name__)


class Minecraft(Cog):
    """Provide minecraft-related features and info."""

    def __init__(self, bot: Bot):
        """Initialize this cog with the Bot instance."""
        self.bot = bot

    @group(name='minecraft', aliases=('smp', 'realm', 'mc'))
    async def minecraft(self, ctx: Context):
        """A group that provides various minecraft info."""
        mc_rules = self.bot.get_channel(Channels.mc_rules)
        mc_chat = self.bot.get_channel(Channels.mc_chat)
        mc_modpacks = self.bot.get_channel(Channels.mc_modpacks)
        gargoyle = self.bot.get_user(Users.gargoyle)

        embed = Embed(
            colour=1416344,
            description=(
                f"This community has a minecraft server, generously hosted by {gargoyle.mention}!"
                f"Head over to {mc_chat.mention} if you wanna discuss it."
            ),
        )

        embed.set_author(
            name="Gargoyle's SMP",
            icon_url=LOGO
        )
        embed.set_thumbnail(
            url=LOGO
        )
        embed.add_field(
            name="Whitelist",
            value=f"Contact {gargoyle.mention} to be added to the realm.",
            inline=False,
        )
        embed.add_field(
            name="Version",
            value="1.17",
        )
        embed.add_field(
            name="Modpack",
            value="1 person sleep, armored elytra, durability ping, "
                  "player heads, mob heads, /tpa, /home, more to come..\n\n"
                  f"To use these modpacks check out {mc_modpacks.mention}",
            inline=False,
        )
        embed.add_field(
            name="Rules",
            value=f"See {mc_rules.mention}",
            inline=False,
        )

        await ctx.send(embed=embed)


def setup(bot: Bot) -> None:
    """
    Load the minecraft cog
    """
    bot.add_cog(Minecraft(bot))
    log.info("Cog loaded: Minecraft")
