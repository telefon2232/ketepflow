import json
from handler_data import handler_data
from regular import handler_line
from get_value import get_v
#print(handler_data())
text=['m\ntau0\nnuMin_\nnuMax_\n', 'nu\n', '        BirdCarreauCoeffs_.lookupOrDefault\nnu0\nnuInf\nk\nn\n a_ = BirdCarreauCoeffs_.lookupOrDefault\n', 'k\nn\ntau0\nnu0\n', 'nu0\nnuInf\nm\nn\n', 'k\nn\nnuMin\nnuMax\n', '']
text2="""./incompressible/viscosityModels/Casson/Casson.H
./incompressible/viscosityModels/Newtonian/Newtonian.H
./incompressible/viscosityModels/BirdCarreau/BirdCarreau.H
./incompressible/viscosityModels/HerschelBulkley/HerschelBulkley.H
./incompressible/viscosityModels/CrossPowerLaw/CrossPowerLaw.H
./incompressible/viscosityModels/powerLaw/powerLaw.H
./incompressible/viscosityModels/strainRateFunction/strainRateFunction.H"""

def create_xml(text,text2):
    z=get_v()
    print(z)
    slov = {}
    for i in range(len(z)):
        slov[z[i]] = text[i].split('\n')
    print(slov)

create_xml(get_v(),handler_data())