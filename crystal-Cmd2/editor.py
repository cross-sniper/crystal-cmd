import os, color_module

def add(content, file):
    print("Current content:")
    for line_number, line in enumerate(lines, start=1):
        print(f"{color_module.color_text(line_number,'yellow')}: {line}")

    # Append text to the content
    text = input("Enter the text to append: ")
    if text == '':
        return 1
    content += text + "\n"

    # Save the modified content back to the file
    with open(file, 'w') as f:
        f.write(content)
    add(content,file)
def main(file: str):
    if os.path.isfile(file):
        with open(file, 'r') as f:
            content = f.read()

        # Split the content into lines
        lines = content.split('\n')

        # Editor loop
        while True:
            # Display the current content with line numbers
            print("Current content:")
            for line_number, line in enumerate(lines, start=1):
                print(f"{color_module.color_text(line_number,'yellow')}: {line}")

            # Prompt the user for an action
            action = input("Enter an action (a: append, r: replace, d: delete, q: quit): ")
            if action == 'a':
                add(content, file)

            elif action == 'r':
                # Replace text in the content
                old_text = input("Enter the text to replace: ")
                new_text = input("Enter the new text: ")
                content = content.replace(old_text, new_text)

            elif action == 'd':
                # Delete text from the content
                text = input("Enter the text to delete: ")
                content = content.replace(text, '')

            elif action == 'q':
                # Quit the editor
                break

            else:
                print("Invalid action. Please try again.")
    else:
        print("file not found")
        return