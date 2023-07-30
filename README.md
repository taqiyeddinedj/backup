# backup
A simple Python command-line utility for creating backups using the tar command.
Backup Shell is a simple Python command-line utility that allows you to create backups of files and directories using the tar command. This script provides a user-friendly shell interface to interactively select files and directories to be included in the backup, as well as specify the destination for the backup archive.

Getting Started
Follow the instructions below to get started with the Backup Shell:

Prerequisites
Python 3.x
Installation
Clone this repository to your local machine using the following command:
git clone https://github.com/taqiyeddinedj/backup.git
Change directory to the cloned repository:
cd backup-shell
Usage
Run the Backup Shell script:


python3 backup.py
The shell will start, and you will see the prompt >>.

Use the following commands within the shell:

backup: Start the process of creating a backup. The script will prompt you to provide full paths of files and directories you want to include in the backup. To finish adding targets, simply press Enter. Then, you will be asked to specify the destination of the backup. Finally, the backup will be created and saved as a compressed .tar.gz file.

exit: Exit the Backup Shell.

help: Print a list of available commands with their descriptions.

Example
Let's go through a quick example of how to use the Backup Shell:

Start the shell:

>> help

backup: start the backup.
exit: Exits the shell.
help: Print the list of commands.


Contributing
Contributions to the Backup Shell project are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.
