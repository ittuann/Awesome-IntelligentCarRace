# -*- coding: utf-8 -*-
"""This module contains the configuration info.

Note:
    File   : config.py
    Author : Baiqi.Lu <ittuann@outlook.com>
    License: MIT License.
"""

from pathlib import Path


class Config:
    """This class contains the configuration info."""

    def __init__(self) -> None:
        """Initialize the configuration info with default paths."""
        # 项目跟绝对路径
        self.PROJECT_PATH: Path = Path(__file__).parents[1].resolve()

        # 其他路径
        self.DOCS_PATH: Path = self.PROJECT_PATH / "docs"
        self.SITE_PATH: Path = self.PROJECT_PATH / "site"
        self.TABLE_PATH: Path = self.PROJECT_PATH / "table.csv"
        self.TABLE_URL_PATH: Path = self.PROJECT_PATH / "table-url.csv"

    def update_site_path(self, new_path: Path) -> None:
        """Update the site path."""
        self.SITE_PATH = self.SITE_PATH / new_path


# 实例化配置类
cfg = Config()
