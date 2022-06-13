# AutoText
This program will send out Text Messages via SMS to a list of phone numbers, where each unique phone number has a corresponding message in a .csv file

##Requirements
In order to run this program you must be using an Apple computer that is connected to your Apple ID, and it must be synced with your phone. All messages will send out via your phone number or the email that is associated with your Apple ID, depending on what your settings are.

##Setup
1) Clone the repository
2) Type the Following Command in to the Terminal and press Enter: pip install -r requirements.txt
3) Change the filename in line 35 to the .csv file you wish to use. Make sure that there is a column named 'Phone' and a column Named 'Message'
4) Navigate to the project directory in your terminal, and type: python3 AutoText.py
5) Hit Enter

##Details
This program will send out a text message to each phone number under the 'Phone' Column in your .csv file using the corresponding message in the 'Message' Column.
Currently all messages are sent via SMS, however, there is an iMessage option that works too. Eventually, this program will attempt to send all messages via iMessage, and if iMessage fails it will send via SMS.

##Send via iMessage
If you would like to use the iMessage option and don't want to wait for the next update, change line 51 in the AutoText.py file to say: scpt_imessage.run(phone, message)
All messages will attempt to send via iMessage.

