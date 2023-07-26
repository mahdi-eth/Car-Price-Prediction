import sys
from os.path import abspath, dirname, join

app_path = abspath(join(dirname(__file__), 'App'))
sys.path.insert(0, app_path)

from app import app
from flask_frozen import Freezer

freezer = Freezer(app)

if __name__ == "__main__":
    freezer.freeze()
