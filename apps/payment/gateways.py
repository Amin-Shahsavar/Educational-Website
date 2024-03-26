from decouple import config
import requests
from xml.etree import ElementTree as ET
#ge6od631p2lE1t2181qt
class Parsian:

    def __init__(self) -> None:
        self.url = 'https://pec.shaparak.ir/NewIPGServices/Sale/SaleService.asmx'
        self.soap_action = 'https://pec.Shaparak.ir/NewIPGServices/Sale/SaleService/SalePaymentRequest'
        self.callback_url = 'http://127.0.0.1:8000/payment/verify/'
        self.login_account = config('PARSIAN_LOGIN_ACCOUNT')

    def get_payment_url(self, amount: int):
        data = f"""<?xml version="1.0" encoding="utf-8"?>
        <soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
          <soap12:Body>
            <SalePaymentRequest xmlns="https://pec.Shaparak.ir/NewIPGServices/Sale/SaleService">
                <requestData>
                    <LoginAccount>{self.login_account}</LoginAccount>
                    <OrderId>{amount}</OrderId>
                    <Amount>{amount}</Amount>
                    <CallBackUrl>{self.callback_url}</CallBackUrl>
                </requestData>
            </SalePaymentRequest>
          </soap12:Body>
        </soap12:Envelope>"""

        headers = {
            'Content-Type': 'application/soap+xml; charset=utf-8',
            'SOAPAction': self.soap_action,
        }

        response = requests.post(url=self.url, data=data, headers=headers)

        if response.status_code == 200:
            root = ET.fromstring(response.content)
            ns = {'ns': 'https://pec.Shaparak.ir/NewIPGServices/Sale/SaleService'}
            token_element = root.find('.//ns:Token', namespaces=ns)

            if token_element is not None:

                if not token_element.text == 0:
                    token = token_element.text
                    print('Token:', token)
                    return {'Payment Url': f"https://pec.shaparak.ir/NewIPG/?token={token}"}
            else:
                return (
                    {'error': 'Token not found in the response'}
                )
        print('Response:', response)
        return {'error': 'invalid request'}

pay = Parsian()
pay.get_payment_url(12345)