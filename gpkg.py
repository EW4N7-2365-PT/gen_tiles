import shutil
from datetime import datetime

from tiles2gpkg import main
from utils import execute, plus
from argparse import Namespace
from constants import TMP_DIR, BUILD_DIR


def make_initial_gpkg(conf):
    pass


def merge_layers():
    pass


def make_gpkg_from_tiles(quality, today):
    nmspc = Namespace(append=False, imagery='png', nsg_profile=False,
                      output_file='{}out.{}.gpkg'.format(TMP_DIR, today),
                      q=quality,
                      renumber=False, source_folder='tmp/tiles', srs=3857, table_name='appended1', threading=True,
                      tileorigin='ll')
    main(nmspc)
    execute('ogr2ogr', '-f', 'GPKG', 'tmp/out.{}.gpkg'.format(today), 'tmp/out.gpkg', '-update', '-append')

    shutil.copy('tmp/out.{}.gpkg'.format(today), BUILD_DIR)
    print('{} Final gpkg moved to build dir'.format(plus))
