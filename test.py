#First version


sub_name="viscosity"
main_name='transport-model'

text = """./incompressible/viscosityModels/Casson/Casson.H
./incompressible/viscosityModels/Newtonian/Newtonian.H
./incompressible/viscosityModels/BirdCarreau/BirdCarreau.H
./incompressible/viscosityModels/HerschelBulkley/HerschelBulkley.H
./incompressible/viscosityModels/CrossPowerLaw/CrossPowerLaw.H
./incompressible/viscosityModels/powerLaw/powerLaw.H
./incompressible/viscosityModels/strainRateFunction/strainRateFunction.H"""

def handler_data(text,**data):
    flag=True

    message = ''
    text = text.split("\n")
    for line in text:
        line = line.split('/')
        line = line[-1]
        line = line.split('.')[0]
        for i, k in data.items():
            if i == line:
                flag = False
                message = message +'''<{}>\n<name>{}</name>\n<params {}/>\n</{}>\n'''.format(sub_name, line,k, sub_name)
                break
        if flag:

            message = message + '''<{}>{}</{}>\n'''.format(sub_name, line, sub_name)
        flag = True
    message='<{}>\n{}</{}>'.format(main_name,message,main_name)
    return message
#Example
print(handler_data(text=text,Casson='namespace = "std" defaul = "0.0"',HerschelBulkley='check =  "hello"'))