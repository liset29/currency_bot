import xml.etree.ElementTree as ET
import requests
import config as con
from app.database import r

CBR_URL = con.BANK_URL


def get_data():
    response = requests.get(CBR_URL)
    response.raise_for_status()
    return response.text


def parse_update_data(xml_data):
    data = ET.fromstring(xml_data)
    for i in data.findall('Valute'):
        char_code = i.find('CharCode').text
        value = i.find('Value').text.replace(',', '.')
        print(char_code, value)

        r.set(name=char_code, value=value)


def update_data():
    xml_data = get_data()
    parse_update_data(xml_data)
