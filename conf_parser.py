import json


# TODO
def get_config():
    return {
        'PG_CONF': {
            'username': 'postgres',
            'password': '12345',
            'host': 'localhost',
            'port': '5432',
            'tables': ['osm_planet_roads', ]
        }
    }
