from twilio.rest import Client 
 
account_sid = '<ACCOUNT SID' 
auth_token = 'AUTH TOKEN' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(  
                              messaging_service_sid='SERVICE ID', 
                              body='VALORANT',      
                              to='+639561657728' 
                          ) 
 
print(message.sid)
