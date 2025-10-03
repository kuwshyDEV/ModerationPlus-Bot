import discord
from discord import app_commands, ui
from discord.ext import commands
import aiohttp
import io
from utils.db import CaseDB
from utils.case import CaseContainer

class UnbanCog(commands.Cog):
    """Cog for /unban by user ID."""
    def __init__(self, b: commands.Bot):
        self.b = b
        self.db = CaseDB()

    @app_commands.command(name="unban", description="Unban user by ID with proof")
    @app_commands.describe(
        user_id="Target user ID",
        reason="Reason (optional)",
        image1="Proof1 (optional)",
        image2="Proof2 (optional)",
        image3="Proof3 (optional)",
        image4="Proof4 (optional)"
    )
    @app_commands.default_permissions(ban_members=True)
    @app_commands.checks.bot_has_permissions(ban_members=True, attach_files=True)
    async def unban(
        self,
        it: discord.Interaction,
        user_id: str,
        reason: str=None,
        image1: discord.Attachment=None,
        image2: discord.Attachment=None,
        image3: discord.Attachment=None,
        image4: discord.Attachment=None
    ):
        """Unban user, log case."""
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
            user = await self.b.fetch_user(int(user_id))
            await it.guild.unban(user, reason=reason or "Test")
        except discord.NotFound:
            return await it.followup.send("User not found or not banned.", ephemeral=True)
        except discord.Forbidden:
            return await it.followup.send("Missing permissions.", ephemeral=True)
        except Exception as e:
            return await it.followup.send(f"Error: {e}", ephemeral=True)

        case_id = self.db.add_case(it.user.id, user.id, "Unban", reason or "Test", urls)
        c = CaseContainer(it.user, user, "Unban", case_id, urls, reason or "Test")
        v = ui.LayoutView()
        v.add_item(c)
        await it.followup.send(view=v, files=files)

async def setup(b: commands.Bot):
    await b.add_cog(UnbanCog(b))