import requests
from bs4 import BeautifulSoup


def check(datasets):
    for dataset in datasets:
        # dataset.split(',')[i]
        # 0:組別 1:學號 2:姓名 3:username 4:repository
        team = dataset.split(',')[0]
        num = dataset.split(',')[1]
        name = dataset.split(',')[2]
        username = dataset.split(',')[3]
        repo = dataset.split(',')[4]
        if (username != ''):
            res = requests.get('https://github.com/{0}/'.format(username))
            if (res.status_code != 404):
                res = requests.get('https://github.com/{0}/{1}/'.format(username,repo))
                if (res.status.code == 404):
                    print ('{0} {1} {2} 這個渾蛋的repo不存在啊?!'.format(team,num,name))
            else:
                print ('{0} {1} {2} 這個渾蛋的username是錯的!'.format(team,num,name))
        #else:
            #print ('{0} {1} {2} 這個渾蛋沒有填username'.format(team,num,name))
        
def getDatasets(gspread):
    res = requests.get(gspread)
    soup = BeautifulSoup(res.text ,'lxml')
    table = soup.find("table", attrs={"class":"waffle"})
    datasets = []
    for row in table.find_all("tr")[2:]:
        dataset = ""
        for td in row.find_all("td"):
            dataset += td.text + ","
        datasets.append(dataset)
    return (datasets)

if __name__ == "__main__":
    datasets = getDatasets('https://docs.google.com/spreadsheets/d/e/2PACX-1vReEn7YC2wFEQxTybKh5Yg2UBg8Uu-fQPPCWKvEJyqxL2AdMNZXayumW4sxw-eYQ36JsB2pgnRlTYN0/pubhtml')
    check(datasets)
