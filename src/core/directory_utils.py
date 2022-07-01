from pathlib import Path

def get_root_folder():
    return str(Path.cwd().parent)

def get_inputs_folder():
    return str(get_root_folder()) + "/inputs"

def get_outputs_folder():
    return str(get_root_folder()) + "/outputs"