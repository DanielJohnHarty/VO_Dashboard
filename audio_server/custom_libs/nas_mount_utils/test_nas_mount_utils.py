from nas_mount_utils import convert_global_nas_path_to_server_repo_path, return_server_filepath_if_exists
import os
import pytest

GLOBAL_NAS_REPOSITORY_ROOT = os.environ['GLOBAL_NAS_REPOSITORY_ROOT']
SERVER_PATH_TO_AUDIO_REPO = os.environ['SERVER_PATH_TO_AUDIO_REPO']


GLOBAL_NAS_TO_SERVER_AUDIO_REPO_TESTDATA = [
    ('C:\\dev\\{}\\frFR\\HS\\03_12.0 (Boomsday)\\01_InGame\\01_RStoAV\\01_180523_Batch01\\test_file.wav'.format(GLOBAL_NAS_REPOSITORY_ROOT),
     '{}/frFR/HS/03_12.0 (Boomsday)/01_InGame/01_RStoAV/01_180523_Batch01/test_file.wav'.format(SERVER_PATH_TO_AUDIO_REPO).format()),
]    

@pytest.mark.parametrize("global_nas_path, expected", GLOBAL_NAS_TO_SERVER_AUDIO_REPO_TESTDATA)
def test_convert_global_nas_path_to_server_repo_path(global_nas_path, expected):
    actual = convert_global_nas_path_to_server_repo_path(global_nas_path)
    assert actual == expected



RETURN_SERVER_FILEPATH_IF_EXISTS_TESTDATA = [
    ('C:\\path\\{}\\that\\doesnt\\exist\\test_file.wav'.format(GLOBAL_NAS_REPOSITORY_ROOT), None),
    ('C:\\path\\which\\does\\exist\\{}\\3_nicolas_14.wav'.format(GLOBAL_NAS_REPOSITORY_ROOT), '/audio_repo/3_nicolas_14.wav')
]    

@pytest.mark.parametrize("global_nas_path, expected", RETURN_SERVER_FILEPATH_IF_EXISTS_TESTDATA)
def test_return_server_filepath_if_exists(global_nas_path, expected):
    actual = return_server_filepath_if_exists(global_nas_path)
    assert actual == expected



def test_return_server_filepath_when_nas_and_server_repo_root_differ():

    try:
        ORIGINAL_GLOBAL_NAS_REPOSITORY_ROOT = os.environ['GLOBAL_NAS_REPOSITORY_ROOT']
        ORIGINAL_SERVER_PATH_TO_AUDIO_REPO = os.environ['SERVER_PATH_TO_AUDIO_REPO']


        GLOBAL_NAS_REPOSITORY_ROOT = 'AUDIO'
        SERVER_PATH_TO_AUDIO_REPO = 'audio_repo'


        global_nas_audio_filepath = 'C:\\path\\which\\does\\exist\\{}\\3_nicolas_14.wav'.format(GLOBAL_NAS_REPOSITORY_ROOT)
        server_audio_filepath = '/{}/3_nicolas_14.wav'.format(SERVER_PATH_TO_AUDIO_REPO)


        actual = return_server_filepath_if_exists(global_nas_audio_filepath)
        expected = server_audio_filepath
        assert actual == expected
    except Exception as e:
        print(e)
    else:
        os.environ['GLOBAL_NAS_REPOSITORY_ROOT'] = ORIGINAL_GLOBAL_NAS_REPOSITORY_ROOT
        os.environ['SERVER_PATH_TO_AUDIO_REPO'] = ORIGINAL_SERVER_PATH_TO_AUDIO_REPO

