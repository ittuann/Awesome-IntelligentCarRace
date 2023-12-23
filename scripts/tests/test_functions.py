# -*- coding: utf-8 -*-

"""Code Coverage Test.

Note:
    File   : test_functions.py
    Author : Baiqi.Lu <ittuann@outlook.com>
    License: MIT License.
"""

from pathlib import Path

import pandas as pd
import pytest
from build import build_docs, update_404page_title
from config import Config, cfg
from split import awardSort, splitTable, urlModification


def test_awardSort():
    """Test case for the awardSort function."""
    awards = pd.Series(["国家级一等奖", "省级三等奖", "国家级二等奖"])
    sorted_awards = awardSort(awards)
    expected = pd.Series([(0, 0), (0, 5), (0, 1)])
    pd.testing.assert_series_equal(sorted_awards, expected)


def test_urlModification_success():
    """Test case for the URLModification function with successful execution."""
    output_file = cfg.DOCS_PATH / "test_output.csv"

    urlModification(outputFile=output_file)

    df_output = pd.read_csv(output_file)
    for url in df_output["链接"]:
        assert url.startswith("<") and url.endswith('>{:target="_blank"}'), f"URL {url} is not modified"
    output_file.unlink()


def test_urlModification_fail():
    """Test case for the URLModification function with failure."""
    with pytest.raises(ValueError):
        urlModification(Path("non_existent.csv"))


def test_splitTable_success():
    """Test case for the splitTable function with successful execution."""
    # 读取输入文件以确定预期年份
    df_input = pd.read_csv(cfg.TABLE_PATH)

    for column_header in ["年份", "组别", "获奖"]:
        expected_categories = sorted(set(df_input[column_header].astype(str)))
        expected_columns = list(df_input.columns)

        splitTable(column_header, Path(__file__).parent)

        for category in expected_categories:
            output_file = Path(__file__).parent / f"{category}.csv"
            # 验证文件成功生成
            assert output_file.exists(), f"Output file {output_file} not found"
            # 验证每个输出文件内容
            df_output = pd.read_csv(output_file)
            assert list(df_output.columns) == expected_columns, f"Columns in {output_file} do not match"
            assert all(
                df_output[column_header].astype(str) == category
            ), f"Category {category} not found in {output_file}"
            output_file.unlink()


def test_splitTable_fail():
    """Test case for the splitTable function with failure."""
    with pytest.raises(ValueError):
        splitTable("获奖", Path(__file__).parent, Path("non_existent.csv"))
    with pytest.raises(ValueError):
        splitTable("获奖", Path("non_existent_dir"), cfg.TABLE_PATH)
    with pytest.raises(ValueError):
        splitTable("不存在的列标题", Path(__file__).parent, cfg.TABLE_PATH)


def test_config_initialization():
    """Test case for the initialization of the Config class."""
    cfg_test = Config()
    assert cfg_test.PROJECT_PATH.is_dir(), "PROJECT_PATH should be a directory"
    assert cfg_test.TABLE_PATH.is_file(), "TABLE_PATH should be a file"


def test_config_update_site_path():
    """Test case for the update_site_path function."""
    cfg_test = Config()
    old_path = cfg_test.SITE_PATH
    cfg_test.update_site_path(Path("new_site"))
    assert old_path / "new_site" == cfg_test.SITE_PATH, "SITE_PATH should be updated to new path"


def test_build_docs():
    """Test case for the build_docs function."""
    build_docs()

    assert cfg.SITE_PATH.exists(), "cfg.SITE_PATH should be created"

    for config_file in cfg.DOCS_PATH.glob("mkdocs.*.yml"):
        language_code = config_file.stem.split(".")[1]
        expected_dir = cfg.SITE_PATH / language_code
        # 验证对应的文件夹是否存在
        assert expected_dir.exists(), f"Expected directory for {language_code} does not exist"


def test_update_404page_title():
    """Test case for the test_update_404page_title function. Need run build_docs() first."""
    test_file_path = cfg.SITE_PATH / "404.html"
    update_404page_title()

    with open(test_file_path, encoding="utf-8") as file:
        updated_content = file.read()

    assert "<title>Awesome Intelligent Car Race - 404 Page Not Found</title>" in updated_content, "New title not found"
    assert "<title>Awesome-IntelligentCarRace</title>" not in updated_content, "Old title should be removed"


def test_update_404page_title_fail():
    """Test case for the test_update_404page_title function with failure."""
    update_404page_title()
    with pytest.raises(FileNotFoundError):
        update_404page_title(Path("non_existent_dir"))
