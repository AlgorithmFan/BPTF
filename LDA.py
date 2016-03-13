#!usr/bin/env python
#coding:utf-8

'''
 Blei, David M., Andrew Y. Ng, and Michael I. Jordan. "Latent Dirichlet Allocation."
 Journal of Machine Learning Research 3 (2003): 993–1022.
'''
import sys
import numpy as np


class LDA:
    ''' Latent Dirichlet allocation using collapsed Gibbs sampling '''
    def __init__(self, cf):
        self.cf = cf

    def getParameters(self):
        self.numFactors = int(self.cf.getParameter('LDA', 'numFactors'))
        self.MAX_Iteration = int(self.cf.getParameter('LDA', 'MAX_Iteration'))

        self.alpha = float(self.cf.getParameter('LDA', 'alpha'))
        self.beta = float(self.cf.getParameter('LDA', 'beta'))


    def fit(self):
        pass


