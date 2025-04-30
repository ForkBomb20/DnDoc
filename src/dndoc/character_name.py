#!/usr/bin/env python3
"""Character name widget."""
from textual.app import ComposeResult
from textual.widgets import Label
from textual.containers import Container
from dndoc.data_loader import load_character
from art import text2art

class CharacterName(Container):
    """A character name widget."""
    
    DEFAULT_CSS = """\
    CharacterName {
        border: round $primary;
        background: $background;
        height: 5;
        min-width: 50;
        color: $accent;
    }
    #label {
        border-title-align: left;
    }
    """

    def compose(self) -> ComposeResult:
        """Create a child widgets for the app."""
        character_data = load_character()
        upper = character_data["name"].upper()
        ascii_name = text2art(upper, font="straight")
        lbl = Label(ascii_name, id="label")
        lbl.border_title = "Character Name"
        yield lbl

    def on_mount(self) -> None:
        """Behavior on widget mount."""
        self.theme = "tokyo-night"
        self.border_title = "Character Name"
