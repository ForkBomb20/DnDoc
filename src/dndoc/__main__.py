"""The main entry point for the DnDoc CLI."""

from dndoc.sheet import CharacterSheet

def main():
    app = CharacterSheet()
    app.run()

if __name__ == "__main__":
    main()