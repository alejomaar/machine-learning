from pyprojroot import here
from pathlib import Path

def get_paths():  
    DIR = [['data','final'],
           ['data','processed'],
           ['data','raw'],
           ['data','final','img'],
           ['documentation'],
           ['models']
          ]
    KEYS = list(map(lambda dir:'_'.join(dir),DIR))
    return {key:here().joinpath(*dir) for key,dir in zip(KEYS,DIR)}

def create_folder(folder:str):
    """Create a folder or nested folder given the path

    Parameters
    ----------
    folder : str
        Path to create folder
    """
    try:
        Path(folder).mkdir(parents=True, exist_ok=True)
    except OSError as e:
        print(f"Error: {e.strerror}")

PATHS = get_paths()
