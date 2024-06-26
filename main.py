
from calc_app import CommandHandler, addCommand, subCommand, multiCommand, divideCommand, exitCommand, greetCommand, goodbyeCommand, menuCommand


class App:
    def __init__(self):
        self.command_handler = CommandHandler()
        self.start()
    def start(self):
       self.command_handler.register_command("menu", menuCommand())
       self.command_handler.register_command("add", addCommand())
       self.command_handler.register_command("subtract", subCommand())
       self.command_handler.register_command("multiply", multiCommand())
       self.command_handler.register_command("divide", divideCommand())
       self.command_handler.register_command("greet", greetCommand())
       self.command_handler.register_command("goodbye", goodbyeCommand())
       self.command_handler.register_command("exit", exitCommand())

       print("Type exit to exit from Program")
       while True:
          self.command_handler.execute_command(input(">>>").strip())
if __name__ == "__main__":
    App()