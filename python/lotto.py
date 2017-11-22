import hangul
import json
import csv
from urllib.request import urlopen

f = open('lotto.csv', mode='w', encoding='utf-8', newline=None)
fw = csv.writer(f)

drwNo = 1
while True:
    # print(drwNo)
    lotto_json = urlopen("http://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo="+str(drwNo)).read().decode('utf-8')
    lotto = json.loads(lotto_json)
    # print(type(lotto),json.dumps(lotto, ensure_ascii=False, indent=4, sort_keys=False))
    if "drwNo" in lotto:
        print("({:0>3}) {} : {} {} {} {} {} {} ({}) : ₩ {:,} / {}명".format(lotto["drwNo"], lotto["drwNoDate"], lotto["drwtNo1"], lotto["drwtNo2"], lotto["drwtNo3"], lotto["drwtNo4"], lotto["drwtNo5"], lotto["drwtNo6"], lotto["bnusNo"], lotto["firstWinamnt"], lotto["firstPrzwnerCo"]))
        fw.writerow([lotto["drwNo"], lotto["drwNoDate"], lotto["drwtNo1"], lotto["drwtNo2"], lotto["drwtNo3"], lotto["drwtNo4"], lotto["drwtNo5"], lotto["drwtNo6"], lotto["bnusNo"], lotto["firstWinamnt"], lotto["firstPrzwnerCo"]])
        drwNo += 1
    else:
        break

f.close()
