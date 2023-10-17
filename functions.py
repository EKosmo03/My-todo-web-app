import zipfile
import pathlib
FILEPATH = "venv/Scripts/todos.txt"

def get_todos(filepath=FILEPATH):

    """reads a text file and returns the
    list of to-do list items
    """

    with open(filepath, "r") as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_argument, filepath=FILEPATH):
    """Write the to-do items list in the text file."""
    with open(filepath, "w") as file:
        file.writelines(todos_argument)

def make_archive(filepaths, destination_directory):
    dest_path = pathlib.Path(destination_directory, "compressed.zip")
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths:
            archive.write(filepath)

def extract_archive(archivepath, dest_dir):
    with zipfile.ZipFile(archivepath, 'r') as archive:
        archive.extractall(dest_dir)