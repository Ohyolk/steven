#3.1
# Git vs. GitHub:
# Git is the tool that tracks changes in your code.
# GitHub is a website where you can store and share your Git projects online.

# Terminal vs. Command Line:
# The terminal is a text window where you type commands
# to control your computer, like moving files or running Git.

# Local vs. Remote Repository:
# Local = the folder with your code on your computer.
# Remote = the copy of that same project stored online.

# Version Control:
# A system that keeps track of all changes made to files so you can go back to old versions if needed.

# Staging Area:
# A place in Git where you put files that you’re ready to commit.
# “waiting room”.

# git add
# Adds changes to the staging area.

# git commit
# Saves the changes in Git with a message describing what you did.

# git push
# Sends your committed changes from your local computer to your GitHub repo.

# git status
# Shows which files are new, changed, or staged.

# git pull
# Downloads the newest version of the project from GitHub to your local computer.

# pwd
# “Print working directory”.

# ls
# Lists all files and folders in your current directory.

# cd
# “Change directory”.

# nano
# Opens a simple text editor right in the terminal so you can type or edit files.

# touch
# Creates a new empty file.

# mv
# Moves or renames a file.

# rm
# Deletes a file.

# cat
# Displays the contents of a file in the terminal.

# 3.2

#pwd

#ls

#cd ~/python_decal/brianna_repo
#git pull

#mv homework.py ../judy_decal/homework/

#cd ../judy_decal/homework

#cat homework.py

#git add homework.py

#git commit -m "Finished homework"

#git push

# If you get an error saying updates were rejected, pull the newest version first
#git pull origin main
#git push

#cd ~/Recent

#4.1
def checkDataType(value):
    return str(type(value))

#4.2
def evenOrOdd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
#5
def sumWithLoop(numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total

#6.1
def duplicateList(list):
    new_list = []
    for item in list:
        new_list.append(item)
        new_list.append(item)
    return new_list

#6.2 #fav code
def square(num): #missing colon
    return num * num

