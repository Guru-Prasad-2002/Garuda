#!/usr/bin/env python 3
from boltiot import Sms, Bolt

#
mybolt = Bolt('Bolt Device API Key', 'BOLT Device ID')
sms = Sms('Twilio Account ID', 'Twilio Account Token', 'Receiver Phone Number', 'Sender Phone Number')
response = mybolt.digitalWrite('0', 'HIGH')
response = sms.send_sms("Hello Guruji")
response = mybolt.digitalWrite('0', 'LOW')
