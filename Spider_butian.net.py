#!/usr/bin/python
# -*- coding:utf-8 -*-
#Date: 2019/11/8
#Author: Saint Michael

from bs4 import BeautifulSoup
from lxml import etree
import requests
import json



def NumSpide(headers):
	url = 'https://www.butian.net/Reward/pub'
	for i in range(1,176):
		data = {'s':'1','p':str(i)}
		response = requests.post(url=url,data=data,headers=headers)
		re = response.content
		text = json.loads(re)
		for i in range(30):
			url_id = text['data']['list'][i]['company_id']
			urlb = 'https://www.butian.net/Loo/submit?cid='+url_id
			try:
				response = requests.get(url=urlb,headers=headers,timeout=3)
			except:
				continue
			GetSiteTitle(response)
	return


def GetSiteTitle(response):
	soup = BeautifulSoup(response.text, "html.parser")
	title = soup.find('input', 'input-xlarge')["value"]
	url = soup.find('input',{'name':'host'})["value"]
	if 'http' not in url:
		url = 'http://'+url
	WriteSite(title,url)
	return


def WriteSite(title,url):
	content = title+' '+url
	print(content)
	with open('BuTianURL.txt','a') as f:
		f.write(url+'\n')
	return


if __name__ == '__main__':
	headers = {
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0",
		"Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
		"Accept-Encoding":"gzip, deflate",
		"Cookie":"PHPSESSID=d5mu7n1kt80446rqhkqka08h81;"
	}
	NumSpide(headers)
	
