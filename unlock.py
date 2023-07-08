from boltiot import Sms, Bolt
import sys 

mybolt = Bolt('e6a9fef6-cb95-41e4-acfe-3953e1bb9467', 'BOLT848710')
sms = Sms('ACbfaef5952757e880587ca693232ac58a', 'db881f9cf65cc1465b43e521563a508f', '+91 8431003590', '+18142125826')

def unlock_door():
    response=mybolt.digitalWrite('0','LOW')
    response = sms.send_sms("Testing Unlock Functionality")
