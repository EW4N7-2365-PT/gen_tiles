import os

TARGET_MAP_EPSG = 3857  # Google
INITIAL_GDPKG_FILENAME = 'out.gpkg'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TMP_DIR = os.path.join(BASE_DIR, 'tmp/')
TILES_DIR = os.path.join(TMP_DIR, 'tiles/')
BUILD_DIR = os.path.join(BASE_DIR, 'build/')
STYLES_DIR = os.path.join(BASE_DIR, 'styles')
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

PG = {
    'database': 'test_style',
    'username': 'postgres',
    'password': '12345',
    'host': 'localhost',
    'port': '5432'
}
