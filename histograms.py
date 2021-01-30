# Objective for this script is to access the database
# Loop through all the patient data, only grabbing info for an individual patient at a time
# Build a histogram out of the data and store it in an array for Matt to display on screen as he wishes

import sqlite3, numpy

from matplotlib import pyplot as plt
from sqlite3 import Error

#Access the database
def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

#Query the database
def query_patient(connection, patient_id):
    cursor = connection.cursor()
    t = [patient_id]
    try:
        cursor.execute("SELECT PATIENT_ID, BED_ID, O2 FROM Data WHERE PATIENT_ID = ?", t)
        connection.commit()
        print("Query executed successfully")
        return cursor.fetchall()
    except Error as e:
        print(f"The error '{e}' occurred")

#Create histogram off of one patient data
def create_histogram(connection, patientData):
    o2list = []
    for data in patientData:
        o2list.append(data[2]) #Grab oxygen from each time
    stdDev = numpy.std(o2list)
    average = numpy.mean(o2list)
    age = int(get_patient(connection, patientData[0][0])[1])
    isOutside = is_outside_expected(age, stdDev, average)

    hist = numpy.histogram(o2list, [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]) 

    #Used for creating graphs    
    #plt.hist(o2list, [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94])
    #plt.title("Patient %s" % patientData[0][0])
    #plt.show()
    
    return (patientData[0][0], average, isOutside, hist[0], hist[1]) #Returns a tuple with the required information to make a histogram and any additional info
    #Returns in order: patient id, average oxygen content, if the oxygen is outside the range, list of oxygen in respective bins, bins for histogram

#Using statistics, determines if the oxygen is stastically significant below the lower boundary
#Also provides bins for the histogram
def is_outside_expected(age, stdDev, average):
    if age < 32:
        lower = 88
    elif age < 35:
        lower = 90
    else:
        lower = 95
    
    if(stdDev * 2 + average < lower): #If it's outside two standard deviations of the average, it's statistically significant and needs to be addressed
        return True
    else:
        return False

#Gets patient age from database    
def get_patient(connection, patient_id):
    cursor = connection.cursor()
    t = [patient_id]
    try:
        cursor.execute("SELECT PATIENT_ID, AGE_WEEKS FROM Patient WHERE PATIENT_ID = ?", t)
        connection.commit()
        print("Query executed successfully")
        return cursor.fetchone()
    except Error as e:
        print(f"The error '{e}' occurred")

def get_all_histograms(): #Gets all patient data and gets it ready for histogram, as well as grabbing essential data
    connection = create_connection('capstone.sqlite')
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT PATIENT_ID FROM Patient")
        connection.commit()
        print("Query executed successfully")
        patients = cursor.fetchall()
        histogram_list = []
        for patient in patients:
            histogram_list.append(create_histogram(connection, query_patient(connection, patient[0])))
        return histogram_list

    except Error as e:
        print(f"The error '{e}' occurred")

print(get_all_histograms())
