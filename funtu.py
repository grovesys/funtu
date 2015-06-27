######################################################
# Project: funtu                                     #
# Date Started: 27/06/2015                           #
# Version: 0.1                                       #
# A test version of a "fun hunting you" project      #
# Any use of this code is done so at your own risk!  #
######################################################

import urllib as url # urllib is required to allow us to use .urlopen
targetUrl = "http://www.malware-traffic-analysis.net/blog-entries.html" # Destination to scrape

web_data = url.urlopen(targetUrl)
print web_data.read()
