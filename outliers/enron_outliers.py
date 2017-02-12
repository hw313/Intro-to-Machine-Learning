#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
#for name in data_dict:
	#print name, "\n"
features = ["salary", "bonus"]

### your code below
data_dict.pop( "TOTAL", 0 ) # The other two outliers: (1)SKILLING JEFFREY K; (2)LAY KENNETH L
data = featureFormat(data_dict, features)
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()


