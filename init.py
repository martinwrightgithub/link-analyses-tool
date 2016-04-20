#!/usr/bin/python

# -*- coding: latin-1 -*-

import urllib2
import sitemap
from bs4 import BeautifulSoup

urls = sitemap.urls

for url in urls:

	try: 
		html_doc = urllib2.urlopen(url)

		soup = BeautifulSoup(html_doc, 'html.parser')

		links = soup.find_all('a')

		for link in links:
			if link.get('href') and ".pdf" in link.get('href'):
			
				href = link.get('href');
				onclick = link.get('onclick');
			
				print '"' + str(url) + '","' + str(href) + '","' + str(onclick) + '"'
	except: urllib2.HTTPError