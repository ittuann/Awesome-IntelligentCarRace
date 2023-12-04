# -*- coding: utf-8 -*-

"""
File   : split.py
Author : Baiqi.Lu <ittuann@outlook.com>
License: MIT License

This module provides functionalities to split a table based on the award filter column.

Main Change Logs:
Date          Author                            Notes
2023-09-22    Baiqi.Lu <ittuann@outlook.com>    Create file
"""

import sys
from pathlib import Path
import pandas as pd


def awardSort(awards):
    """
    根据指定的顺序对奖项进行排序。
    :param awards: 包含奖项名称的系列。
    :return: 根据奖项优先级的排序值的系列。
    """
    awardOrder = ["国家级一等奖", "国家级二等奖", "国家级三等奖", "省级一等奖", "省级二等奖", "省级三等奖"]
    return awards.map(
        lambda award: (0, awardOrder.index(award))
        if award in awardOrder
        else (1, award)
    )


def URLModification(inputFile=None, outputFile=None):
    """
    修饰主表的URL链接
    :param inputFile: 输入的 CSV 文件路径。默认为 None ，将使用路径"./table.csv"。
    :param outputFile: 输出的 CSV 文件路径。默认为 None ，将使用路径"./table-url.csv"。
    """
    if inputFile is None:
        inputFile = Path("./table.csv")
    if outputFile is None:
        outputFile = Path("./table-url.csv")

    if not inputFile.exists():
        raise ValueError(f"The specified {inputFile} does not exist.")

    df = pd.read_csv(inputFile, encoding="utf-8")
    df["链接"] = "<" + df["链接"] + '>{:target="_blank"}'
    df.to_csv(outputFile, index=False, encoding="utf-8")
    print(f"Successfully generate url modification table {outputFile}")


def splitTable(filtration, outputDir, inputFile=None):
    """
    根据给定的过滤列将主表拆分，并保存到输出目录。
    :param filtration: 过滤的列名称。
    :param outputDir: 输出目录路径。
    :param inputFile: 输入的 CSV 文件路径。默认为 None ，将使用路径"./table-url.csv"
    """
    if inputFile is None:
        inputFile = Path("./table-url.csv")

    if not inputFile.exists():
        raise ValueError(f"The specified input file {inputFile} does not exist.")
    if not outputDir.exists():
        raise ValueError(f"The specified output directory {outputDir} does not exist.")

    df = pd.read_csv(inputFile, encoding="utf-8")
    if filtration not in df.columns:
        raise ValueError(
            f"The specified filtration {filtration} is not a column of the table."
        )
    grouped = df.groupby(filtration)

    for filtrate, group in grouped:
        sorted_group = group.sort_values(by="获奖", key=awardSort, ascending=True)
        filename = Path(outputDir) / f"{filtrate}.csv"
        sorted_group.to_csv(filename, index=False, encoding="utf-8")
        print(f"Successfully generate sub-table {filtrate}.csv")


if __name__ == "__main__":
    sys.path.append(str(Path.cwd()))

    URLModification()

    splitTable("年份", Path(".") / "docs" / "year")
    splitTable("组别", Path(".") / "docs" / "group")
    splitTable("获奖", Path(".") / "docs" / "award")

