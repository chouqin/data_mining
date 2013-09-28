# -*- coding=utf-8 -*-

"""
Base class of Recommender
"""

import math

class Recommender:
    def __init__(self, train_path, test_path, data_cls):
        self.trainm = data_cls.loads(train_path) # train matrix
        self.testm = data_cls.loads(train_path) # test matrix
        self.unum = self.trainm.get_user_number()
        self.inum = self.trainm.get_item_number()

        self.init_parameters()
        self.train()
        self.test()


    def rmse(self, fnum=None):
        count = 0
        esum = 0

        for uid, ratings in enumerate(self.testm.get_ratings()):
            for iid, rating in ratings:
                prating = self.predict_rating(uid, iid, fnum)
                esum += (prating - rating) * (prating - rating)
                count += 1

        return math.sqrt(float(esum) / count)

    def init_parameters(self):
        raise NotImplementedError

    def train(self):
        raise NotImplementedError

    def test(self):
        raise NotImplementedError

    def predict_rating(self, uid, iid, fnum=None):
        """
        predict rating of uid to iid
        """
        raise NotImplementedError
