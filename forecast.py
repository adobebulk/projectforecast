#! Project Forecast
# Copyright 2020 C.T. Smith
# http://ctsmith.org 

""" A Program which depitcs the current day's weather, as forecast
by the United States National Weather Service
"""

import sys
import datetime
import re
from ftplib import FTP

def main():

    statement_header = 'WEATHER STATEMENT' #printout
    statement_general = 'PARSED BY CTSMITH.ORG\nFROM THE NATIONAL WEATHER SERVICE\n. . .'
    
    #Gets the current date
    date_get = datetime.date.today()
    #Gets the hour and minute and puts them together, like you would see on a clock.
    time_get = "%d:%d" % (datetime.datetime.now().hour, datetime.datetime.now().minute)
    

    
    #Establish the FTP connection and desired directory.
    ftp = FTP('tgftp.nws.noaa.gov')
    ftp.login(user='anonymous', passwd = '')
    ftp.cwd('/data/forecasts/state/ok/')
    #Should add a bailout for if the FTP fails (say, if the internet is down).
    
    #This is the method which will grab the file from the FTP directory.
    def grabFile():
        
        filename = 'okz041.txt'
        
        localfile = open(filename, 'wb')
        ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
        
        ftp.quit()
        localfile.close()
        
    #grab the file
    grabFile()
    
    def searchFile():
        
        searchTerm = 'Oklahoma City'
        
        with open('okz041.txt') as myFile:
            for num, line in enumerate(myFile, 1):
                if searchTerm in line:
                    foundLine = num

            #debugging 
            #print foundLine
            
            #Close the file, good housekeeping.
            myFile.close()
            return foundLine
    
    #We're going to print out like four lines of data from this file. It's going to start at the 
    #line we just searched, so let's set that line as our index here.
    startLine = searchFile()

    
    #experimental element splitter
    with open('okz041.txt') as myFile:
        #We load every thing we want from the specified city into a list called lines.
        #The NWS formatted text file is associated with 4 lines of text of info.
        #The first line is the city. The second line is the forecasted condition
        #the third line is the Low/High temperature in degrees F
        #the fourth line is probability of precipitation now and then some time later?
        lines = myFile.readlines()[(startLine-1):(startLine+3)]
        
        #We now have a line which is a list. The list is already in an order which we know.
        #We take the second line, first column (delimted by three spaces) for the predicted
        #condition of the day 
        #We will take that line, split it by the delimeter (which turns it into a list)
        #and store that day's predicted condition.
        predictedCondition = lines[1].strip().split("   ")
        
        predictedTemps = lines[2].split('/')
        predictedHigh = predictedTemps[1].split('    ')
        predictedLow = predictedTemps[0].strip('    ')        
        
        #for line in lines:
        #    elements = line.strip().split("   ")
        #    print elements
        #print elements[0]    
    myFile.close()
    
    print statement_header #Print the header
    print date_get, time_get, 'H' #Print out the date, time, and show it as hours.
    print statement_general #prints the general statement
    
    print 'TODAY    .   .   .   %s' % date_get
    print 'CONDITION    .   .   %s' % predictedCondition[0]
    print 'HIGH     .   .   .   %s F' % predictedHigh[0]
    print 'LOW      .   .   .   %s F' % predictedLow
  
    outputFile = open('output.txt', 'w')
    outputFile.write(statement_header + '\n')
    outputFile.write('%s %s H' % (date_get, time_get) + '\n')
    outputFile.write(statement_general + '\n')
    outputFile.write('TODAY    .   .   .   %s' % date_get + '\n')
    outputFile.write('CONDITION    .   .   %s' % predictedCondition[0] + '\n')
    outputFile.write('HIGH     .   .   .   %s F' % predictedHigh[0] + '\n')
    outputFile.write('LOW      .   .   .   %s F' % predictedLow + '\n')
    outputFile.close()

#Standard command for calling the main function.
if __name__ == '__main__':
    main()