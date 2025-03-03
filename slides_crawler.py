import sys
import json
import requests
from fpdf import FPDF
from PIL import Image
from io import BytesIO

try:
    with open('config.json', 'r') as f:
        config = json.load(f)
        sessionid = config['sessionid']
        authorization = config['authorization']
        presentation_id = config['presentation_id']
except:
    print('Error: config.json not found or invalid.')
    sys.exit()

headers = {
    'authorization': authorization,
    'cookie'       : f'sessionid={sessionid}',
    'user-agent'   : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}

response = requests.get(f'https://pro.yuketang.cn/api/v3/lesson/presentation/fetch?presentation_id={presentation_id}', headers=headers)
if response.status_code != 200:
    print(f'Error: {response.status_code}')
    sys.exit()
response = response.json()
if response['code'] != 0:
    print(f'Error: {response["message"]}')
    sys.exit()

pdf = FPDF()

slides = response['data']['slides']
for slide in slides:
    response = requests.get(f'{slide['cover']}', headers=headers)
    if response.status_code != 200:
        print(f'Error: {response.status_code}')
        sys.exit()
    img = Image.open(BytesIO(response.content))
    width, height = img.size
    pdf.add_page(format=(width*25.4/72, height*25.4/72))
    pdf.image(BytesIO(response.content), x=0, y=0, w=width*25.4/72, h=height*25.4/72)

pdf.output('slides.pdf')
print('Done.')