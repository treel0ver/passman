import os

def is_path_exists_or_creatable(path):
    if os.path.exists(path):
        return False

    try:
        Path(path).mkdir(parents=True, exist_ok=True)
        return False
    except Exception as e:
        return True