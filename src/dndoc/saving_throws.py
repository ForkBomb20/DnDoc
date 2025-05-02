#!/usr/bin/env python3
"""Saving Throws widget using RadioButton components."""
from textual.app import ComposeResult
from textual.containers import Container
from textual.widgets import SelectionList
from dndoc.data_loader import load_character

class SavingThrows(Container):
    """A saving throws widget with radio buttons indicating proficiency."""
    
    DEFAULT_CSS = """\
    SavingThrows {
        border: round $primary;
        background: $background;
        height: 10;
        min-width: 44;
        color: $foreground;
        border-title-color: $accent;
    }
    
    #selection_list {
        width: 40
    }
    """

    def compose(self) -> ComposeResult:
        """Create child widgets for the saving throws container."""
        data = load_character()
        stats = data["stats"]
        proficiency_bonus = data["proficiency_bonus"]
        saving_throw_bonuses = data["saving_throw_bonuses"]
        
        # Map the abbreviated stat names to full names
        stat_names = {
            "strength": "Strength",
            "dexterity": "Dexterity",
            "constitution": "Constitution", 
            "intelligence": "Intelligence",
            "wisdom": "Wisdom",
            "charisma": "Charisma"
        }
        
        # Create a row for each ability score with RadioSet
        # with RadioSet(disabled=True):
        selection_list = []
        for i, (stat, full_name) in enumerate(stat_names.items()):
            # Calculate modifier
            modifier = (stats[stat] - 10) // 2
            
            # Check if this saving throw has proficiency bonus
            has_proficiency = stat in saving_throw_bonuses or stat[:3] in saving_throw_bonuses
            
            # Add proficiency bonus if proficient
            if has_proficiency:
                modifier += proficiency_bonus
            
            # Format the modifier string
            mod_str = f"{modifier:+d}" if modifier >= 0 else f"{modifier}"
            
            # Create horizontal container for each row
                # RadioButton for proficiency (pre-selected based on proficiency)
            if has_proficiency:
                selection_list.append((f"{full_name} {mod_str}", i, has_proficiency))
            else:
                selection_list.append((f"{full_name} {mod_str}", i))
        
        yield SelectionList[int](*selection_list, disabled=True, id="selection_list")
                    

    def on_mount(self) -> None:
        """Set up the widget when mounted."""
        self.border_title = "Saving Throws"
        self.query_one(SelectionList).highlighted = None