import os
import time
import cmd
import subprocess


class MyShell(cmd.Cmd):
    prompt = '>> '
    intro = "Welcome to the backup shell! Type 'help' for a list of available commands."

    # List to collect everything to be backed up
    backup_targets = []

    # Dictionary of the commands
    commands = {
        'backup': 'start the backup.',
        'exit': 'Exits the shell.',
        'help': 'Print the list of commands.'
    }

    def do_backup(self, arg):
        # Ask the user for file and directory paths until they enter an empty line
        while True:
            path = input("Please provide me with the full path (or press Enter to finish):\n").strip()
            if not path:
                break  # Break the loop if the user enters an empty line
            if os.path.exists(path):
                self.backup_targets.append(path)
                print(f"{path} added to backup targets.")
            else:
                print(f"The path '{path}' does not exist. Please provide a valid path.")

        while True:
            # 'dest' variable will contain the machine's destination of the backup
            dest = input("Please provide me with the destination of the backup (or press enter to finish:)\n").strip()
            if not dest:
                break  # Break the loop if the user enters an empty line
            if os.path.exists(dest):
                # Ask the user for the backup name
                backup_name = input("Please type the backup name:\n").strip()
                # Adding timestamp to the backup name
                timestamp = time.strftime("%Y%m%d-%H%M%S")

                # Using the tar command to archive and compress backup
                try:
                    with open(os.devnull, 'w') as devnull:
                        command = ["tar", "czvf", f"{dest}/{backup_name}_{timestamp}.tar.gz", ' '.join(self.backup_targets)]
                        subprocess.run(command, stdout=devnull, stderr=devnull)
                        print("Backup is done!")
                    break  # To quit the loop
                except subprocess.CalledProcessError as e:
                    print(f'Error occurred while creating the backup: {e}')
            else:
                print("The destination does not exist")

    def do_exit(self, arg):
        print("Exiting the shell...")
        return True

    def do_help(self, arg):
        for command, description in self.commands.items():
            print(f"\n{command}: {description}\n")


if __name__ == '__main__':
    my_shell = MyShell()
    my_shell.cmdloop()
