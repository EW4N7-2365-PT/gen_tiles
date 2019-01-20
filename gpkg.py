from argparse import Namespace

from tiles2gpkg import make_gpkg
from utils import execute, plus
from settings import TMP_DIR


def merge_layers():
    pass


def make_initial_gpkg():
    execute('ogr2ogr', '-f', 'GPKG', 'tmp/initial.gpkg',
            'PG:user=postgres password=12345 dbname=test_style tables=planet_osm_roads')
    print('{} Initial dpkg created'.format(plus))


def make_gpkg_from_tiles(quality, filename):
    nmspc = Namespace(append=True,
                      imagery='png',
                      nsg_profile=False,
                      output_file='{}out.{}.gpkg'.format(TMP_DIR, filename),
                      q=quality,
                      renumber=False,
                      source_folder='tmp/tiles',
                      srs=3857, table_name='osm_tiles',
                      threading=True,
                      tileorigin='ll')
    make_gpkg(nmspc)
