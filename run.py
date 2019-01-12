from __future__ import print_function

import os

import click
from checks import run_checks
from generate_tiles import render_tiles
from utils import plus
import subprocess

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TILES_DIR = os.path.join(BASE_DIR, 'tiles/')
TMP_DIR = os.path.join(BASE_DIR, '.tmp/')


@click.command('Generate tiles')
@click.option('--min-zoom', default=1)
@click.option('--max-zoom', default=10)
def run(min_zoom, max_zoom):
    run_checks()
    bbox = (19.848546, 50.000802, 20.062178, 50.100336)
    render_tiles(bbox, '/home/kamil/Downloads/main.xml', TILES_DIR, min_zoom, max_zoom)


if __name__ == '__main__':
    if not os.path.isdir(TMP_DIR):
        os.mkdir(TMP_DIR)

    ret = subprocess.Popen(
        ['ogr2ogr', '-f', 'GPKG', 'out.gpkg',
         'PG:user=\'postgres\' password=\'12345\' dbname=\'test1\' tables=planet_osm_roads']).wait()
    print('{} Initial dpkg created'.format(plus))
    print(ret)
    run()
