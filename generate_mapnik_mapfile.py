from __future__ import absolute_import
import os
from jinja2 import Environment, FileSystemLoader

from utils import execute, plus
import settings
from utils import execute


def fetched_recently(timedelta=30):
    pass


def fetch_openstreetmap_carto_styles():
    execute('git', 'clone', 'https://github.com/gravitystorm/openstreetmap-carto',
            'styles', '--depth', '1')
    execute('python', '{}/scripts/get-shapefiles.py'.format(settings.STYLES_DIR))


def compile_osm_styles(bbox, min_zoom, max_zoom):
    if not os.path.exists(settings.STYLES_DIR):
        print('{} Setting up styles'.format(plus))
        fetch_openstreetmap_carto_styles()

    with open('{}/project.mml'.format(settings.STYLES_DIR), 'w+') as prj:
        j2_env = Environment(loader=FileSystemLoader(settings.TEMPLATES_DIR), trim_blocks=True)
        template = j2_env.get_template('project.mml')
        prj.write(template.render(PG=settings.PG, bbox=bbox, min_zoom=min_zoom, max_zoom=max_zoom))

    print('{} compiling osm carto styles --------> mapnik mapfile xml'.format(plus))
    execute('carto', '{}/project.mml'.format(settings.STYLES_DIR), '-q', '-f', '{}/osm.xml'.format(settings.STYLES_DIR))
