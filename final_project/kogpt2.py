import requests
import json


r = requests.post(
    #'https://train-vj1d5bkiit2sb1x2g6s8-gpt2-train-teachable-ainize.endpoint.ainize.ai/predictions/gpt-2-ko-small-finetune', #가장 초기 엑셀
    #'https://train-6bh1yyyxev9xvphzuibp-gpt2-train-teachable-ainize.endpoint.ainize.ai/predictions/gpt-2-ko-small-finetune', #잡다한거까지 나옴
    #'https://train-nqhy6iii8xyt5739th8f-gpt2-train-teachable-ainize.endpoint.ainize.ai/predictions/gpt-2-ko-small-finetune', #기업설명, 슬로건
    'https://train-yf2rrqjish0iiaionifu-gpt2-train-teachable-ainize.endpoint.ainize.ai/predictions/gpt-2-ko-small-finetune', #슬로건만 있는 api
    headers = {'Content-Type' : 'application/json'
               },
    data=json.dumps({
  "text": "샴푸",
  "num_samples": 20,
  "length": 15
    }))

#print(r.json())
for i in r.json():
    print(i)
    print('='*30)