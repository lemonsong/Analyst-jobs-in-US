#!/usr/local/bin/python
# coding: utf-8
# import the libraries we will be using
import urllib2,os,re,sys

# make a new browser
browser=urllib2.build_opener()
browser.addheaders=[('User-agent', 'Mozilla/5.0')]

fileindeed=open('indeedcounts.txt','w')

states=['New+York','California']
count=0
for a in ['New+York','California']:
    fileopen=open('skillsets.txt')
    fileindeed.write(a + '\n') 
    for line in fileopen:
        line = line.strip()
        url = "http://www.indeed.com/jobs?q=" + str(line) + "+analysis&l=" + str(a)
        print url
        try:
            response=browser.open(url)
        except urllib2.HTTPError:  # handling exotic HTTP errors
            continue
        myHTML=response.read()
        counts = re.findall('div id=\"searchCount\">Jobs 1 to \d+ of ([0-9,]+)</div>',myHTML) # get counts

        #write into file
        fileindeed.write('{"name": "'+ str(line) + '", "counts": ' + str(counts[0]) + '},' + '\n') 
    fileopen.close()            

               