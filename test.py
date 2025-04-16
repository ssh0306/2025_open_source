with open(".gitignore", "r") as file_pointer:
    git_ignore = file_pointer.readline()
    print(git_ignore)