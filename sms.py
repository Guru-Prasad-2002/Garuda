from boltiot import Sms, Bolt
import sys 
#
val=sys.argv[1]
mybolt = Bolt('BOLT API KEY', 'BOLT ID')
sms = Sms('Twilio Account Number', 'API KEY', 'Target Phone number', 'Twilio phone number')
response = mybolt.digitalWrite('0', 'HIGH')
response = sms.send_sms(val)

def status():
    response=mybolt.digitalRead('2')
