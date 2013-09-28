# -*- coding=utf-8 -*-

class RatingMatrix:
    def __init__(self, unum, inum):
        """
        init the matrix with unum users
        store a array of rating for each user
        """
        self.unum = unum
        self.inum = inum
        self.ratings = []
        for i in xrange(unum):
            self.ratings.append([])

    def add_user_rating(self, uid, iid, rating):
        """
        set rating for (uid, iid) entry
        each entry is a (iid, rating) tuple
        """
        self.ratings[uid].append((iid, rating))

    def get_mean_rating(self):
        total = count = 0

        for ratings in self.ratings:
            for _, rating in ratings:
                count += 1
                total += rating

        return float(total) / count

    def get_user_mean_rating(self, uid):
        total = count = 0

        for _, rating in self.ratings[uid]:
            count += 1
            total += rating

        return float(total) / count

    def get_item_mean_rating(self, iid):
        total = count = 0

        for ratings in self.ratings:
            for iid, rating in ratings:
                if iid == iid:
                    count += 1
                    total += rating

        return float(total) / count

    def get_ratings(self):
        return self.ratings

    def get_user_number(self):
        return self.unum

    def get_item_number(self):
        return self.inum
