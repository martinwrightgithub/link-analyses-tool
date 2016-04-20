#!/usr/bin/python

# -*- coding: latin-1 -*-

page = "http://www.justiceinspectorates.gov.uk/hmic/publications/strategic-policing-requirement-inspection-force-findings/"

import urllib2
html_doc = urllib2.urlopen(page)

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

links = soup.find_all('a')

print page

for link in links:
	if ".pdf" in link.get('href'):
		print link
