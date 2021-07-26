import requests
import json


r = requests.post(
    #'https://train-vj1d5bkiit2sb1x2g6s8-gpt2-train-teachable-ainize.endpoint.ainize.ai/predictions/gpt-2-ko-small-finetune', #가장 초기 엑셀
    #'https://train-6bh1yyyxev9xvphzuibp-gpt2-train-teachable-ainize.endpoint.ainize.ai/predictions/gpt-2-ko-small-finetune', #잡다한거까지 나옴
    'https://train-nqhy6iii8xyt5739th8f-gpt2-train-teachable-ainize.endpoint.ainize.ai/predictions/gpt-2-ko-small-finetune', #기업설명, 슬로건
    #'https://train-yf2rrqjish0iiaionifu-gpt2-train-teachable-ainize.endpoint.ainize.ai/predictions/gpt-2-ko-small-finetune', #슬로건만 있는 api
    headers = {'Content-Type' : 'application/json'
               },
    data=json.dumps({
  "text": "리니지, rpg 게임",
  "num_samples": 20,
  "length": 20
    }))

#print(r.json())
for slogan in r.json():
    slogan = slogan.split('\n')[0]
    #print(slogan, end=' / ')
    slogan = slogan.split(',')[2:]
    slogan = ', '.join(slogan)
    if slogan :
        print(slogan)
        print('='*30)

"""
음료, 시원한 - 컴마가 없이 발 이어짐
리니지, rpg 게임 - 컴마 있음 (컴마가 '리니지, rpg 게임, 다시, 시작' 이런 식으로 나오기 때문에 마지막 pop 말고 if 문으로 컴마 개수 세기) 
"""