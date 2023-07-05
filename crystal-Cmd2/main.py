import cmd
import os
import glob
import color_module as cm#has some useful things
import config
import json
import textwrap
import subprocess as sub
# Colored text escape sequences
class Colors:
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    RESET = "\033[0m"

definitions = json.loads(open("definitions.json").read())

def Error(text):
    print(Colors.RED + text + Colors.RESET)

def Alert(text):
    print(Colors.YELLOW + text + Colors.RESET)


class Command(cmd.Cmd):
    def __init__(self, completionKey) -> 'Command':
        super().__init__()
        self.completekey = completionKey
        self.commands = definitions
        cm.delay(f"Crystal cmd\n", 0.001, ['cyan', "blue"], True)
        print("created by Cross")
        print("https://github.com/cross-sans2/crystal-cmd2")
        print("type \"help\" for a list of commands")
        print(f"os info: name(related to code, and functions) {os.name}, cpu count: {os.cpu_count()}")
        self.prompt = f"{Colors.CYAN}{os.getcwd()}{Colors.RESET}\n:>"
        self.prompt_width = 70  # Adjust the width as needed
        self.input_color = Colors.GREEN  # Color for user input
        
    def format_prompt(self):
        prompt_lines = textwrap.wrap(self.prompt, self.prompt_width)
        formatted_prompt = '\n'.join(prompt_lines)
        return formatted_prompt + ' '
    def do_run(self,args):
        os.system(args)

    def complete_cd(self, text, line, begidx, endidx):
        """
        Tab completion for the 'cd' command.
        """
        dir_names = glob.glob(text + '*/')  # Only match directories
        return dir_names
    def complete_cat(self, text, line, begidx, endidx):
        """
        Tab completion for the 'cat' command.
        """
        file_names = glob.glob(text + '*.*')  # Only match files
        return file_names
    def complete_open(self, text, line, begidx, endidx):
        """
        Tab completion for the 'open' command.
        """
        file_names = glob.glob(text + '*.html')+glob.glob(text+"*.htm")  # Only match files
        return file_names
    def complete_edit(self, text, line, begidx, endidx):
        """
        Tab completion for the 'edit' command.
        """
        files = [f for f in glob.glob(text + "*") if os.path.isfile(f)]
        return files
    def complete_ls(self, text, line, begidx, endidx):
        """
        Tab completion for the 'ls' command.
        """
        dir_files = glob.glob(text + '*/')  # Only match directories
        return dir_files
    def do_help(self, arg: str) -> bool | None:
        if not arg:
            for command in self.commands.values():
                print(f"{Colors.YELLOW}{command['name']} >>> {command['description']}{Colors.RESET}")
        else:
            print(f"{Colors.YELLOW}{self.commands[arg]['name']} >>> {self.commands[arg]['description']}{Colors.RESET}")
    def do_clear(self, arg):
        if os.name == "nt":
            os.system("cls")  # Clear the screen on Windows
        else:
            os.system("clear")  # Clear the screen on Unix-like systems
    def emptyline(self) -> None:
        pass

    def do_load_definitions(self, arg):
        self.commands = json.loads(open("definitions.json").read())
    def do_echo(self, arg):
        """
        Print the provided text.
        Usage: echo <text>
        """
        print(arg)

    def do_calc(self, arg):
        """
        Perform a simple calculation.
        Usage: calc <expression>
        """
        try:
            result = eval(arg)
            print(result)
        except Exception as e:
            Error(f"Error calculating expression: {e}")
    def do_open(self, arg):
        for args in arg.split(' '):
            cm.open_browser(args)
    def do_edit(self,arg):
        os.system(f"nano {arg}")
    def do_ls(self, arg: str) -> None:
        folder = arg or "."
        for item in os.listdir(folder):
            if os.path.isfile(item):
                print(item)
            else:
                print(cm.colored(item,'blue'))
    
    def do_touch(self,args):
        for arg in args.split(' '):
            with open(arg,'w') as f:
                f.write('')
    def do_cat(self,args):
        for arg in args.split(' '):
            print(f"\n===={arg}====")
            try:
                with open(arg,'r') as f:
                    print(f.read())
            except FileNotFoundError as e:
                print(e)

    def do_mkdir(self,arg):
        folders = arg.split(" ")
        for folder in folders:
            os.mkdir(os.path.join(os.getcwd(),folder))

    def do_cd(self, arg: str) -> None:
        folder = arg or "~"  # Default to the home directory if no argument is provided
        folder = os.path.expanduser(folder)  # Expand the "~" or "$HOME" path
        try:
            os.chdir(folder)
            self.prompt = f"{Colors.CYAN}{os.getcwd()}{Colors.RESET}\n:>"
        except FileNotFoundError:
            Error("Directory not found.")
    def default(self, line: str) -> None:
        if line.startswith("(") and line.endswith(")"):
            try:
                result = eval(line[1:-1])
                if result is not None:
                    print(result)
            except Exception as e:
                Error(f"Error executing command: {e}")
        else:
            Error(f"Command not recognized: {line}")
        if line == '..':
            folder = '..'
            folder = os.path.expanduser(folder)
            os.chdir(folder)
            self.prompt = f"{Colors.CYAN}{os.getcwd()}{Colors.RESET}\n:>"
            return
    def cmdloop(self, intro=None):
        if intro is not None:
            self.intro = intro
        self.preloop()
        if self.use_rawinput and self.completekey:
            try:
                import readline
                readline.set_completer(self.complete)
                readline.parse_and_bind(self.completekey+": complete")
            except ImportError:
                pass
        stop = None
        while not stop:
            if self.cmdqueue:
                line = self.cmdqueue.pop(0)
            else:
                if self.use_rawinput:
                    try:
                        line = input(self.format_prompt())  # Use the modified format_prompt() method
                    except EOFError:
                        line = 'EOF'
                else:
                    line = self.stdin.readline()
                    if not len(line):
                        line = 'EOF'
                    else:
                        line = line.rstrip('\r\n')
            line = self.precmd(line)
            stop = self.onecmd(line)
            stop = self.postcmd(stop, line)
        self.postloop()
if __name__ == "__main__":
    main = Command(config.read_completion_key())
    main.cmdloop()
