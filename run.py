from __future__ import print_function

import os
import shutil
from datetime import datetime
import sys
from argparse import Namespace

import click

from checks import run_checks
from generate_tiles import render_tiles
from utils import plus, execute, minus
from tiles2gpkg import main
import bbox_cities

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TMP_DIR = os.path.join(BASE_DIR, 'tmp/')
TILES_DIR = os.path.join(TMP_DIR, 'tiles/')
BUILD_DIR = os.path.join(BASE_DIR, 'build/')


@click.command('Generate tiles')
@click.option('--min-zoom', default=1)
@click.option('--max-zoom', default=3)
@click.option('--bbox-code', required=True)
@click.option('--no-cleanup', is_flag=True, default=False)
def run(min_zoom, max_zoom, bbox_code, no_cleanup):
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
    render_tiles(getattr(bbox_cities, bbox_code), os.path.join(BASE_DIR) + '/test_mapnik_mapfile.xml', TILES_DIR,
                 min_zoom, max_zoom,
                 tms_scheme=True)
    print('{} tiles created'.format(plus))
    nmscp = Namespace(append=False, imagery='png', nsg_profile=False,
                      output_file='{}out.{}.gpkg'.format(TMP_DIR, today),
                      q=75,
                      renumber=False, source_folder='tmp/tiles', srs=3857, table_name='appended1', threading=True,
                      tileorigin='ll')

    main(nmscp)
    print('{} Layer generated'.format(plus))
    execute('ogr2ogr', '-f', 'GPKG', 'tmp/out.{}.gpkg'.format(today), 'tmp/out.gpkg', '-update', '-append')
    shutil.copy('tmp/out.{}.gpkg'.format(today), BUILD_DIR)
    print('{} Final gpkg moved to build dir'.format(plus))
    if not no_cleanup:
        shutil.rmtree(TMP_DIR)
    print('{} tmp dir deleted'.format(plus))


if __name__ == '__main__':
    run()
