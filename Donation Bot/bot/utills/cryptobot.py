

import uuid
import os
import httpx
from dotenv import load_dotenv

load_dotenv()


def testnet_check():
    if bool(os.getenv("CRYPTOBOT_TESTNET")):
        cryptobot_url = "https://testnet-pay.crypt.bot"
    else:
        cryptobot_url = "https://pay.crypt.bot"
    return cryptobot_url

async def request(data, method: str):
    cryptobot_headers = {'Crypto-Pay-API-Token': os.getenv("CRYPTOBOT_TOKEN")}
    url = testnet_check()
    cryptobot_url = f"{url}/api/{method}"
    async with httpx.AsyncClient() as client:
        cryptobot_response = await client.post(url=cryptobot_url,
                                               headers=cryptobot_headers,
                                               data=data)
    json = cryptobot_response.json()
    return json


async def create_invoice(price: float):
    data = {
        'amount': price,
        'asset': os.getenv("CRYPTOBOT_CURRENCY"),
        'description': "ID: " + str(uuid.uuid4()),
        'allow_comments': False,
        'allow_anonymous': False,
        'expires_in': 900
    }
    r = await request(data=data, method='createInvoice')
    url, invoice_id = r["result"]['pay_url'], r["result"]['invoice_id']
    return url, invoice_id

async def get_status(invoice_id: int):
    r = await request(data=f'invoice_ids: {invoice_id}', method='getInvoices')
    status = r['result']['items'][0]['status']
    if status == 'paid':
        return True
    else:
        return False


async def getexchange():
    r = await request(data='', method='getExchangeRates')
    for item in r['result']:
        if item['source'] == os.getenv("CRYPTOBOT_CURRENCY"):
            if item['target'] == 'RUB':
                return f'{float(item['rate']):g}'


