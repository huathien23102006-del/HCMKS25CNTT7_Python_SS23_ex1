import os

def create_log_dir(dir_name="logs"):
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
        return True
    return False
