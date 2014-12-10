import urllib2
import urllib
import xml.etree.ElementTree as ET

#URL to the XML file
apiPath = "http://www.radioreddit.com/api/status.xml"

#Load the XML into URLLib
xml = urllib.urlopen(apiPath)

#Parse the XML With ET
tree = ET.parse(xml)

root = tree.getroot()

#Print the second element (third item) value. (In status.xml it's listeners)
print root[2].text
