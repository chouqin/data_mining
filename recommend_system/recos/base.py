# -*- coding=utf-8 -*-

"""
Base class of Recommender
"""

import math

class Recommender:
    def __init__(self, train_path, test_path, train_cls, test_cls, fnum=None):
        self.trainm = train_cls.loads(train_path) # train matrix
        self.testm = test_cls.loads(train_path) # test matrix
        self.unum = self.trainm.get_user_number()
        self.inum = self.trainm.get_item_number()

        self.init_parameters()
        self.train()
        self.test()

        # fnum should be determined when init
        self.fnum = fnum

    def rmse(self, fnum=None):
        count = 0
        esum = 0

        for uid, iid, rating in self.testm:
            prating = self.predict_rating(uid, iid)
            esum += (prating - rating) * (prating - rating)
            count += 1

        return math.sqrt(float(esum) / count)

    def fit(self, lbda, gamma, k=60, srate=1, **kwargs):
        print "begin to train baseline model..."

        pre_rmse = cur_rmse = 0

        for i in range(k):
            cur_rmse = 0
            print "iteration: ", i

            # iterate every rating to update parameters
            for uid, ratings in enumerate(self.trainm.get_ratings()):
                for iid, rating in ratings
                    # first: compute eui
                    prating = self.predict_rating(uid, iid)
                    eui = (rating - prating)
                    cur_rmse += eui

                    # update bu and bi
                    self.update_parameters(lbda, gamma, uid, iid, eui, **kwargs)

            # if rmse begin to increase, stop
            if cur_rmse > pre_rmse  and i != 0:
                print pre_rmse, cur_rmse, 'rmse begin to increase, stop iteration'

            print "finish iteration: ", i, pre_rmse, cur_rmse
            pre_rmse = cur_rmse
            gamma *= srate

        #print "finish all iteration, current rmse is", self.rmse()
        print "finish train"

    def init_parameters(self):
        raise NotImplementedError

    def predict_rating(self, uid, iid):
        """
        predict rating of uid to iid
        """
        raise NotImplementedError
