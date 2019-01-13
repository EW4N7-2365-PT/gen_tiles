import subprocess
import sys

from utils import minus


class GPKG:

    def __init__(self, bbox, conf):
        self.conf = conf
        self.layers = conf['layers']

    @classmethod
    def execute(cls, *args):
        ret = subprocess.Popen(args).wait()
        if ret != 0:
            print('{} {} exited with {}'.format(minus, args[0], ret))
            sys.exit(-1)

    def get_initial_gpkg_from_postgis(self, user, password, host, port, dbname):
        pg_coon = "host={} port={} dbname={} user={} password={}"

    def apply_layer(self, layername):
        pass

    def generate_layers(self):
        pass

    def squash_layers(self):
        pass

    def make_gpkg(self):
        pass
