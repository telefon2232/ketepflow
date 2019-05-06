z={'strainRateFunction': [''], 'Casson': ['m', 'tau0', 'nuMin_', 'nuMax_'], 'CrossPowerLaw': ['nu0', 'nuInf', 'm', 'n'], 'Newtonian': ['nu'], 'powerLaw': ['k', 'n', 'nuMin', 'nuMax'], 'BirdCarreau': ['nu0', 'nuInf', 'k', 'n'], 'HerschelBulkley': ['k', 'n', 'tau0', 'nu0']}
for key in z.keys():
   #z[key]=[{'name':'z[key]','attrs':'z.get[key]'}]
   # print(z[key])
   pass
#w={'transport':z}
#print(z)
doc={}
q=['strainRateFunction','Casson','CrossPowerLaw','Newtonian','powerLaw','BirdCarreau','HerschelBulkley']
w=[[''],['m', 'tau0', 'nuMin_', 'nuMax_'],['nu0', 'nuInf', 'm', 'n'],['nu'],['k', 'n', 'nuMin', 'nuMax'],['nu0', 'nuInf', 'k', 'n'],['k', 'n', 'tau0', 'nu0']]
mas=[]
for run in range(len(q)):
    mas.append({'name':q[run],'attrs':w[run]})



main={'models':mas}
main['categories']= [{'name':'viscosity','models':q}]
main={'transport':main}
print(main)