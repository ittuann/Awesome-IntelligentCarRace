# -*- coding: utf-8 -*-
"""This module contains the configuration info.

Note:
    File   : config.py
    Author : Baiqi.Lu <ittuann@outlook.com>
    License: MIT License.
"""

from pathlib import Path

# Constants
PROJECT_PATH = Path(__file__).parents[1].resolve()
DOCS_PATH = PROJECT_PATH / "docs"
SITE_PATH = PROJECT_PATH / "site"
TABLE_PATH = PROJECT_PATH / "table.csv"
TABLE_URL_PATH = PROJECT_PATH / "table-url.csv"
