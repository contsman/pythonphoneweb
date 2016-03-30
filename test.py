#!/usr/bin/python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
p = open('C:/Users/Administrator/Desktop/test.html')

soup = BeautifulSoup(p.read(),'html5lib')
print(soup.meta)
print(soup.meta.get('content'))
print(soup.meta.get('http-equiv'))

def test(username,password):
    print('select * from users where username = "%s" and password = "%s"' % (username,password))

if __name__ == '__main__':
    test('wangtiecai1','wangtiecai1')