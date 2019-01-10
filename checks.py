def check_mapnik_config():
    pass


def run_checks():
    [c() for name, c in globals().items() if callable(c) and name.startswith('check')]


