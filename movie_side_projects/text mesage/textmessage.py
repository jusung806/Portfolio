from twilio.rest import TwilioRestClient

account_sid = "AC7f1f5160294b2d24b6cee5d3640657c3" # Your Account SID from www.twilio.com/console
auth_token  = "fe9f8aa18118ebba10ac3218172ecbd7"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
    body="Hey! It's Eliza!",
    to="+14156234529",    # Replace with your phone number
    from_="+14158747838") # Replace with your Twilio number

printmessage.sid
