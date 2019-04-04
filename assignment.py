#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 17:42:11 2019

@author: manzars
"""
import requests
from bs4 import BeautifulSoup
import pandas
base = "https://vdw.de/en/the-vdw/members-directory/#A"
req = requests.get(base)
soup = BeautifulSoup(req.text, 'lxml')
div = soup.findAll('div', {'class': 'wpb_wrapper'})
k = 0
file = open('assignment.csv', 'w')
header = 'Company Name, Email, Telephone, Website\n'
file.write(header)
for element in div:
    if(1 < k < 25):
        p = element.findAll('p')
        for ele in p:
            name, email, telephone, website = '', '', '', ''
            name = ele.strong.text
            #print(name)
            
            try:
                email = ele.a.attrs['href'].split('mailto:')[1]
                #print(email)
            except:
                email = ele.a.attrs['href']
                #print(email)
                
            telephone = ele.contents[-7].replace('Tel.', '').replace('Telefon:', '').replace('Tel:', '').replace('\n', '')
            if( 'Fax' in telephone):
                telephone = ele.contents[-9].replace('Tel.', '').replace('Telefon:', '').replace('Tel:', '').replace('\n', '')
            print(telephone)
            
            website = ele.contents[-1].attrs['href']
            #print(website)
            file.write(name.replace(',', '') + ',' + email.replace(',', '') + ',' + telephone.replace(',', '') + ',' + website.replace(',', '') + '\n')
    k+=1
file.close()

file = pandas.read_csv('assignment.csv')