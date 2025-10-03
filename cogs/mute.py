import discord
from discord import app_commands, ui
from discord.ext import commands
import aiohttp
import io
from utils.db import CaseDB
from utils.case import CaseContainer

class MuteCog(commands.Cog):
    """Cog for /mute with role-based mute."""
    def __init__(self, b: commands.Bot):
        self.b = b
        self.db = CaseDB()

    @app_commands.command(name="mute", description="Mute user with duration and proof")
    @app_commands.describe(
        user="Target user",
        duration="Duration in minutes (1-43200)",
        reason="Reason (optional)",
        image1="Proof1 (optional)",
        image2="Proof2 (optional)",
        image3="Proof3 (optional)",
        image4="Proof4 (optional)"
    )
    @app_commands.default_permissions(manage_roles=True)
    @app_commands.checks.bot_has_permissions(manage_roles=True, attach_files=True)
    async def mute(
        self,
        it: discord.Interaction,
        user: discord.Member,
        duration: int,
        reason: str=None,
        image1: discord.Attachment=None,
        image2: discord.Attachment=None,
        image3: discord.Attachment=None,
        image4: discord.Attachment=None
    ):
        """Apply mute role, log case."""
        await it.response.defer()
        imgs = [i for i in [image1, image2, image3, image4] if i]
        if len(imgs) > 4:
            return await it.followup.send("Max 4 images.", ephemeral=True)
        if duration < 1 or duration > 43200:
            return await it.followup.send("Duration must be 1-43200 minutes.", ephemeral=True)

        files, urls = [], []
        async with aiohttp.ClientSession() as s:
            for att in imgs:
                async with s.get(att.url) as r:
                    if r.status != 200:
                        return await it.followup.send("Image fetch failed.", ephemeral=True)
                    d = await r.read()
                    f = discord.File(io.BytesIO(d), att.filename, spoiler=att.is_spoiler())
                    files.append(f)
                    urls.append(att.url)

        mute_role = discord.utils.get(it.guild.roles, name="Muted")
        if not mute_role:
            return await it.followup.send("Muted role not found.", ephemeral=True)

        try:
            await user.add_roles(mute_role, reason=reason or "Test")
        except discord.Forbidden:
            return await it.followup.send("Missing permissions.", ephemeral=True)
        except Exception as e:
            return await it.followup.send(f"Error: {e}", ephemeral=True)

        case_id = self.db.add_case(it.user.id, user.id, "Mute", reason or f"Muted for {duration}m", urls)
        c = CaseContainer(it.user, user, "Mute", case_id, urls, reason or f"Muted for {duration}m")
        v = ui.LayoutView()
        v.add_item(c)
        await it.followup.send(view=v, files=files)

async def setup(b: commands.Bot):
    await b.add_cog(MuteCog(b))