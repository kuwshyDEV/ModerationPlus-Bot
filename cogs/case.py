import discord
from discord import app_commands, ui
from discord.ext import commands
from utils.db import CaseDB
from utils.case import CaseContainer

class CaseCog(commands.Cog):
    """Cog for /case to retrieve case by ID."""
    def __init__(self, b: commands.Bot):
        self.b = b
        self.db = CaseDB()

    @app_commands.command(name="case", description="Retrieve case by ID")
    @app_commands.describe(case_id="Case ID to retrieve")
    @app_commands.checks.bot_has_permissions(send_messages=True, attach_files=True)
    async def case(self, it: discord.Interaction, case_id: str):
        """Display case UI from database."""
        await it.response.defer()
        case = self.db.get_case(case_id)
        if not case:
            return await it.followup.send("Case not found.", ephemeral=True)

        try:
            mod = await self.b.fetch_user(case["mod_id"])
            tgt = await it.guild.fetch_member(case["tgt_id"])
        except discord.NotFound:
            return await it.followup.send("User data unavailable.", ephemeral=True)
        except Exception as e:
            return await it.followup.send(f"Error: {e}", ephemeral=True)

        c = CaseContainer(mod, tgt, case["type"], case_id, case["files"], case["reason"])
        v = ui.LayoutView()
        v.add_item(c)
        await it.followup.send(view=v)

async def setup(b: commands.Bot):
    await b.add_cog(CaseCog(b))