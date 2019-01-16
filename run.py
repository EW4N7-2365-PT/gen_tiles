from __future__ import print_function

import os
import shutil
from datetime import datetime
import sys

import click

from checks import run_checks
from generate_tiles import render_tiles
from utils import plus, execute, minus
from gpkg import make_gpkg_from_tiles
import bbox_cities
from constants import TMP_DIR, BUILD_DIR, TILES_DIR


@click.command('Generate tiles')
@click.option('--min-zoom', default=1)
@click.option('--max-zoom', default=3)
@click.option('--bbox-code', required=True)
@click.option('--no-cleanup', is_flag=True, default=False)
@click.option('--quality', default=75)
def run(min_zoom, max_zoom, bbox_code, no_cleanup, quality):
    if not hasattr(bbox_cities, bbox_code.upper()):
        print('{} bbox code not found in bbox_cities.py'.format(minus))
        sys.exit(-1)

    run_checks()

    if not os.path.isdir(TMP_DIR):
        os.mkdir(TMP_DIR)
    if not os.path.isdir(BUILD_DIR):
        os.mkdir(BUILD_DIR)

    execute('ogr2ogr', '-f', 'GPKG', 'tmp/out.gpkg',
            'PG:user=postgres password=12345 dbname=test1 tables=planet_osm_roads')
    print('{} Initial dpkg created'.format(plus))
    today = datetime.today()
    render_tiles(getattr(bbox_cities, bbox_code), '/home/kamil/src/openstreetmap-carto/osm.xml', TILES_DIR, min_zoom,
                 max_zoom,
                 tms_scheme=True)
    print('{} tiles created'.format(plus))

    make_gpkg_from_tiles(quality, today)

    if not no_cleanup:
        shutil.rmtree(TMP_DIR)
        print('{} tmp dir deleted'.format(plus))


if __name__ == '__main__':
    run()
