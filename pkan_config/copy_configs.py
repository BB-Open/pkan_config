import os
import shutil
from os.path import exists
from pathlib import Path

from pkan_config.config import load_user_path
from pkan_config.exceptions import DirectoryMissing

FRONTEND_FILES = [
    'nuxt_config.js'
]

def copy_frontend_configs():
    cfg = load_user_path()

    # have to copy to nuxt directory cause nuxt can not load from directory outside of project route
    if not exists(cfg.FRONTEND_SRC_DIRECTORY):
        raise DirectoryMissing(
            'Please configure cfg.FRONTEND_SRC_DIRECTORY in paths.yaml '
            'to match the frontend installation directory. The given directory does not exist.')

    target_dir = Path(cfg.FRONTEND_SRC_DIRECTORY) / 'config'
    default_dir = Path(os.path.abspath(__file__)).parent.parent
    default_dir = default_dir / 'templates'

    cfg_dir = Path(cfg.CONFIG_DIR)

    if not exists(target_dir):
        os.mkdir(target_dir)

    for file in FRONTEND_FILES:
        # for overwrites
        if exists(cfg_dir / file):
            shutil.copyfile(cfg_dir / file, target_dir / file)
        # for defaults
        else:
            shutil.copyfile(default_dir / file, target_dir / file)

if __name__ == '__main__':
    copy_frontend_configs()