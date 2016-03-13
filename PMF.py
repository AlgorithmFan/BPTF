#!usr/bin/env python
#coding:utf-8

from readConfig import ReadConfig
import numpy as np


class PMF:
    def __init__(self, trainMatrix, testMatrix, cf):
        self.trainMatrix = trainMatrix
        self.testMatrix = testMatrix
        self.cf = cf
        self.numUsers = 0
        self.numItems = 0
