from datetime import datetime

from tiles2gpkg import main
from utils import execute
from argparse import Namespace
from constants import TMP_DIR


def make_initial_gpkg(conf):
    pass


def merge_layers():
    pass


def make_gpkg_from_tiles(quality, tiles_format, today):
    nmspc = Namespace(append=False, imagery=tiles_format, nsg_profile=False,
                      output_file='{}out.{}.gpkg'.format(TMP_DIR, today),
                      q=quality,
                      renumber=False, source_folder='tmp/tiles', srs=3857, table_name='appended1', threading=True,
                      tileorigin='ll')
    main(nmspc)
    execute('ogr2ogr', '-f', 'GPKG', 'tmp/out.{}.gpkg'.format(today), 'tmp/out.gpkg', '-update', '-append')
