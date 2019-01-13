from __future__ import print_function
from utils import plus, minus
import sys
from subprocess import Popen, PIPE


def run_checks():
    [c() for name, c in globals().items() if callable(c) and name.startswith('check')]


def check_mapnik_config():
    try:
        import mapnik
        if hasattr(mapnik, 'mapnik_version'):
            print('{} mapnik {} installed'.format(plus, mapnik.mapnik_version()))
    except ImportError:
        print('{} install mapnik'.format(minus))
        sys.exit(-1)


def check_gdal_version():
    pipe = Popen(['gdalinfo', '--version'], stdout=PIPE)
    text = None
    try:

        text = pipe.communicate()[0].split(' ')[1][:-1]
    except IndexError:
        print('{} Install GDAL'.format(minus))
    if pipe.returncode == 0 and text:
        print('{} GDAL {} installed'.format(plus, text))
