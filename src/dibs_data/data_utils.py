import os


def get_data_path() -> str:
    current_file_path = os.path.abspath(__file__)
    data_folder = os.path.join(os.path.dirname(current_file_path), "data")
    return data_folder
