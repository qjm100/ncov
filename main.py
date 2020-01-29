#_*_utf:8_*_
import requests
import json
class search:
    def __init__():
        pass
    def searchA (b):
        d = search.searchC(url='https://myapi.ihogu.com/public/?s=Whfy.city',a=b)
        f = d['data']
        b = f['items']
        return b[0]
    def searchB ():
        d = search.searchC(url='https://myapi.ihogu.com/public/?s=Whfy.count',a=None)
        f = d['data']
        b = f['items']
        return b[0]
    def searchC (url,a):
        r = requests.get(url,params=a)
        jr = r.content.decode()
        dic = json.loads(jr)
        return dic

if __name__ == '__main__':
    a=search.searchB()
    while (1):
        print ("2019-ncov\n时间",a["create_time"])
        print (a["country"])
        print ("确诊人数",a["confirm"])
        print ("疑似",a["suspect"])
        print ("死亡",a["dead"])
        z = int(input ("搜1省，2市"))
        if z == 1:
            c = input("什么省")
            b = {
                    'area':c
                }
            d = search.searchA(b)
            print ("------------------------------------------\n",c)
            print ("时间",d["create_time"])
            print ("确诊人数",d["confirm"])
            print ("疑似",d["suspect"])
            print ("死亡",d["dead"])
        if z == 2:
            c = input("什么市")
            b = {'city':c}
            d = search.searchA(b)
            print ("------------------------------------------\n",c)
            print ("时间",d["create_time"])
            print ("确诊人数",d["confirm"])
            print ("疑似",d["suspect"])
            print ("死亡",d["dead"])
        input ("按任意键继续\n--------------------------------------")
        break




