#!usr/bin/env python
#coding:utf-8

from readConfig import ReadConfig
import numpy as np


class BPMF:
    def __init__(self, trainMatrix, testMatrix, cf):
        self.trainMatrix = trainMatrix
        self.testMatrix = testMatrix
        self.cf = cf
        self.numUsers = 0
        self.numItems = 0

    def getParameters(self):
        self.numFactors = int(self.cf.getParameter('BPMF', 'numFactors'))
        self.MAX_Iteration = int(self.cf.getParameter('BPMF', 'MAX_Iteration'))

    def initGaussian(self, matrix, mean, var):
        ''''''
        return np.random.normal(mean, var, size=matrix.shape)

    def generateUVHyperParameters(self, matrix, N):
        # The prior of matrix
        beta0 = 2.0
        mu0 = np.zeros(self.numFactors)
        X_bar = matrix.mean(axis=1)
        v0 = self.numFactors
        # mu0_post = beta0 * mu0 + N*


    def buildModel(self):
        '''
        '''
        beta = 2
        mu_u = np.zeros(self.numFactors)
        mu_m = np.zeros(self.numFactors)

        # parameters of Inv-Whishart distribution
        WI_u = np.eye(self.numFactors)
        b0_u = 2
        df_u = self.numFactors
        mu0_u = np.zeros(self.numFactors)

        WI_m = np.eye(self.numFactors)
        b0_m = 2
        df_m = self.numFactors
        mu0_m = np.zeros(self.numFactors)

		# initializing Bayesian PMF using MAP solution found by PMF
        P = np.zeros((self.numUsers, self.numFactors))
        Q = np.zeros((self.numItems, self.numFactors))

        P = self.initGaussian(P, 0, 1)
        Q = self.initGaussian(Q, 0, 1)

        mu_u = P.mean(axis=1)
        mu_m = Q.mean(axis=1)

        alpha_u = np.asarray(np.asmatrix(np.var(P, axis=1))**(-1))
        alpha_m = np.asarray(np.asmatrix(np.var(Q, axis=1))**(-1))

		# Iteration:
        x_bar = np.zero(self.numFactors)
        normalRdn = np.zero(self.numFactors)

        M = self.numUsers
        N = self.numItems

        for iter in range(1, self.MAX_Iteration):

            # Sample from user hyper parameters
            x_bar = P.mean(axis=1)
            S_bar = np.var(P, axis=1)

            mu0_u_x_bar = mu0_u - x_bar
            e1e2 = np.asmatrix(mu0_u_x_bar).transpose() * np.asmatrix(mu0_u_x_bar)
            e1e2 /= (M * b0_u / (b0_u + M + 0.0))

            WI_post = np.
			WI_post = WI_u.inv().add(S_bar.scale(M)).add(e1e2);
			WI_post = WI_post.inv();
			WI_post = WI_post.add(WI_post.transpose()).scale(0.5);

			df_upost = df_u + M;
			DenseMatrix wishrnd_u = wishart(WI_post, df_upost);
			if (wishrnd_u != null)
				alpha_u = wishrnd_u;
			mu_temp = mu0_u.scale(b0_u).add(x_bar.scale(M)).scale(1 / (b0_u + M + 0.0));
			lam = alpha_u.scale(b0_u + M).inv().cholesky();

			if (lam != null) {
				lam = lam.transpose();

				for (int f = 0; f < numFactors; f++)
					normalRdn.set(f, Randoms.gaussian(0, 1));

				mu_u = lam.mult(normalRdn).add(mu_temp);
			}