from twilio.rest import Client 
 
account_sid = 'AC9625235c06066ca5a4a3aca16daf0341' 
auth_token = '779e6578b1bb369c2329a65bdc8fafe0' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(  
                              messaging_service_sid='MGd9b3d9bb0785042bb9187f296a9a23f9', 
                              body='VALORANT',      
                              to='+639561657728' 
                          ) 
 
print(message.sid)