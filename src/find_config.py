
"""find_config.py: finds config file or prints informative message if not"""

__author__ = "ejd"
__credits__ = ["ejd","borrowing from Brody Lab and datajoint documentation"]
__maintainer__ = "ejd"
__email__ = "dennise@hhmi.org"
__license__ = "MIT"
__status__ = "Development"

import os
import pathlib

def chdir_to_root():
    """looks for the dj config file in this directory,
    and in root directory"""
    # borrowed from Brody Lab
    root_dir_found = 0
    conf_file_found = 0
    while 1:
        current_dir = os.getcwd()
        if os.path.isdir(lab_dir):
            root_dir_found = 1
            if os.path.isfile(pathlib.Path(current_dir,'dj_local_conf.json')):
                conf_file_found = 1
        if root_dir_found:
            break
        os.chdir('..')
        new_current_dir = os.getcwd()
        if str(current_dir) == str(new_current_dir):
            break

    return root_dir_found, conf_file_found


def try_find_conf_file():
    """prints an informative message as it looks for the dj config file"""
    # borrowed from Brody Lab

    root_dir_found, conf_file_found = chdir_to_root()
    if root_dir_found and conf_file_found:
        print('Local configuration file found !! no need to run the configuration (unless configuration has changed)')
    elif root_dir_found:
        print('Local configuration file not found. Ignore this if you have a global config. Run configuration notebook otherwise')
    else:
        print('Root dir not found, change this notebook to the project folder')
