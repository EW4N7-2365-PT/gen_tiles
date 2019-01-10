import os

import click
from checks import run_checks
from generate_tiles import render_tiles


BASE_DIR = os.path.basename(__file__)

def get_tile_dir():
    return os.path.join(BASE_DIR,'tiles')


@click.command('Generate tiles')
@click.option('--min-zoom', default=0)
@click.option('--max-zoom', default=18)
@click.argument('mapfile')
def run(min_zoom, max_zoom, mapfile):
    run_checks()
    bbox = (1.0, 10.0, 20.6, 50.0)
    render_tiles(bbox, mapfile, '', min_zoom, max_zoom, "Europe+")


if __name__ == '__main__':
    # run()
