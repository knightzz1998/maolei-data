# -*- coding: utf-8 -*-
# @Time    : 2023/1/11 17:27
# @Author  : 王天赐
# @Email   : 15565946702@163.com
# @File    : main.py
# @Software: PyCharm

import pandas as pd
from numpy import NaN


def solution(source, target):
    data = pd.read_csv(source, sep='\t',
                       header=0, encoding="UTF-8")
    drugNames = data['drugName']
    conditions = data['condition']
    reviews = data['review']
    ratings = data['rating']

    aspect = []

    for i in range(len(reviews)):
        if drugNames[i] is NaN:
            aspect.append(conditions[i])
            continue
        if conditions[i] is NaN:
            aspect.append(drugNames[i])
            continue
        if drugNames[i] is NaN and conditions[i] is NaN:
            print(i)
        aspect.append(drugNames[i] + " " + conditions[i])

    with open(target, mode="a", encoding="UTF-8") as f:
        for i in range(len(reviews)):
            f.write(reviews[i] + "\n")
            f.write(aspect[i] + "\n")
            f.write("{}\n".format(ratings[i]))


if __name__ == '__main__':
    source = "dataset/drugsComTrain_raw.tsv"
    target = "result/drugsComTrain_processed.txt"
    solution(source, target)
