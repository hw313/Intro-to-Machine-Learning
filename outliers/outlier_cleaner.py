#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    errors = []
    for index in range(0, len(predictions)):
    	errors.append(predictions[index] - net_worths[index]) 
    largest_ten_percent_indices = sorted(range(len(errors)), key=lambda i: errors[i])[-len(predictions)/10:]

    for index in range(0, len(predictions)):
    	if index not in largest_ten_percent_indices:
    		cleaned_data.append((ages[index], net_worths[index], errors[index]))
    
    return cleaned_data

