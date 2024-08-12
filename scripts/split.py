"""Split Scripts.

This module provides functionalities to split a table based on the award filter column.

Note:
    File   : split.py
    Author : Baiqi.Lu <ittuann@outlook.com>
    License: MIT License.

Example:
    $ python ./scripts/split.py
"""

from pathlib import Path

import pandas as pd
from config import cfg


def awardSort(awards: pd.Series) -> pd.Series:
    """奖项排序.

    根据指定的中文顺序对奖项进行排序。

    Args:
        awards (pd.Series): 包含奖项名称的系列

    Returns:
        pd.Series: 排序后的系列
    """
    awardOrder = [
        "国家级一等奖",
        "国家级二等奖",
        "国家级三等奖",
        "省级一等奖",
        "省级二等奖",
        "省级三等奖",
    ]
    return awards.map(lambda award: (0, awardOrder.index(award)) if award in awardOrder else (1, award))


def urlModification(inputFile: Path = cfg.TABLE_PATH, outputFile: Path = cfg.TABLE_URL_PATH) -> None:
    """修饰主表的URL链接.

    Args:
        inputFile (Path, optional): 输入的 CSV 文件路径。默认为将使用路径"./table.csv"
        outputFile (Path, optional): 输出的 CSV 文件路径。默认为将使用路径"./table.csv"

    Raises:
        ValueError: 如果输入的文件不存在，则抛出异常

    Examples:
        >>> urlModification()
    """
    if not inputFile.exists():
        raise ValueError(f"The specified {inputFile} does not exist.")

    df = pd.read_csv(inputFile, encoding="utf-8")
    df["链接"] = "<" + df["链接"] + '>{:target="_blank"}'
    df.to_csv(outputFile, index=False, encoding="utf-8")
    print(f"Successfully generate url modification table {outputFile}")


def splitTable(filtration: str, outputDir: Path, inputFile: Path = cfg.TABLE_URL_PATH) -> None:
    """根据给定的过滤列将主表拆分.

    根据给定的过滤列将主表拆分为多个子表，并将子表保存在指定的输出目录中。
    每个子表的名称为过滤列的值，例如，如果过滤列为"年份"，则将生成多个子表，分别为"2022.csv"、"2021.csv"等。

    Note:
        应首先运行 urlModification() 以获得修饰后的主表

    Args:
        filtration (str): 过滤的列名称
        outputDir (Path): 输出目录路径
        inputFile (Path, optional): 输入的 CSV 文件路径。默认为将使用路径"./table-url.csv"

    Raises:
        ValueError: 如果输入的文件不存在，则抛出异常
        ValueError: 如果输出的目录不存在，则抛出异常
        ValueError: 如果指定的过滤列不是表的列，则抛出异常

    Examples:
        >>> splitTable("年份", cfg.DOCS_PATH / "zh" / "year")
    """
    if not inputFile.exists():
        raise ValueError(f"The specified input file {inputFile} does not exist.")
    if not outputDir.exists():
        raise ValueError(f"The specified output directory {outputDir} does not exist.")

    df = pd.read_csv(inputFile, encoding="utf-8")
    if filtration not in df.columns:
        raise ValueError(f"The specified filtration {filtration} is not a column of the table.")
    grouped = df.groupby(filtration)

    for filtrate, group in grouped:
        sorted_group = group.sort_values(by="获奖", key=awardSort, ascending=True)
        filename = Path(outputDir) / f"{filtrate}.csv"
        sorted_group.to_csv(filename, index=False, encoding="utf-8")
        print(f"Successfully generate sub-table {filtrate}.csv")


if __name__ == "__main__":
    urlModification()

    splitTable("年份", cfg.DOCS_PATH / "zh" / "year")
    splitTable("组别", cfg.DOCS_PATH / "zh" / "group")
    splitTable("获奖", cfg.DOCS_PATH / "zh" / "award")
