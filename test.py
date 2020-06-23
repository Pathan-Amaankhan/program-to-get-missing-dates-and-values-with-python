from datetime import timedelta
from datetime import datetime

def getMissingDatesAndValues(inp):
	listOfDates = list(inp.keys())
	listOfValues = list(inp.values())
	i=0

	while listOfDates[-1]!=listOfDates[i]:

		numberOfDaysInBetween = (datetime.strptime(listOfDates[i], "%Y-%m-%d").date() - datetime.strptime(listOfDates[i+1], "%Y-%m-%d").date()).days
		numberToAddOrSub = int((inp[listOfDates[i]] - inp[listOfDates[i+1]])/numberOfDaysInBetween)
		j=-1
		
		if(numberOfDaysInBetween>1):
			for j in range(numberOfDaysInBetween-1):
				listOfDates.insert(i+j+1,datetime.strftime(datetime.strptime(listOfDates[i],"%Y-%m-%d").date() - timedelta(days=j+1),"%Y-%m-%d"))
				listOfValues.insert(i+j+1,listOfValues[i+j]-numberToAddOrSub)
				
		elif(numberOfDaysInBetween<-1):
			for j in range(-numberOfDaysInBetween-1):
				listOfDates.insert(i+j+1,datetime.strftime(datetime.strptime(listOfDates[i],"%Y-%m-%d").date() + timedelta(days=j+1),"%Y-%m-%d"))
				listOfValues.insert(i+j+1,listOfValues[i+j]+numberToAddOrSub)
		i+=(1 if j<0 else j+2)

	return dict(zip(listOfDates,listOfValues))

inp = {"2019-01-04":100,"2019-01-01":115}
print(getMissingDatesAndValues(inp))
inp = {"2019-01-10":10,"2019-01-11":20,"2019-01-13":10}
print(getMissingDatesAndValues(inp))
