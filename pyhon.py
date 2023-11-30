import requests as req
import re
import json

response = req.get('https://ocistatus.oraclecloud.com/api/v2/components.json')
dict = json.loads(response.text)

for i in dict['regionHealthReports']:
    listaFuncionando = []
    listaNãoFuncionando = []
    if 'Sao Paulo' in i['regionName'] or 'Vinhedo' in i['regionName']:
        for ii in i['serviceHealthReports']:
            if ii['serviceStatus'] != 'NormalPerformance':
                listaNãoFuncionando.append(ii['serviceName'])
            else:
                listaFuncionando.append(ii['serviceName'])
        print(len(listaFuncionando))
        print(len(listaNãoFuncionando))



response = req.get('https://jira-software.status.atlassian.com/')
html = response.text

t = re.compile(r'.*    Operational.*')
check = len(t.findall(html))
errado = 12 - check
print(check)
print(errado)
