//package com.chouqin.RatingMatrix;

import java.io.File;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.LinkedList;


public class RatingMatrix {
    final int USER_NUM = 480189;
    final int ITEM_NUM = 17770;

    public LinkedList<Tuple>[] ratings;

    public RatingMatrix() {
        ratings = (LinkedList<Tuple>[])new LinkedList[ITEM_NUM];
        for (int i = 0; i < ITEM_NUM; ++i) {
            ratings[i] = new LinkedList<Tuple>();
        }
    }

    public static void main(String[] args) {
        RatingMatrix rm = new RatingMatrix();
        rm.traverse();
    }

    public void traverse() {
        String traverseDir = "/home/chouqin/Desktop/Recommender/download/training_set/";
        File dir = new File(traverseDir);
        String[] files = dir.list();

        int itemId = 0;
        String[] result;
        int userId;
        byte rating;
        int count = 0;
        for (String file: files) {
            BufferedReader br = null;
            file = traverseDir + '/' + file;
            try {
                String line;
                br = new BufferedReader(new FileReader(file));

                while ((line = br.readLine()) != null) {
                    if (line.indexOf(':') != -1) {
                        result = line.split(":");
                        itemId = Integer.parseInt(result[0]);
                    } else {
                        result = line.split(",");
                        userId = Integer.parseInt(result[0]);
                        rating = (byte)Integer.parseInt(result[1]);
                        addItemRating(itemId, userId, rating);
                        count += 1;
                        if (count % 100000 == 0) {
                            System.out.println(count);
                        }
                    }
                }
            } catch (IOException e) {
                e.printStackTrace();
            } finally {
                try {
                    if (br != null)br.close();
                } catch (IOException ex) {
                    ex.printStackTrace();
                }
            }
        }
    }

    private void addItemRating(int itemId, int userId, byte rating) {
       ratings[itemId].add(new Tuple(userId, rating));
    }

    private class Tuple {
        public final int userId;
        public final byte rating;

        public Tuple(int uid, byte r) {
            this.userId = uid;
            this.rating = r;
        }
    }
}
