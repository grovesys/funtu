######################################################
# Project: funtu                                     #
# Date Started: 27/06/2015                           #
# Version: 0.1                                       #
# A test version of a "fun hunting you" project      #
# Any use of this code is done so at your own risk!  #
######################################################

from lxml import html
import requests
targetUrl = "http://www.malware-traffic-analysis.net/blog-entries.html" #Destination location

page = requests.get(targetUrl) #Request the URL specified in the targetURL
fullPage = html.fromstring(page.text) #Return the full source of the page

date = fullPage.xpath('//a[@class="list_header"]/text()') #This will create the list of all the entries in list_header from the html returned
subject = fullPage.xpath('//a[@class="main_menu"]/text()') ## This will create the list of all the entries in main_menu from the html returned

print "Date: ", date[7] # Return number 8 in the list
print "Subject: ", subject[7] # Return number 8 in the list
