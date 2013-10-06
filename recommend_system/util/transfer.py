# -*- coding=utf-8 -*-

"""
transfer the origin netflix into three files:
    train.txt: data used to train, without prob data, file format:
        item_id:
        user_id, rating, date
        ...
    probe.txt: data used to test, file format:
        item_id, user_id, rate
    user_map: json file:  origin user id map to continous user id
"""

import json
import pickle
from utils import traverse_directory
#from matrix import RatingMatrix
from scipy.sparse import csc_matrix

ALL_USR_NUM = 480189
ALL_ITEM_NUM = 17770

DATASET_DIR = '/home/chouqin/Desktop/Recommender/download'

def get_contents(line):
    """
    get contents of a line
    return a tuple (item_id, rating)
    """
    content = line.strip()
    if content.find(':') != -1: # if it is line of itemd_id
        item_id = content.split(':')[0]
        return (item_id, None)
    else:
        user_id, rating, _ = content.split(',')
        return (None, (user_id, rating))

def get_user_map():
    user_map = {}
    index = 0
    #rm = RatingMatrix(ALL_USR_NUM, ALL_ITEM_NUM)
    rm = csc_matrix((ALL_USR_NUM, ALL_ITEM_NUM), dtype=int8)

    cur_item_id = 0
    cur_col = []
    count = 0
    for f in traverse_directory(DATASET_DIR + '/training_set'):
        with open(f, 'r') as fi:
            for line in fi:
                item_id, tu = get_contents(line)
                if not item_id:
                    user_id, rating = tu
                    user_id = int(user_id)
                    rating = int(rating)

                    # get the continous user id
                    if user_id not in user_map:
                        user_map[user_id] = index
                        index += 1

                    # set rating
                    #rm.add_user_rating(user_map[user_id], cur_item_id, rating)
                    #rm[user_map[user_id], cur_item_id] = rating
                    cur_col.append(
                    count += 1
                    if count % 100000 == 0:
                        print count
                else:
                    if len(cur_col) > 0:
                        rm[:, cur_item_id] = cur_col
                    cur_item_id = int(item_id) - 1
                    cur_col = []

    print count
    exit(0)
    return user_map, rm


def test_data(user_map):
    pass

def train_data(user_map, test_data):
    pass

if __name__ == '__main__':
    user_map, rm = get_user_map()
    #with open(DATASET_DIR + '/transfer/user_map', 'w') as f:
        #json.dump(user_map, f)
    #with open(DATASET_DIR + '/transfer/rating_matrix.pkl', 'w') as f:
        #pickle.dump(rm, f)

    #with open(DATASET_DIR + '/transfer/user_map', 'r') as f:
        #user_map = json.loads(f)
    #with open(DATASET_DIR + '/transfer/rating_matrix.pkl', 'r') as f:
        #rm = pickle.loads(f)

    #test_data = test_data(user_map)
    #train_data(user_map, test_data)
