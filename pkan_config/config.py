import os
from os.path import exists
from pathlib import Path

from dynaconf import Dynaconf
from zope import component

from pkan_config.exceptions import ConfigFileNotFound
from pkan_config.interfaces import ICfg

FILES = [
    'solr.yaml',
    'rdfstore.yaml',
    'iso2dcat.yaml',
    'flask.yaml',
    'plone.yaml',
    'settings.yaml',
    '.secrets.yaml',
    'shacl.yaml'
]

# user_path = Path('/etc/pkan')

PLONE_DIR = 'plone_harvester'

def load_user_path():
    default_dir = Path(os.path.abspath(__file__)).parent.parent
    paths_file = default_dir / 'paths' / 'paths.yaml'
    if not exists(paths_file):
        raise ConfigFileNotFound(f'Please create paths-File {paths_file}')
    cfg = Dynaconf(
        envvar_prefix='DYNACONF',
        settings_files=[paths_file],
        environments=True,
    )
    return cfg
def load_config(files, directory=None, env=None):
    if env is None:
        env = 'Production'

    user_path = Path(load_user_path().CONFIG_DIR)

    load_files = []

    if directory:
        default_dir = Path(os.path.abspath(__file__)).parent.parent
        default_dir = default_dir / 'templates' / directory
        etc_dir = user_path / directory
    else:
        default_dir = Path(os.path.abspath(__file__)).parent.parent
        default_dir = default_dir / 'templates'
        etc_dir = user_path

    for file in files:
        if exists(etc_dir / file):
            load_files.append(etc_dir / file)
        elif exists(default_dir/file):
            load_files.append(default_dir / file)
        else:
            raise ConfigFileNotFound(file)

    cfg = Dynaconf(
        envvar_prefix='DYNACONF',  # replaced "DYNACONF" by 'DYNACONF'
        settings_files=load_files,
        environments=True,
        env=env,
    )

    return cfg


def get_plone_harvester_config_by_name(file):
    return load_config([file], directory=PLONE_DIR)


def get_config():
    comp = component.queryUtility(ICfg)
    # todo: this is not nice, but working with plone_harvester
    if comp is None:
        register_config()
        comp = component.queryUtility(ICfg)
    return comp


def register_config(env=None):

    cfg = load_config(FILES, directory=None, env=env)

    # `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
    # `settings_files` = Load these files in the order.

    component.provideUtility(cfg, ICfg)

def unregister_config():
    component.provideUtility(None, ICfg)


if __name__ == '__main__':
    register_config('Production')
    cfg = get_config()
    print(cfg)
