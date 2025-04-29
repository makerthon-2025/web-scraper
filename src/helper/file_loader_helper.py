import os

def router_loader():
    """
    This function loads all the Python files in the specified folder.
    """
    # Specify the folder path where the Python files are located
    folder_path = 'src/router'

    # List all Python files in the specified folder
    py_files = [f for f in os.listdir(folder_path) if f.endswith('.py')]

    return py_files