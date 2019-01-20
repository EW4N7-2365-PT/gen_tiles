from __future__ import print_function
import sys
from subprocess import Popen, PIPE

from utils import plus, minus


def run_checks():
    [c() for name, c in globals().items() if callable(c) and name.startswith('check')]


def get_version_or_exit(program, version):
    try:
        return Popen([program, version], stdout=PIPE).communicate()[0].replace('\n', '')
    except (OSError, IndexError):
        print('{} install {}'.format(minus, program))
        sys.exit(-1)


def check_mapnik_config():
    try:
        import mapnik
        print('{} mapnik {} installed'.format(plus, mapnik.mapnik_version()))
    except ImportError:
        print('{} install mapnik'.format(minus))
        sys.exit(-1)


def check_gdal_version():
    gdal = get_version_or_exit('gdalinfo', '--version')
    print("{} {} installed".format(plus, gdal))


def check_carto():
    carto = get_version_or_exit('carto', '--version')
    print("{} carto {} installed".format(plus, carto))


def check_git():
    git = get_version_or_exit('git', '--version')
    print("{} {} installed".format(plus, git))


def check_node():
    node = get_version_or_exit('node', '--version')
    print("{} node {} installed".format(plus, node))


if __name__ == "__main__":
    run_checks()
