#!/usr/bin/env python3
"""Character name widget."""
from textual import on
from textual.app import ComposeResult
from textual.widgets import Input, Pretty
from textual.containers import Container

class CharacterName(Container):
    """A character name widget."""
    
    DEFAULT_CSS = """\
    CharacterName {
        border: round #c971e9;
        background: #0a1a2f;
        # padding: 1 2;
        height: 5;
        min-width: 50;
    }
    """
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        """Create a child widgets for the app."""
        yield Input(
            placeholder="Enter a character name..."
    )
