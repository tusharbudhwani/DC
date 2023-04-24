from datetime import timedelta

numClients = int(input("Enter the number of clients: "))
clientTimes = input("Enter client time for each client separated by space: ").split()
serverTime = input("Enter server time: ")

def timeToSeconds(time):
    h,m = time.split(":")
    inSeconds = int(h)*60*60 + int(m)*60
    return inSeconds

def timetoHours(timeInSeconds):
    formattedTime = timedelta(seconds=timeInSeconds)
    return formattedTime

sum = 0
for time in clientTimes:
    sum = sum + timeToSeconds(time)

sum = sum + timeToSeconds(serverTime)

averageTime = int(sum/numClients+1)

print("The new time for the system is: ", timetoHours(averageTime))