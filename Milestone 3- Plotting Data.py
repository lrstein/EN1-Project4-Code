import csv
import matplotlib.pyplot as plt

#reads csv file found in same folder as code and opens as freezerFile
with open('freezer_dial1to2_2.csv', 'r') as freezerFile:
    #empty lists to hold temperatures and times
    freezerTimes = []
    freezerTemps = []
    csv_reader = csv.reader(freezerFile)
    #skips over default headers in first row using "next" function
    headers = next(csv_reader)
    #retrieves first time value and sets equal to startTime
    initial = next(csv_reader)
    startTime = initial[0]
    
    #add each value to respective lists
    for row in csv_reader:
        #convert strings to floats
        #subtract startTime to get time relative to start of data collection
        #divide relative time by 3600 to get hours since start of data collection
        freezerTimes.append((float(row[0]) - float(startTime))/3600)
        freezerTemps.append(float(row[1]))

#same functions as found above in reading freezerFile, but does same thing for fridgeFile
with open('fridge_dial1to2_2.csv', 'r') as fridgeFile:
    fridgeTimes = []
    fridgeTemps = []
    csv_reader = csv.reader(fridgeFile)
    headers = next(csv_reader)
    initial = next(csv_reader)
    startTime = initial[0]
    
    for row in csv_reader:
        fridgeTimes.append((float(row[0]) - float(startTime))/3600)
        fridgeTemps.append(float(row[1]))

#plot both data streams on the same graph
plt.plot(fridgeTimes, fridgeTemps)
plt.plot(freezerTimes, freezerTemps)
#label data and graph
plt.title("Temperature vs. Time (Dial 1 to 2)")
plt.xlabel("time (hrs)")
plt.ylabel("temperature (°F)")
plt.show()