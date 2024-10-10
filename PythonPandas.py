import pandas as pd
import matplotlib.pyplot as plt

courselist = ["CCIT","CCDM","CCNS"]
courseID = [101,102,103]

#to use pandas Dataframe Function
#Create a dictionary
courseDict = {'course':courselist,'ID':courseID}

#use Function-->DATAFRAME
myvariable = pd.DataFrame(courseDict)
#print(myvariable)

#Panda Series
myvariable2 = pd.Series(courseDict)
#print(myvariable2)

#reading csv files
pulsedata = pd.read_csv('Pulse.csv')
#print(pulsedata)

update1= pulsedata.dropna()    #removes empty cells
#print(update1)

#Changing date format
update2 = pd.read_csv('Pulse.csv')
update2['Date'] = pd.to_datetime(update2["Date"])
#YYYY-MM-DD
#print(update2)

#Change Value
pulsedata.loc[10,'Pulse']=111
#print(pulsedata)

#Using Mathplot and pandas
pulsedata = pd.read_csv('Pulse.csv')
pulsedata.plot(kind='scatter',x='Duration',y='Calories')
#plt.show()

#histogram
pulsedata["Duration"].plot(kind='pie')
#plt.show()







