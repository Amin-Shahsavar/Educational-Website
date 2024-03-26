from kavenegar import *

from decouple import config
import logging


def send_sms(receptor, code):
    try:
        api = KavenegarAPI(config('SMS_API_KEY'))
        params = {
            # 'sender': config('SMS_NUMBER'),
            'receptor': str(receptor),
            'token': code,
        }
        response = api.sms_send(params)
        print(response)
        return True
    except APIException as e:
        print(e)
        logging.error(f'APIException: {e}')
        return False
    except HTTPException as e:
        print(str(e))
        return False
    except Exception as e:
        print(str(e))
        return False
