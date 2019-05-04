import subprocess
import regular
from get_value import get_v
def handler_data():

  #  line_mas=[]

    text=get_v()
    main_mas=[]
    line_mas=regular.handler_line(text)
    for line in line_mas:
        z = r"""cd /opt/openfoam-dev/src/transportModels/incompressible/viscosityModels/{}/ && cat {}.C | grep -E "\.lookup" | sed 's%.*lookup("\([^"]*\)".*%\1%g'""".format(line,line)
        child = subprocess.Popen(z, stdout=subprocess.PIPE, shell=True)
        output = child.communicate()[0].decode('utf-8')

      #  print(output)
        main_mas.append(output)
        print('--------------------------------')
    list_params = []
    message = ''
    for param in main_mas:
        params = param.split('\n')
        for k in params:
            if k != '':
                message = message + '{}\n'.format(k)

        list_params.append(message)
        message = ''
    print(list_params)
    return list_params
#for i in handler_data():
 #   print(i)