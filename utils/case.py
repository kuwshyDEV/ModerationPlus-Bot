import discord
from discord import ui, Color
from datetime import datetime

class CaseContainer(ui.Container):
    """Structured case UI with dynamic fields and separate proof."""
    def __init__(self, mod: discord.User, tgt: discord.Member, c_type: str, code: str, file_urls: list[str]=None, reason: str="Test case"):
        super().__init__(accent_color=Color.orange())  # Theme color

        # Case: Numeric code and type
        self.add_item(ui.TextDisplay(f"**Case {code}** - {c_type}"))
        self.add_item(ui.Separator())  # Divider

        # Target: Dynamic user details
        tgt_txt = ui.TextDisplay(f"**Target User** - {tgt.display_name} ({tgt.id})\n**Total Cases** - 1")
        self.add_item(tgt_txt)
        self.add_item(ui.Separator())

        # Mod: Dynamic moderator
        mod_txt = ui.TextDisplay(f"**Moderator** - {mod.display_name} ({mod.id})")
        self.add_item(mod_txt)
        self.add_item(ui.Separator())

        # Reason: Dynamic input
        rsn = ui.TextDisplay(f"**Reason for Action**\n> {reason}")
        self.add_item(rsn)
        self.add_item(ui.Separator())

        # Proof: Separate section if URLs exist
        if file_urls:
            self.add_item(ui.TextDisplay("**Proof**"))
            gal = ui.MediaGallery()
            for url in file_urls:
                gal.add_item(media=url, spoiler="SPOILER_" in url)
            self.add_item(gal)
            self.add_item(ui.Separator())

        # Timestamp: Current time
        ts = int(datetime.now().timestamp())
        tsp = ui.TextDisplay(f"**Timestamp** - <t:{ts}:F> (<t:{ts}:R>)")
        self.add_item(tsp)
        self.add_item(ui.Separator())

        # Actions: Update, Revoke, History
        ar1 = ui.ActionRow()
        ar1.add_item(ui.Button(label="Update Reason", style=discord.ButtonStyle.primary, emoji="✏️", custom_id="edit"))
        ar1.add_item(ui.Button(label="Revoke", style=discord.ButtonStyle.danger, emoji="🗑️", custom_id="revoke"))
        ar1.add_item(ui.Button(label="User History", style=discord.ButtonStyle.secondary, emoji="📋", custom_id="hist"))
        self.add_item(ar1)

        # Actions: Export, Share, Appeal
        ar2 = ui.ActionRow()
        ar2.add_item(ui.Button(label="Export", style=discord.ButtonStyle.secondary, emoji="📥", custom_id="exp"))
        ar2.add_item(ui.Button(label="Share Case", style=discord.ButtonStyle.secondary, emoji="🔗", custom_id="shr"))
        ar2.add_item(ui.Button(label="Appeal Status", style=discord.ButtonStyle.link, emoji="📋", url="https://example.com"))
        self.add_item(ar2)