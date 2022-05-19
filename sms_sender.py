from email.mime import message
from twilio.rest import Client 
import time
# Your Account SID from twilio.com/console


account_sid = "AC22ac959da682b0c15f623e9ede7542c6"
auth_token  = "40c79de66045d2cc6879653ed7137764"
client = Client(account_sid, auth_token)

def read_and_send_file():
    leads_file = open("leads_//leads_example.txt", "r+")
    print("Reading text file ........")
    # Convert into list using readlines. 
    leads_content = leads_file.readlines()   
    print(f'Length of numbers in the text file: {len(leads_content)}')
    print("List of numbers in the text file: ")
 
    time.sleep(1)
    for each in leads_content:
        raw_leads = each.strip()
        print(raw_leads)
        print(f"Preparing to send sms / mms to {each}")

        message = client.messages.create(
        body = 'SMS / MMS test ',
        from_ = '+17435002492',
        to = each    
     )  
        try:
            print(message.sid)
        except:
            print("Unfortunately there seems to be a network connection error.")



    

read_and_send_file()


