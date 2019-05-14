from handler_data import handler_data
from regular import handler_line
from get_value import get_v

def create_xml(text2):
    z=handler_line(get_v())
  #  print(z)
    slov = {}
    len_z=len(z)
    for i in range(len_z):
        slov[z[i]] = text2[i].split('\n')
    print(slov)

create_xml(handler_data())