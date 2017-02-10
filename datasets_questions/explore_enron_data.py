#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print "people num:", len(enron_data)
#for people in enron_data:
#	print people, "\n"

print "feature num: ", len(enron_data["SKILLING JEFFREY K"])
#for feature in enron_data["SKILLING JEFFREY K"]:
#	print feature, "\n"

num_POI = 0
num_POI_have_Nan_for_their_total_payments = 0
num_folks_have_quantified_salary = 0
num_folks_have_known_email_address = 0
num_folks_have_Nan_for_their_total_payments = 0
for people in enron_data:
	if enron_data[people]["poi"] == 1:
		num_POI += 1
	if enron_data[people]["salary"] != "NaN":
		num_folks_have_quantified_salary += 1
	if enron_data[people]["email_address"] != "NaN":
		num_folks_have_known_email_address += 1
	if enron_data[people]["total_payments"] == "NaN":
		num_folks_have_Nan_for_their_total_payments += 1
		if enron_data[people]["poi"] == 1:
			num_POI_have_Nan_for_their_total_payments += 1
print "POI num: ", num_POI
print "Percentage of POIs have Nan for their total payments: ", 100 * num_POI_have_Nan_for_their_total_payments/len(enron_data)
print "Folks have quantified salary: ", num_folks_have_quantified_salary
print "Folks have known email address: ", num_folks_have_known_email_address
print "Percentage of folks have Nan for their total payments: ", 100 * num_folks_have_Nan_for_their_total_payments/len(enron_data)

print "Total value of the stock belonging to James Prentice", enron_data["PRENTICE JAMES"]["total_stock_value"]

print "Messages from Wesley Colwell to POIs", enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

print "Value of stock options exercised by Jeffrey K Skilling", enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

print "Money took home by Jeffrey K Skilling", enron_data["SKILLING JEFFREY K"]["total_payments"]
print "Money took home by Kenneth L Lay", enron_data["LAY KENNETH L"]["total_payments"]
print "Money took home by Andrew S Fastow", enron_data["FASTOW ANDREW S"]["total_payments"]

