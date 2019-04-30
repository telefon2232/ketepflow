import xml.etree.ElementTree as xml
import subprocess
from handler_data import handler_data
from regular import handler_line
print(handler_data())



def create_xml(line,params):
    text = r'(cd /opt/openfoam-dev/src/transportModels/ && grep -Ril -E "public viscosityModel" | grep -v "lnInclude")'
    child = subprocess.Popen(text, stdout=subprocess.PIPE, shell=True)
    text = child.communicate()[0].decode('utf-8')
    root = xml.Element("transport-model")
    for i in range(len(handler_line(text))):

        sub_root=xml.SubElement(root,"viscosity")
        sub_param=xml.SubElement(sub_root,handler_data()[i])
    return xml.ElementTree(root)