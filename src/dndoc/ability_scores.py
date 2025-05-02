#!/usr/bin/env python3
"""Character ability widget."""
from textual.app import ComposeResult
from textual.containers import Container, HorizontalGroup, Center, VerticalGroup
from textual.widgets import Label
from dndoc.data_loader import load_character
from art import text2art

class AbilityScores(Container):
    """An ability score widget."""
    
    DEFAULT_CSS = """\
    AbilityScores {
        border: round $primary;
        background: $background;
        height: 10;
        min-width: 50;
        color: $foreground;
        border-title-color: $accent;
    }
    .ability_label {
        border-subtitle-align: center;
        border: solid $foreground;
        color: $foreground;
        min-width: 20;
        height: 6;
        text-align: center;
        content-align-vertical: middle;
        content-align-horizontal: center;
        color: $secondary;
    }
    #mod{
        color: $secondary;
    }
    """

    def compose(self) -> ComposeResult:
        """Create a child widgets for the app."""
        data = load_character()
        stats = data["stats"]
        with HorizontalGroup():
            for stat in stats:
                art = text2art(str(stats[stat]), font="straight")
                mod = (stats[stat] - 10) // 2
                mod_str = str(mod)
                if mod >= 0:
                    mod_str = "+" + mod_str
                with VerticalGroup():
                    with Center():
                        yield Label(art, classes="ability_label", id=stat)
                        yield Label(mod_str, id="mod")


    def on_mount(self) -> None:
        """Behavior"""
        self.theme = "tokyo-night"
        self.border_title = "Ability Scores"
        data = load_character()
        stats = data["stats"]
        for stat in stats:
            self.query_one(f"#{stat}").border_subtitle = stat.capitalize()
            # yield Label(art, classes="ability_label", id=f"{stat}")
        
    
