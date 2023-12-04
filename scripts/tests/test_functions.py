# -*- coding: utf-8 -*-

"""
File   : test_functions.py
Author : Baiqi.Lu <ittuann@outlook.com>
License: MIT License

Code Coverage Test

Main Change Logs:
Date          Author                            Notes
2023-12-04    Baiqi.Lu <ittuann@outlook.com>    Create file
"""

from pathlib import Path
import pytest
from split import awardSort, URLModification, splitTable
import pandas as pd


def test_awardSort():
    # 示例测试用例
    awards = pd.Series(["国家级一等奖", "省级三等奖", "国家级二等奖"])
    sorted_awards = awardSort(awards)
    expected = pd.Series([(0, 0), (0, 5), (0, 1)])
    pd.testing.assert_series_equal(sorted_awards, expected)


def test_URLModification_success():
    output_file = Path(__file__).parent / "test_output.csv"

    URLModification(outputFile=output_file)

    df_output = pd.read_csv(output_file)
    for url in df_output["链接"]:
        assert url.startswith("<") and url.endswith('>{:target="_blank"}')
    output_file.unlink()


def test_URLModification_fail():
    with pytest.raises(ValueError):
        URLModification(Path("non_existent.csv"))


def test_splitTable_success():
    # 读取输入文件以确定预期年份
    df_input = pd.read_csv(Path("./table.csv"))
    for column_header in ["年份", "组别", "获奖"]:
        expected_categories = sorted(set(df_input[column_header].astype(str)))

        splitTable(column_header, Path(__file__).parent)

        for category in expected_categories:
            output_file = Path(__file__).parent / f"{category}.csv"
            # 验证文件成功生成
            assert output_file.exists()
            # 验证每个输出文件内容
            df_output = pd.read_csv(output_file)
            expected_columns = ["名称", "链接", "学校", "组别", "获奖", "年份", "备注"]
            assert list(df_output.columns) == expected_columns
            assert all(df_output[column_header].astype(str) == category)
            output_file.unlink()


def test_splitTable_fail():
    with pytest.raises(ValueError):
        splitTable("获奖", Path(__file__).parent, Path("non_existent.csv"))
    with pytest.raises(ValueError):
        splitTable("获奖", Path("non_existent_dir"), Path("./table.csv"))
    with pytest.raises(ValueError):
        splitTable("不存在的列标题", Path(__file__).parent, Path("./table.csv"))
