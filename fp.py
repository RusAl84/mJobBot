import json

def fp(login='rusal', getpdn='passport'):

    fileObject = open("data.json", "r")
    jsonContent = fileObject.read()
    ListOfItem = json.loads(jsonContent)
    result=''
    for item in ListOfItem:
        if str(item['login']).lower()==str(login).lower():
            result=item['data'][getpdn]
    print(result)
    return str(result)

if __name__ == '__main__':
    ip1 = '10.1.1.1'