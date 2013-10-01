#include <vector>
#include <list>
#include <fstream>
#include <iostream>
#include <dirent.h>
#include <sys/types.h>
#include <stdlib.h>

using namespace std;

struct tuple {
    short iid;
    char rating;
};

const int USER_NUM = 480189;
const string PATH = "/home/chouqin/Desktop/download/transfer_set/";

void splitstr(string str, string sep, vector<string> &res) {
    int pos = 0;
    string token;

    res.clear();
    vector<string>().swap(res);
    while ((pos = str.find(sep)) != string::npos) {
        token = str.substr(0, pos);
        res.push_back(token);
        str.erase(0, pos + sep.length());
    }
}

void loadRating(vector <vector <tuple> > &ratings) {
    DIR *dp;
    struct dirent *ep;
    dp = opendir(PATH.c_str());
    string filename, filepath;
    string line;
    vector<string> res;
    int count = 0;
    short iid = 0;
    int uid = 0;
    char rating = 0;

    while (ep = readdir(dp)) {
        filename = ep->d_name;
        filepath = PATH + filename;

        ifstream f(filepath.c_str());
        while (getline(f, line)) {
            if (line.find(':') != -1) {
                splitstr(line, ":", res);
                iid = atoi(res[0].c_str());
            } else {
                splitstr(line, ",", res);
                uid = atoi(res[0].c_str());
                rating = (char)atoi(res[1].c_str());

                // push rating to ratings
                //cout << uid << " " << iid << " " << (int)rating << endl;
                tuple tu;
                tu.iid = iid;
                tu.rating = rating;
                ratings[uid].push_back(tu);

                // update count
                count += 1;
                if (count % 100000 == 0) {
                    cout << count << endl;
                }
            }
        }

        //cout << filepath << endl;
        f.close();
    }
    closedir(dp);
}

int main() {
    //vector<string> res;
    //string s = "scott>=tiger>=mushroom";
    //string delimiter = ">=";
    //splitstr(s, delimiter, res);

    //cout << "split result:" << endl;
    //for(std::vector<string>::iterator it = res.begin(); it != res.end(); ++it) {
        //cout << *it << endl;
    //}
    //return 0;

    vector <vector <tuple> > ratings(USER_NUM);

    // init each tuple
    //vector <vector <tuple> > ratings;
    //for (int i = 0; i < USER_NUM; ++i) {
        //vector<tuple> rating;
        //ratings.push_back(rating);
    //}

    //tuple tu;
    //tu.iid = 1;
    //tu.rating = (char) 3;

    //ratings[0].push_back(tu);

    loadRating(ratings);

    //for (int i = 0; i < ratings.size(); ++i) {
        //if (i == 2 || i == 1) {
            //cout << "user " << i << ": ";
            //for (vector<tuple>::iterator it = ratings[i].begin(); it != ratings[i].end(); ++it) {
                //cout << "(" << it->iid << ", " << (int)it->rating << ")" << ", ";
            //}
            //cout << endl;
        //}
    //}

    return 0;
}

