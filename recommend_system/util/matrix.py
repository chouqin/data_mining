# -*- coding=utf-8 -*-

import redis

class RatingMatrix:
    def __init__(self, unum, inum):
        """
        init the matrix with unum users
        store a array of rating for each user
        """
        self.unum = unum
        self.inum = inum
        self.rclient = redis.StrictRedis(host='localhost', port=6379, db=0)

    def add_user_rating(self, uid, iid, rating):
        """
        set rating for (uid, iid) entry
        each entry is a (iid, rating) tuple
        """
        self.rclient.lpush(uid, (iid, rating))

    def get_mean_rating(self):
        total = count = 0

        for uid in xrange(self.unum):
            for _, rating in self.get_user_ratings(uid):
                count += 1
                total += rating

        return float(total) / count

    def get_user_mean_rating(self, uid):
        total = count = 0

        for _, rating in self.get_user_ratings(uid):
            count += 1
            total += rating

        return float(total) / count

    def get_item_mean_rating(self, iid):
        total = count = 0

        for uid in xrange(self.unum):
            rating = self.get_user_ratings(uid, iid)
            if rating:
                count += 1
                total += rating

        return float(total) / count

    def get_user_item_rating(self, uid, iid):
        for iid, rating in self.get_user_ratings(uid):
            if iid == iid:
                return rating
        return None

    def get_ratings(self):
        return self.ratings

    def get_user_ratings(self, uid):
        size = self.rclient.llen(uid)
        for i in range(size):
            yield self.rclient.lindex(uid, i)

    def get_user_number(self):
        return self.unum

    def get_item_number(self):
        return self.inum
