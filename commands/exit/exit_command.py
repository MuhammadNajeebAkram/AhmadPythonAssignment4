from calc_app.commands.command import Command
import sys
class exitCommand(Command):
    def execute(self):
        print("Goodbye")
        sys.exit(0)
    