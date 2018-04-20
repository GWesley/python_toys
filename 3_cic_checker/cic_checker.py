import requests
import json
import urllib.parse as urlparse
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import time

from selenium import webdriver

headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8'}

def start_checker():
    with open('/Users/gwesley/Projects/config.cic.json', 'r') as f:
        session = requests.Session()
        session.headers.update(headers)
        req_id = get_req_id(session)
        print("=== Get req_id : "+req_id)
        #登录
        account = json.loads(f.read()).get('account')
        parmas = {"token1":account.get("name"),"token2":account.get("password")}
        url = "https://clegc-gckey.gc.ca/j/eng/gckey_login?ReqID="+req_id
        r = session.post(url, data=parmas)
        print("===登录 Sign In")
        # print(r.text)
        url = get_form_action(r, 'form')
        time.sleep(3)
        print("===继续 "+ url)

        r = session.post(url)
        time.sleep(3)

        url = get_form_action(r, 'form')
        r = session.post(url)
        #同意
        time.sleep(3)
        print(r.text)
        #答题

        #点进详情

def get_req_id(session):
    r = session.get("https://onlineservices-servicesenligne-cic.fjgc-gccf.gc.ca/mycic/gccf?lang=eng&idp=gckey&svc=/mycic/start")
    query = urlparse.urlparse(r.url).query
    req_id = urlparse.parse_qs(query)['ReqID'][0]
    return req_id

def get_form_action(r,form_id):
    bsObj = BeautifulSoup(r.text,"html.parser")
    action = bsObj.find('form',id=form_id).get('action')
    if('http' not in action):
        return urljoin(r.url,action)
    else: 
        return action

start_checker()



