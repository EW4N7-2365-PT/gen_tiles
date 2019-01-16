import os
from utils import execute
from constants import TMP_DIR


def fetch_openstreetmap_carto_styles():
        execute('git', 'clone', 'https://github.com/gravitystorm/openstreetmap-carto',
                '{}osm_carto'.format(TMP_DIR), '--depth', '1')


def compile_osm_styles():
    if not os.path.isdir(os.path.join(TMP_DIR, 'osm_carto')):
        fetch_openstreetmap_carto_styles()
    execute('carto', 'tmp/osm_carto/project.mml', '>', 'tmp/osm_carto/osm.xml')
