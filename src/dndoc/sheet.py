#!/usr/bin/env python3
"""Main file for D&D character sheet CLI."""
from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, TabbedContent, TabPane, Label
from dndoc.character_name import CharacterName
from dndoc.character_info import CharacterInfo

class CharacterSheet(App):
    """A Textual app to manage a D&D character sheet."""

    def compose(self) -> ComposeResult:
        """Create a child widgets for the app."""
        CSS_PATH = "dndoc/theme.tcss"
        yield Header(id="header")
        with TabbedContent():
            with TabPane("Stats"):
                yield CharacterName()
                yield CharacterInfo()
                yield Label("Stats")
            with TabPane("Actions"):
                yield CharacterName()
                yield Label("Actions")
            with TabPane("Spells"):
                yield CharacterName()
                yield Label("Spells")
            with TabPane("Inventory"):
                yield CharacterName()
                yield Label("Inventory")
            with TabPane("Features"):
                yield CharacterName()
                yield Label("Features")
        # yield CharacterName()
        yield Footer(id="footer")
    

    def on_mount(self) -> None:
        self.theme = "tokyo-night"
