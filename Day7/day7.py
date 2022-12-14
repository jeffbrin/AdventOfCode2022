class File:
    def __init__(self, name: str, size: int) -> None:
        self.name = name
        self.size = size

class Directory:
    def __init__(self, name: str, parent = None) -> None:
        self.name = name
        self.directories = []
        self.files = []
        self.parent = parent

    def add_sub_directory(self, directory) -> None:
        self.directories.append(directory)

    def add_file(self, file: File) -> None:
        self.files.append(file)

    def get_size(self) -> int:
        size = 0
        for file in self.files:
            size += file.size
        for directory in self.directories:
            size += directory.get_size()

        return size

    def find_child_directory(self, directory):

        # Check children
        for dir in self.directories:
            if dir.name == directory:
                return dir

        return None

    def contains_file(self, filename: str) -> bool:
        for file in self.files:
            if file.name == filename:
                return True

        return False

    def get_tree_folders(self, directories = []) -> list:
        dirs = directories
        dirs.append(self)
        for dir in self.directories:
            dir.get_tree_folders(dirs)

        return dirs

with open("input.txt") as file:
    commands = file.readlines()

home_directory = None
current_directory = None
for command in commands:
    # Remove newlines
    command = command.split("\n")[0]

    # If there's a cd
    if command.startswith("$ cd"):
        dir_name = command.split()[2]

        # If this is a new home directory
        if dir_name == "/" and home_directory is None:
            home_directory = Directory(dir_name)
            current_directory = home_directory
        elif dir_name == "..":
            current_directory = current_directory.parent
        else:
            # If this is a new sub directory
            target_dir = current_directory.find_child_directory(dir_name)
            if target_dir is None:
                new_dir = Directory(dir_name, current_directory)
                current_directory.add_sub_directory(new_dir)
            else:
                new_dir = target_dir

            # Change the current directory key to the new folder
            current_directory = new_dir

    # If this line has contents of the current directory
    elif not command.startswith("$"):

        # Add this to the list of files found in this folder.
        file_data = command.split()

        # Skip directories
        if file_data[0] == "dir":
            continue

        filename = file_data[1]
        file_size = int(file_data[0])

        # Don't re-add a file
        if current_directory.contains_file(filename):
            continue

        file = File(filename, file_size)
        current_directory.add_file(file)

sum = 0
total_disk_space = 70000000
required_disk_space = 30000000
folders = home_directory.get_tree_folders()

remaining_disk_space = total_disk_space - folders[0].get_size()
space_to_clear = required_disk_space - remaining_disk_space

folders = filter(lambda x: x.get_size() >= space_to_clear, folders)
folders = sorted(folders, key=lambda x: x.get_size())


print(folders[0].get_size())
print(folders[-1].get_size())