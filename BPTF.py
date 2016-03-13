#!usr/bin/env python
#coding:utf-8

from readConfig import ReadConfig
import numpy as np
from wishart import wishrnd

class BPTF:
    def __init__(self, trainTensor, testTensor, cf):
        self.trainTensor = trainTensor
        self.testTensor = testTensor
        self.cf = cf

    def getHyperParameters(self):
        self.numFactors = int(self.cf.getParameter('BPTF', 'numFactors'))
        self.nuAlpha = int(self.cf.getParameter('BPTF', 'nuAlpha'))
        self.Walpha = int(self.cf.getParameter('BPTF', 'Walpha'))
        self.mu0 = int(self.cf.getParameter('BPTF', 'mu'))
        self.muT0 = int(self.cf.getParameter('BPTF', 'muT'))
        self.beta0 = int(self.cf.getParameter('BPTF', 'beta'))
        self.W0 = np.eye(self.numFactors)
        self.W0T = np.eye(self.numFactors)

        self.iWalpha = 1.0/self.Walpha


    def generateUVHyperParameters(self, matrix, N):
        ''''''
        # The prior of matrix
        beta0 = 2.0
        v0 = self.numFactors
        mu0 = np.zeros(self.numFactors)
        W0 = np.eye(self.numFactors)

        X_bar = matrix.mean(axis=1)
        S_bar = np.cov(matrix.transpose())

        mu0_post = (beta0 * mu0 + N * X_bar) / (beta0 + N)
        beta0_post = beta0 + N
        v0_post = v0 + N

        WI0 = np.linalg.inv(W0)
        WI0_post = WI0 + N * S_bar + beta0 * N / beta0_post * np.outer(mu0 - X_bar, mu0 - X_bar)
        W0_post = np.linalg.inv(WI0_post)

        Lambda = wishrnd(W0_post, v0_post)
        sigma = np.linalg.cholesky(np.linalg.inv(Lambda * beta0))
        normalRdn = np.random.normal(0, 1, size=self.numFactors)

        mu_post = np.inner(sigma, normalRdn) + mu0_post

        return mu_post, Lambda

    def generateTHyperParameters(self, matrix, K):
        pass

    def gibbsUVSampling(self):
        pass

    def gibbsTSampling(self):
        pass

    def buildModel(self):
        pass




