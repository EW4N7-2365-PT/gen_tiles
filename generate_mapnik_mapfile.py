import os
from utils import execute
from constants import TMP_DIR


def fetch_openstreetmap_carto_styles():
    if not os.path.isdir(os.path.join(TMP_DIR, 'osm_carto')):
        execute('git', 'clone', 'https://github.com/gravitystorm/openstreetmap-carto',
                '{}osm_carto'.format(TMP_DIR), '--depth', '1')


def compile_osm_styles():
    pass
