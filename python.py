import requests as req
import re
import json
from flask import Flask, jsonify
 
def get_oracle_services_data():
    response = req.get('https://ocistatus.oraclecloud.com/api/v2/components.json')
    dict = json.loads(response.text)
 
    services=[]
    servers=[]
    for i in dict['regionHealthReports']:
        oracleWorkingList = []
        oracleNotWorkingList = []
        if 'Sao Paulo' in i['regionName'] or 'Vinhedo' in i['regionName']:
            for ii in i['serviceHealthReports']:
                if ii['serviceStatus'] != 'NormalPerformance':
                    oracleNotWorkingList.append(ii['serviceName'])
                else:
                    oracleWorkingList.append(ii['serviceName'])
           
            servers.append({'Local':i['regionName'],'Status':{'working': oracleWorkingList,'unavailable':oracleNotWorkingList}})
    services.append({'Name':'Oracle','servers':servers})
 
    response = req.get('https://jira-software.status.atlassian.com/api/v2/summary.json')
    data = response.json()
    jiraWorkingList = []
    jiraNotWorkingList = []
    for i in data['components']:
        servers=[]
        if i['status'] == 'operational':
            jiraWorkingList.append(i['name'])
        else:
            jiraNotWorkingList.append(i['name'])
    servers.append({'Local':data['page']['name'],'Status':{'working': jiraWorkingList,'unavailable':jiraNotWorkingList}})        
    services.append({'Name':data['page']['name'],'servers':servers})
 
    return jsonify(services)