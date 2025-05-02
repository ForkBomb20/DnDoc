#!/usr/bin/env python3
"""Skills widget using RadioButton components."""
from textual.app import ComposeResult
from textual.containers import Container
from textual.widgets import SelectionList
from dndoc.data_loader import load_character

class Skills(Container):
    """A Skills widget with radio buttons indicating proficiency."""
    
    DEFAULT_CSS = """\
    Skills {
        border: round $primary;
        background: $background;
        height: 22;
        min-width: 44;
        color: $foreground;
        border-title-color: $accent;
    }
    
    #selection_list {
        width: 40
    }
    """

    def compose(self) -> ComposeResult:
        """Create child widgets for the Skills container."""
        data = load_character()
        stats = data["stats"]
        proficiency_bonus = data["proficiency_bonus"]
        skill_bonuses = data["skill_bonuses"]
        
        # Map the abbreviated stat names to full names
        skill_map = {
            "acrobatics": "dexterity",
            "animal handling": "wisdom",
            "arcana": "intelligence",
            "athletics": "strength",
            "deception": "charisma",
            "history": "intelligence",
            "insight": "wisdom",
            "intimidation": "charisma",
            "investigation": "intelligence",
            "medicine": "wisdom",
            "nature": "intelligence",
            "perception": "wisdom",
            "performance": "charisma",
            "persuasion": "charisma",
            "religion": "intelligence",
            "sleight of hand": "dexterity",
            "stealth": "dexterity",
            "survival": "wisdom"
        }

        
        # Create a row for each ability score with RadioSet
        # with RadioSet(disabled=True):
        selection_list = []
        for i, (skill, prof) in enumerate(skill_map.items()):
            # Calculate modifier
            modifier = (stats[skill_map[skill]] - 10) // 2
            
            # Check if this saving throw has proficiency bonus
            has_proficiency = skill in skill_bonuses
            
            # Add proficiency bonus if proficient
            if has_proficiency:
                modifier += proficiency_bonus
            
            # Format the modifier string
            mod_str = f"{modifier:+d}" if modifier >= 0 else f"{modifier}"
            
            # Create horizontal container for each row
                # RadioButton for proficiency (pre-selected based on proficiency)
            if has_proficiency:
                selection_list.append((f"{skill} ({prof}) {mod_str}", i, has_proficiency))
            else:
                selection_list.append((f"{skill} ({prof}) {mod_str}", i))
        
        yield SelectionList[int](*selection_list, disabled=True, id="selection_list")
                    

    def on_mount(self) -> None:
        """Set up the widget when mounted."""
        self.border_title = "Skills"
        self.query_one(SelectionList).highlighted = None