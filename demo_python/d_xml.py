import xml.etree.ElementTree as ET


tree = ET.parse('country_data.xml')
root = tree.getroot()

for child in root:
    print child.tag, child.attrib
    for c_child in child:
        print c_child.tag, c_child.attrib, c_child.text
       
c = root.find("./country/rank")
print type(c),c,c.text
