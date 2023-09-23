# -*- coding: utf-8 -*-
#
# File: split.py
# MIT License
#
# Main Change Logs:
# Date          Author      Notes
# 2023-09-22    Baiqi.Lu    Create file
#

import os, sys
import pandas as pd

def awardSort(awards):
    """ 按照奖项级别进行排序 """
    awardOrder = [
        '国家级一等奖', '国家级二等奖', '国家级三等奖', '省级一等奖', '省级二等奖', '省级三等奖'
    ]
    return awards.map(lambda award: (0, awardOrder.index(award)) if award in awardOrder else (1, award))


def splitTable(filtration, outputDir, inputFile='./table.csv'):
    """
    将汇总表按照筛选条件拆分成分表
    参数:
        - filtration    (str): 列名称
        - outputDir     (str): 输出文件路径
        - inputFile     (str): 输入的CSV文件路径。默认为 'table.csv'
    """

    if not os.path.exists(outputDir):
        raise ValueError(f'The specified {outputDir} does not exist.')
    if not os.path.exists(inputFile):
        raise ValueError(f'The specified {inputFile} does not exist.')

    df = pd.read_csv(inputFile)

    grouped = df.groupby(filtration)

    for filter, group in grouped:
        sorted = group.sort_values(by='获奖', key=awardSort, ascending=True)
        filename = os.path.join(outputDir, f'{filter}.csv')
        sorted.to_csv(filename, index=False)
        print(f'Successfully generate sub-table {filter}.csv .')


if __name__ == '__main__':
    sys.path.append(os.getcwd())

    splitTable('年份', './docs/year')
    splitTable('组别', './docs/group')
    splitTable('获奖', './docs/award')
