#!/usr/bin/env python3
"""Hit Points widget."""
from textual.app import ComposeResult
from textual.containers import Container, Center, VerticalGroup, HorizontalGroup, Grid
from textual.widgets import ProgressBar, Label, Button
from dndoc.data_loader import load_character, save_character

class HealthInfo(Container):
    """A character hit points widget."""
    
    DEFAULT_CSS = """\
    HealthInfo {
        border: round $primary;
        background: $background;
        height: 9;
        min-width: 50;
        color: $foreground;
        border-title-color: $accent;
    }

    #hp_bar {
        width: 100%;
        align-horizontal: center;
    }

    #hp_label, #thp_label {
        content-align: center middle;
        width: 100%;
        color: $secondary;
    }

    #status_grid {
        grid-size: 2 1;
        grid-gutter: 1 0;
        height: 3;
        margin-top: 1;
    }
    
    .status_container {
        border: solid $foreground;
        height: 3;
        width: 100%;
    }
    
    #hit_dice_display {
        width: 100%;
        height: 1;
        content-align: center middle;
        color: $secondary
    }
    
    #dice_indicators, #save_indicators {
        align: center middle;
        height: 1;
    }
    
    .dice_button {
        width: 2;
        height: 1;
        content-align: center middle;
        margin: 0 1 0 0;
        background: $success;
    }
    
    .dice_used {
        background: $error;
    }
    
    #death_saves {
        width: 100%;
        height: 1;
        content-align: center middle;
        color: $secondary;
    }
    
    .save_success {
        width: 2;
        height: 1;
        content-align: center middle;
        margin: 0 1 0 0;
        background: $primary-background;
        color: $success;
    }
    
    .save_failure {
        width: 2;
        height: 1;
        content-align: center middle;
        margin: 0 1 0 0;
        background: $primary-background;
        color: $error;
    }
    
    .success_active {
        background: $success;
        color: $text;
    }
    
    .failure_active {
        background: $error;
        color: $text;
    }
    """

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        data = load_character()
        
        with Center():
            with VerticalGroup():
                # HP Bar and Labels
                yield ProgressBar(total=data["hit_points"]["max"], show_percentage=False, show_eta=False, id="hp_bar")
                yield Label(id="hp_label")
                yield Label(id="thp_label")
                
                # Compact status grid with Hit Dice and Death Saves
                with Grid(id="status_grid"):
                    # Hit Dice Section
                    with Container(id="hit_dice", classes="status_container"):
                        yield Label(id="hit_dice_display")
                    
                    # Death Saves Section
                    with Container(id="death_saves_container", classes="status_container"):
                        yield Label(id="death_saves")

    def on_mount(self) -> None:
        """Behavior on mount."""
        data = load_character()
        self.border_title = "Health & Rest"
        
        # Update HP bar and labels
        hp = self.query_one("#hp_bar")
        hp.progress = data["hit_points"]["current"]
        self.query_one("#hp_label").update(f"{data['hit_points']['current']}/{data['hit_points']['max']} HP")
        self.query_one("#thp_label").update(f"Temporary HP: {data['hit_points']['temporary']}")
        
        # Set container labels
        self.query_one("#hit_dice").border_subtitle = "Hit Dice"
        self.query_one("#hit_dice_display").update(f"{data['current_hit_dice']}/{data['max_hit_dice']} {data['hit_die']}")
        
        self.query_one("#death_saves_container").border_subtitle = "Death Saves"
        self.query_one("#death_saves").update(f"{data['death_save_successes']}✓ {data['death_save_failures']}✗")
