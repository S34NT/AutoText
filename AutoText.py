import applescript
from time import sleep
import pandas as pd
import re


#Applescript code for sending via iMessage
scpt_imessage = applescript.AppleScript('''
    on run {targetBuddy, targetMessage}
        
        tell application "Messages"
            set targetService to id of 1st account whose service type = iMessage
            set theBuddy to participant targetBuddy of account id targetService
            send targetMessage to theBuddy
        end tell
    end run
''')

#Applescript code for sending via SMS
scpt_SMS = applescript.AppleScript('''
    on run {targetBuddy, targetMessage}
        
        tell application "Messages"
            set targetService to id of 1st account whose service type = SMS
            set theBuddy to participant targetBuddy of account id targetService
            send targetMessage to theBuddy
        end tell
    end run
''')


def messageSend():
    
    #Open the .csv file
    readFile = pd.read_csv('csvWithPhoneAndMessage.csv')

    #read the 'Phone' column into a pandas series
    phones = pd.Series(readFile.Phone)
    #read the 'Message' column into a pandas series
    messages = pd.Series(readFile.Message)

    #initialize counter to 0
    count = 0

    #loop through the .csv file, send a message to each phone number
    for x in range(count, phones.size):
        phone = str(phones.iloc[x])
        message = messages.iloc[x]

        #send the message
        scpt_SMS.run(phone, message)
        
        #pause execution while message is attempting to send
        sleep(120)

        #print out the index after each send
        print(x)

    return()
   
messageSend()



