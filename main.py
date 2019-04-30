import bs4



import xml.etree.ElementTree as ET
text="""./incompressible/viscosityModels/Casson/Casson.H
./incompressible/viscosityModels/Newtonian/Newtonian.H
./incompressible/viscosityModels/BirdCarreau/BirdCarreau.H
./incompressible/viscosityModels/HerschelBulkley/HerschelBulkley.H
./incompressible/viscosityModels/CrossPowerLaw/CrossPowerLaw.H
./incompressible/viscosityModels/powerLaw/powerLaw.H
./incompressible/viscosityModels/strainRateFunction/strainRateFunction.H"""
name=input("Enter name")
message=''
root = ET.Element(name)



text=text.split("\n")
for line in text:
    line=line.split('/')
    line=line[-1]
    line=line.split('.')[0]
    ET.SubElement(root, "viscosity").text = line
  #  ET.SubElement(root, "viscosity").text = line
    print(line)
tree = ET.ElementTree(root)

#kek=ElementTree.tostring(tree)
#print(kek)
#print(new_text)

tree.write("filename.xml",method="xml")