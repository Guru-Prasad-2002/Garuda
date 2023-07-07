from boltiot import Sms, Bolt
import sys 
#
val=sys.argv[1]
mybolt = Bolt('e6a9fef6-cb95-41e4-acfe-3953e1bb9467', 'BOLT848710')
sms = Sms('ACbfaef5952757e880587ca693232ac58a', 'db881f9cf65cc1465b43e521563a508f', '+91 8431003590', '+18142125826')
response = mybolt.digitalWrite('0', 'LOW')
response = mybolt.digitalWrite('0', 'HIGH')
response = mybolt.digitalWrite('0', 'LOW')
response = sms.send_sms(val)

# from boltiot import Sms, Bolt

# mybolt = Bolt('e6a9fef6-cb95-41e4-acfe-3953e1bb9467', 'BOLT848710')
# sms = Sms('ACbfaef5952757e880587ca693232ac58a', 'db881f9cf65cc1465b43e521563a508f', '+91 8431003590', '+18142125826')
# response = mybolt.digitalWrite('0', 'HIGH')
# response = mybolt.digitalWrite('0', 'LOW')
# response = sms.send_sms("L")