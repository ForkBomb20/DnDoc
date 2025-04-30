#!/usr/bin/env python3
"""Character info widget."""
from textual.app import ComposeResult
from textual.containers import Container, HorizontalGroup
from textual.widgets import Label
from dndoc.data_loader import load_character

class CharacterInfo(Container):
    """A character info widget."""
    
    DEFAULT_CSS = """\
    CharacterInfo {
        border: round $primary;
        background: $background;
        height: 7;
        min-width: 50;
        color: $foreground;
    }
    .info_label {
        border-subtitle-align: center;
        border: solid $foreground;
        color: $foreground;
        min-width: 25;
        text-align: center;
        margin: 1 1
    }

    """

    def compose(self) -> ComposeResult:
        """Create a child widgets for the app."""
        data = load_character()
        player_info = data["player_info"]
        level = player_info["level"]
        character_class = player_info["class"]
        self.class_lbl = Label(f"Level {level} {character_class}", classes="info_label")
        self.bkgr_lbl = Label(player_info["background"], classes="info_label")
        self.player_name_lbl = Label(player_info["player_name"], classes="info_label")
        self.race_lbl = Label(player_info["race"], classes="info_label")
        self.alignment_lbl = Label(player_info["alignment"], classes="info_label")
        self.exp_lbl = Label(player_info["exp_points"], classes="info_label")
        yield HorizontalGroup(self.class_lbl, self.bkgr_lbl, self.player_name_lbl,
                              self.race_lbl, self.alignment_lbl, self.exp_lbl)

    def on_mount(self) -> None:
        """Behavior"""
        self.theme = "tokyo-night"
        self.border_title = "Character Info"
        self.class_lbl.border_subtitle = "Class & Level"
        self.bkgr_lbl.border_subtitle = "Background"
        self.player_name_lbl.border_subtitle = "Player Name"
        self.race_lbl.border_subtitle = "Race"
        self.alignment_lbl.border_subtitle = "Alignment"
        self.exp_lbl.border_subtitle = "Experience Points"
    
