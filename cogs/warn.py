import discord
from discord import app_commands, ui
from discord.ext import commands
import aiohttp
import io
from utils.db import CaseDB
from utils.case import CaseContainer

class WarnCog(commands.Cog):
    """Cog for /warn with error resilience."""
    def __init__(self, b: commands.Bot):
        self.b = b
        self.db = CaseDB()

    @app_commands.command(name="warn", description="Warn user with optional proof")
    @app_commands.describe(
        user="Target", reason="Reason (opt)", image1="Proof1 (opt)", image2="Proof2 (opt)", image3="Proof3 (opt)", image4="Proof4 (opt)"
    )
    @app_commands.default_permissions(moderate_members=True)
    @app_commands.checks.bot_has_permissions(send_messages=True, attach_files=True)
    async def warn(self, it: discord.Interaction, user: discord.Member, reason: str=None, image1: discord.Attachment=None, image2: discord.Attachment=None, image3: discord.Attachment=None, image4: discord.Attachment=None):
        """Send warn DM, log case."""
        await it.response.defer()
        imgs = [i for i in [image1, image2, image3, image4] if i]
        if len(imgs) > 4:
            return await it.followup.send("Max 4 images.", ephemeral=True)

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

        try:
            await user.send(f"Warned: {reason or 'Test'}")
        except discord.Forbidden:
            await it.followup.send("DM failed.", ephemeral=True)
        except Exception as e:
            return await it.followup.send(f"Error: {e}", ephemeral=True)

        case_id = self.db.add_case(it.user.id, user.id, "Warn", reason or "Test", urls)
        c = CaseContainer(it.user, user, "Warn", case_id, urls, reason or "Test")
        v = ui.LayoutView()
        v.add_item(c)
        await it.followup.send(view=v, files=files)

async def setup(b: commands.Bot):
    await b.add_cog(WarnCog(b))