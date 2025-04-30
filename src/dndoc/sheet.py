#!/usr/bin/env python3
"""Main file for D&D character sheet CLI."""
from textual.app import App, ComposeResult
from textual.widgets import Footer, Header
from dndoc.character_name import CharacterName

class CharacterSheet(App):
    """A Textual app to manage a D&D character sheet."""

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        """Create a child widgets for the app."""
        CSS_PATH = "css/theme.tcss"
        yield Header(id="header")
        yield CharacterName()
        yield Footer(id="footer")

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )
