import json
from handler_data import handler_data
from regular import handler_line
from get_value import get_v

def create_xml(text,text2):
    z=handler_line(get_v())
  #  print(z)
    slov = {}
    for i in range(len(z)):
        slov[z[i]] = text2[i].split('\n')
    print(slov)

create_xml(get_v(),handler_data())