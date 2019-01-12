from __future__ import print_function

import os

import click
from checks import run_checks
from generate_tiles import render_tiles
import bbox_cities
from utils import plus,minus

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TILES_DIR = os.path.join(BASE_DIR, 'tiles/')
TMP_MAPNIK_MAPFILE_DIR = os.path.join(BASE_DIR, '.tmp/')


@click.command('Generate tiles')
@click.option('--min-zoom', default=0)
@click.option('--max-zoom', default=12)
def run(min_zoom, max_zoom):
    run_checks()
    bbox = bbox_cities.KRK
    render_tiles(bbox, '/home/kamil/Downloads/main.xml', TILES_DIR, min_zoom, max_zoom, 'Europe')


if __name__ == '__main__':
    print('{} hello'.format(plus))
    run()
