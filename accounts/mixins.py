from django.conf import settings
from accounts.models import *
import messagebird
import random


class MessaHandler:
    phone_number = None
    otp = None
    def __init__(self, phone_number, otp) -> None:
        self.phone_number = phone_number
        self.otp = otp


    def send_otp(self):
        client = messagebird.Client(settings.MESSAGEBIRD_KEY)
        try:
            # message = client.message_create(
            #     # "SkilledCheck LTD",
            #     '+12068038349',
            #     body =f'Your SkilledCheck otp is {self.otp}',
            #     recipients = {self.phone_number}

            #     # 'sender_name', '+1XXXXXXXXXX', 'test message'
            #     )
            # print(message.__dict__)
            msg = client.message_create('+12068038349',
                 self.phone_number,
                                         body =f'Your SkilledCheck otp is {self.otp}'
                                         )
            print(msg.__dict__)

        except messagebird.client.ErrorException as e:
            for error in e.errors:
                print(error)
        



        