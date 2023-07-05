# Project Crystal

Project Crystal is a command-line interface that combines the functionality of a command prompt with the ability to execute Python code. It provides an interactive environment where you can navigate the file system, run commands, and perform Python calculations.

## Key Features

### 1. Command Execution

Project Crystal allows you to execute various commands, including built-in commands and custom commands defined in the `definitions.json` file. Some of the available commands are:

- `ls`: Returns the contents of the folder provided or the current folder.
- `cd`: Changes the working directory to the provided folder or the user's "home" directory.
- `clear`: Clears the console window.
- `mkdir`: Creates one or more directories.
- `touch`: Creates empty files.
- `edit`: Opens a simple text editor (work in progress).
- `cat`: Outputs the content of the given files.
- `open`: Opens the given HTML/HTM file in the system's default web browser.
- `echo`: Prints the provided text to the console.
- `calc`: Performs a simple calculation with the provided expression.
- `help`: Outputs the command's name and description.

### 2. Python Code Execution

You can execute Python code directly within Project Crystal by enclosing the code in parentheses "()" and pressing enter. For example:

```
(3 + 5)
```

This will execute the Python expression `3 + 5` and print the result.

### 3. Tab Completion

Project Crystal provides tab completion for certain commands, making it easier and faster to navigate the file system and enter command arguments. Tab completion is available for commands like `cd`, `cat`, `open`, `edit`, and `ls`, allowing you to quickly select files and directories.

### 4. Customization

Project Crystal allows you to customize the available commands and their descriptions by modifying the `definitions.json` file. You can add new commands or modify existing ones to suit your needs.

### 5. Color Formatting

The console output in Project Crystal is enhanced with color formatting. Error messages are displayed in red, alerts in yellow, and user input in green, providing a visually appealing and informative interface.

## Getting Started

To get started with Project Crystal, follow these steps:

1. Clone the Project Crystal repository.
2. Install the required dependencies.
3. Customize the `definitions.json` file to define your own commands if desired.
4. Run the `command.py` script to start Project Crystal.

## Contribution

Contributions to Project Crystal are welcome! If you find any issues or have ideas for new features, please open an issue or submit a pull request on the GitHub repository.

## License

Project Crystal is released under the [MIT License](https://opensource.org/licenses/MIT). Feel free to use, modify, and distribute the code as per the license terms.

Enjoy using Project Crystal!