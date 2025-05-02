#!/usr/bin/env python3
"""Character performance widget."""
from textual.app import ComposeResult
from textual.containers import Container, HorizontalGroup, Center, VerticalGroup
from textual.widgets import Label
from dndoc.data_loader import load_character
from art import text2art

class Performance(Container):
    """An combat, mobility, and performance widget."""
    
    DEFAULT_CSS = """\
    Performance {
        border: round $primary;
        background: $background;
        height: 8;
        min-width: 50;
        color: $foreground;
        border-title-color: $accent;
    }
    .performance_label {
        border-subtitle-align: center;
        border: solid $foreground;
        color: $secondary;
        min-width: 20;
        height: 6;
        text-align: center;
        content-align-vertical: middle;
        content-align-horizontal: center;
    }
    """

    def compose(self) -> ComposeResult:
        """Create a child widgets for the app."""
        data = load_character()
        features = ["armor_class", "initiative_bonus", "speed", "proficiency_bonus"]
        with HorizontalGroup():
            for feature in features:
                val = data[feature]
                feature_str = str(val)
                if feature[-5:] == "bonus":
                    if val >= 0:
                        feature_str = "+" + feature_str
                art = text2art(feature_str, font="straight")
                with VerticalGroup():
                    with Center():
                        yield Label(art, classes="performance_label", id=feature)


    def on_mount(self) -> None:
        """Behavior"""
        self.theme = "tokyo-night"
        self.border_title = "Combat & Mobility"
        data = load_character()
        features = ["armor_class", "initiative_bonus", "speed", "proficiency_bonus"]
        for feature in features:
            self.query_one(f"#{feature}").border_subtitle = feature.split("_")[0].capitalize()
            # yield Label(art, classes="ability_label", id=f"{stat}")
        
    
