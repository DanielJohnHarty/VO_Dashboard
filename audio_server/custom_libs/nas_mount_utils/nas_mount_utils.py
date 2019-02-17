from pathlib import PureWindowsPath, PurePosixPath
import os

GLOBAL_NAS_REPOSITORY_ROOT = os.environ['GLOBAL_NAS_REPOSITORY_ROOT']
SERVER_PATH_TO_AUDIO_REPO = os.environ['SERVER_PATH_TO_AUDIO_REPO']



def convert_global_nas_path_to_server_repo_path(global_nas_path:str)->str:

    global_path_parts = PureWindowsPath(global_nas_path).parts
    
    global_nas_root_split_index = global_path_parts.index(GLOBAL_NAS_REPOSITORY_ROOT) + 1
    
    server_repo_parts = global_path_parts[global_nas_root_split_index:]

    return os.path.join(SERVER_PATH_TO_AUDIO_REPO, *server_repo_parts)


def return_server_filepath_if_exists(global_nas_path:str):
    
    server_filepath = None
    try:
        theoretic_server_filepath = \
                convert_global_nas_path_to_server_repo_path(global_nas_path)
        if os.path.exists(theoretic_server_filepath):
            server_filepath = theoretic_server_filepath
    except Exception as e:
        print(e)
        server_filepath = None

    return server_filepath

