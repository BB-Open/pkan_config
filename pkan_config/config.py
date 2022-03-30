import os
from os.path import exists
from pathlib import Path

import zope
from dynaconf import Dynaconf
from zope import component

from pkan_config.exceptions import ConfigFileNotFound
from pkan_config.interfaces import ICfg

FILES = ['solr.yaml', 'rdfstore.yaml', 'iso2dcat.yaml', 'flask.yaml', 'plone.yaml', 'settings.yaml', '.secrets.yaml']

ETC_PATH = Path('/etc/pkan')

def get_config():
    comp = component.queryUtility(ICfg)
    # todo: this is not nice, but working with plone
    if comp is None:
        register_config()
        comp = component.queryUtility(ICfg)
    return comp

def register_config(env=None):

    if env is None:
        env='Production'

    load_files = []

    default_dir = Path(os.path.abspath(__file__)).parent.parent / 'templates'

    for file in FILES:
        if exists(ETC_PATH / file):
            load_files.append(ETC_PATH/file)
        elif exists(default_dir/file):
            load_files.append(default_dir/file)
        else:
            raise ConfigFileNotFound(file)

    cfg = Dynaconf(
        envvar_prefix='DYNACONF',  # replaced "DYNACONF" by 'DYNACONF'
        settings_files=load_files,
        environments=True,
        env=env,
    )

    # `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
    # `settings_files` = Load these files in the order.

    component.provideUtility(cfg, ICfg)

if __name__ == '__main__':
    register_config('Production')
