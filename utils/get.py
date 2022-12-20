import os

import requests
import lxml.etree as etree
from .utils import fprint
import pandas as pd


def get_inside_files_from_url(url: str) -> list:
    data = requests.get('https://darsbazi.com/wp-content/themes/bazimooz/games/')
    fprint("\tData DOWNLOADED SUCCESSFULLY")
    return [data.content]
