import discord
from discord import app_commands, ui
from discord.ext import commands
import aiohttp
import io
from utils.db import CaseDB
from utils.case import CaseContainer

class ReportCog(commands.Cog):
    """Cog for /report with error handling."""
    def __init__(self, b: commands.Bot):
        self.b = b
        self.db = CaseDB()
        self.mod_log_channel_id = 123456789012345678  # Replace with mod-log channel ID

    @app_commands.command(name="report", description="Report a user to moderators")
    @app_commands.describe(
        user="User to report",
        reason="Reason for report (optional)",
        image1="Proof1 (optional)",
        image2="Proof2 (optional)",
        image3="Proof3 (optional)",
        image4="Proof4 (optional)"
    )
    @app_commands.checks.bot_has_permissions(send_messages=True, attach_files=True)
    async def report(
        self,
        it: discord.Interaction,
        user: discord.Member,
        reason: str=None,
        image1: discord.Attachment=None,
        image2: discord.Attachment=None,
        image3: discord.Attachment=None,
        image4: discord.Attachment=None
    ):
        """Log user report in mod channel."""
        await it.response.defer(ephemeral=True)
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

        mod_channel = self.b.get_channel(self.mod_log_channel_id)
        if not mod_channel:
            return await it.followup.send("Mod log channel not found.", ephemeral=True)

        try:
            case_id = self.db.add_case(it.user.id, user.id, "Report", reason or "User report", urls)
            c = CaseContainer(it.user, user, "Report", case_id, urls, reason or "User report")
            v = ui.LayoutView()
            v.add_item(c)
            await mod_channel.send(view=v, files=files)
            await it.followup.send("Report submitted.", ephemeral=True)
        except discord.Forbidden:
            return await it.followup.send("Missing permissions.", ephemeral=True)
        except Exception as e:
            return await it.followup.send(f"Error: {e}", ephemeral=True)

async def setup(b: commands.Bot):
    await b.add_cog(ReportCog(b))