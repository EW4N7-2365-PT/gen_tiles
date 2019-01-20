from __future__ import print_function
import os
import shutil
import sys
import hashlib
from datetime import datetime

import click

from checks import run_checks
from generate_tiles import render_tiles
from utils import plus, execute, minus
from gpkg import make_gpkg_from_tiles, make_initial_gpkg
import bbox_cities
from settings import TMP_DIR, BUILD_DIR, TILES_DIR, STYLES_DIR
from generate_mapnik_mapfile import compile_osm_styles


@click.command('Generate tiles')
@click.option('--min-zoom', default=1)
@click.option('--max-zoom', default=3)
@click.option('--bbox-code', required=True)
@click.option('--quality', default=85)
@click.option('--only-tiles', is_flag=True, default=False)
def run(min_zoom, max_zoom, bbox_code, quality, only_tiles):
    bbox_code = bbox_code.upper()
    if not hasattr(bbox_cities, bbox_code):
        print('{} bbox code not found in bbox_cities.py'.format(minus))
        sys.exit(-1)

    run_checks()

    if not os.path.isdir(TMP_DIR):
        os.mkdir(TMP_DIR)
    if not os.path.isdir(BUILD_DIR):
        os.mkdir(BUILD_DIR)

    compile_osm_styles(getattr(bbox_cities, bbox_code), min_zoom, max_zoom)

    filename = hashlib.md5('{}{}{}{}{}'.format(bbox_code, min_zoom, max_zoom, quality, datetime.now())).hexdigest()

    if not only_tiles:
        make_initial_gpkg()

    render_tiles(getattr(bbox_cities, bbox_code), '{}/osm.xml'.format(STYLES_DIR), TILES_DIR, min_zoom,
                 max_zoom,
                 tms_scheme=True)
    print('{} tiles created'.format(plus))

    make_gpkg_from_tiles(quality, filename)

    if not only_tiles:
        execute('ogr2ogr', '-f', 'GPKG', 'tmp/out.{}.gpkg'.format(filename), 'tmp/initial.gpkg', '-update', '-progress')

    shutil.copy('tmp/out.{}.gpkg'.format(filename), BUILD_DIR)
    print('{} Final gpkg moved to build dir'.format(plus))

    # shutil.rmtree(TMP_DIR)
    # print('{} tmp dir deleted'.format(plus))


if __name__ == '__main__':
    run()
