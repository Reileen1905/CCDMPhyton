import pandas as pd
import matplotlib.pyplot as plt


##Q1.
#Create an Object called "Empdata" to read employees file
Empdata = pd.read_csv('employees.csv')   #Displays 1000 Rows by 8 columns
#print(Empdata)

##Question 2
#Create New Object nonull to remove empty\null rows
#Use dropna
Nonull = Empdata.dropna()   #displays 764 Rows by 8 Columns
#print(Nonull)

#Question? How many rows were dropped? 1000 - 764 = 236 rows were dropped

#Question 3
#Create object empStartDate to format date to YYYY-MM-DD
empStartDate = pd.read_csv('employees.csv')
empStartDate['Start Date'] = pd.to_datetime(empStartDate["Start Date"])
#YYYY-MM-DD
#print(empStartDate)

#Question 4
#Using Plot function, come up with a 
#Histogram chart based on Salary to answer the following

Empdata['Salary'].plot(kind='hist')
plt.show()


#What is the range that most employees are paid within?
#Provide ans: 80,000 - 100,000

