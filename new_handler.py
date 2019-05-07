import get_value
import regular
import subprocess

def new_handler():
    line_mas=(regular.handler_line(get_value.get_v()))
    main_mas=[]
    g_mas=[]
    for line in line_mas:
        z = r"""cd /opt/openfoam-dev/src/transportModels/incompressible/viscosityModels/{}/ && cat {}.C | grep -E "\.lookup" | sed 's%.*lookup("\([^"]*\)".*%\1%g'""".format(
            line, line)
        child = subprocess.Popen(z, stdout=subprocess.PIPE, shell=True)
        output = child.communicate()[0].decode('utf-8')

        #  print(output)
        #if output!='':
        main_mas.append(output)
    for i in main_mas:
        i=i.split('\n')
        if i[-1]=='':
            i=i[:-1]
        g_mas.append(i)
       # print(i)
   # print(g_mas)
    return g_mas



#['', 'm\ntau0\nnuMin_\nnuMax_\n', 'nu0\nnuInf\nm\nn\n', 'nu\n', 'k\nn\nnuMin\nnuMax\n', '        BirdCarreauCoeffs_.lookupOrDefault\nnu0\nnuInf\nk\nn\n    a_ = BirdCarreauCoeffs_.lookupOrDefault\n', 'k\nn\ntau0\nnu0\n']
