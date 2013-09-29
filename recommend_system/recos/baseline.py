# -*- coding=utf-8 -*-

"""
implementation of the svd recommender
"""

from base import Recommender

class baseline(Recommender):
    def init_parameters(self):
        """
        parameters: bu, bi
        """
        print "begin init parameters..."
        self.mean = self.trainm.get_mean_rating()
        self.bu = [0] * self.unum
        self.bi = [0] * self.inum
        #self.total = 0

        ucount = [0] * self.unum
        icount = [0] * self.inum

        for uid, ratings in enumerate(self.trainm.get_ratings()):
            for iid, rating in ratings:
                self.bu[uid] += rating - self.mean
                self.bi[iid] += rating - self.mean

                ucount[uid] += 1
                icount[iid] += 1
                #self.total += 1

        for i in xrange(self.unum):
            self.bu[i] /= float(self.ucount[i])

        for i in xrange(self.inum):
            self.bi[i] /= float(self.icount[i])

        print "finish init parameters"

    def predict_rating(self, uid, iid):
        """
        predict rating of uid to iid
        """
        rating = self.mean + self.bu[uid] + self.bi[iid]
        if rating > 5:
            rating = 5
        elif rating < 1:
            rating = 1

        return rating

    def update_parameters(self, lbda, gamma, uid, iid, eui):
        self.bu[uid] += gamma * (eui - lbda * self.bu[uid])
        self.bi[iid] += gamma * (eui - lbda * self.bi[iid])
