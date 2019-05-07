q=['strainRateFunction','Casson','CrossPowerLaw','Newtonian','powerLaw','BirdCarreau','HerschelBulkley']
w=[[''],['m', 'tau0', 'nuMin_', 'nuMax_'],['nu0', 'nuInf', 'm', 'n'],['nu'],['k', 'n', 'nuMin', 'nuMax'],['nu0', 'nuInf', 'k', 'n'],['k', 'n', 'tau0', 'nu0']]
import new_handler
import regular
import get_value
def new_model(q,w):
    mas=[]
    for run in range(len(w)):
        if w[run]==['']:
            mas.append({'name': q[run], 'attrs': []})
            continue
        mas.append({'name':q[run],'attrs':w[run]})



    main={'models':mas}
    main['categories']= [{'name':'viscosity','models':q}]
    main={'transport':main}
    print(main)
new_model(regular.handler_line(get_value.get_v()),new_handler.new_handler())