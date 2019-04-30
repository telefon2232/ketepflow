import subprocess
import regular
def handler_data():
  #  z = r"""cd /opt/openfoam-dev/src/transportModels/incompressible/viscosityModels/ && cat powerLaw.C | grep -E "\.lookup" | sed 's%.*lookup("\([^"]*\)".*%\1%g'"""
   # child = subprocess.Popen(z, stdout=subprocess.PIPE, shell=True)
   # output = child.communicate()[0].decode('utf-8')
    line_mas=[]
    text=r'(cd /opt/openfoam-dev/src/transportModels/ && grep -Ril -E "public viscosityModel" | grep -v "lnInclude")'
    child = subprocess.Popen(text, stdout=subprocess.PIPE, shell=True)
    text = child.communicate()[0].decode('utf-8')
    main_mas=[]
    text = text.split("\n")
    line_mas=regular.handler_line(text)
    for line in line_mas:
        z = r"""cd /opt/openfoam-dev/src/transportModels/incompressible/viscosityModels/{}/ && cat {}.C | grep -E "\.lookup" | sed 's%.*lookup("\([^"]*\)".*%\1%g'""".format(line,line)
        child = subprocess.Popen(z, stdout=subprocess.PIPE, shell=True)
        output = child.communicate()[0].decode('utf-8')

        print(output)
        #output=output.replace(r'\n','\n')
        main_mas.append(output)
        print('--------------------------------')
    list_params = []
    message = ''
    for param in main_mas:
        params = param.split('\n')
        for k in params:
            if k != '':
                message = message + '<param name="{}" />\n'.format(k)

        list_params.append(message)
        message = ''
    return line_mas,list_params
for i in handler_data():
    print(i)