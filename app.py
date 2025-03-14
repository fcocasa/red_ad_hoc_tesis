from flask import Flask, render_template, request, send_from_directory,send_file, session, redirect
from flask import Flask, jsonify, request
from datetime import datetime, timedelta
import os
import re
import random
from time import time

# Inicializo la app
app = Flask(__name__)

def get_random_numbers_from_list(data_list, num_samples):
    """
    Returns a list of `num_samples` random numbers from the given `data_list`.

    Args:
    data_list: The list of numbers to sample from.
    num_samples: The number of random numbers to select.

    Returns:
    A list of `num_samples` random numbers.
    """

    if num_samples > len(data_list):
        raise ValueError("Number of samples cannot exceed the length of the list.")

    return list(set(random.sample(data_list, num_samples)))

def ping2():
    import time
    print('esperando')
    time.sleep(2)
    for x in os.listdir(app.root_path+'/static/ips'):
        os.remove(app.root_path+'/static/ips/'+x)
    nodos_existentes_int = get_random_numbers_from_list(range(1, 255), random.sample(range(5, 10), 1)[0])
    nodos_existentes = [f'192.168.0.{x}' for x in nodos_existentes_int]
    for n in nodos_existentes_int:
        with open(f'{app.root_path}/static/ips/nuc{n}_ips.txt', 'w+') as file:
            for x in get_random_numbers_from_list(nodos_existentes_int, random.choice(range(1, len(nodos_existentes_int) + 1))):
                file.write(f'192.168.0.{x}\n')
    with open(f'{app.root_path}/static/ips/laptop_ips.txt', 'w+') as file:
        for x in get_random_numbers_from_list(nodos_existentes_int, random.choice(range(1, len(nodos_existentes_int) + 1))):
            file.write(f'192.168.0.{x}\n')
    import time
    # print('duermo')
    # time.sleep(10)
    # print('despierto')
            
    ######################################################################
            


    print(os.listdir(app.root_path+'/static/ips'))
    base =''' // Define nodes with fixed positions
    const nodes = new vis.DataSet([
    '''
    connections = {}
    for x in [y for y in os.listdir(app.root_path+'/static/ips') if 'nuc' in y]:
        id_origen = x.split('_')[0].split('c')[1]
        id_origen = re.sub('\n','',id_origen)
        
        connections[id_origen] = []
                        
        base +=  "{ id: "+id_origen+", label: '"+id_origen+"', color: 'lightgray', x: -800+("+id_origen+"%16)*100, y: Math.round("+id_origen+"/16)*50 },\n"

        with open(app.root_path+'/static/ips/'+x,'r') as file:
            for line in file.readlines():
                id = line.split('.')[-1]
                id = re.sub('\n','',id)
                connections[id_origen]=connections[id_origen]+[id]
    
    base +=  "{ id: 0, label: 'Laptop', color: 'lightgray', x: 0, y:  -100},\n"
    connections['0'] = []
    with open(app.root_path+'/static/ips/laptop_ips.txt','r') as file:
        for line in file.readlines():
            id = line.split('.')[-1]
            id = re.sub('\n','',id)
            connections['0']+=[id]

    base += ''']);
    // Define edges with custom colors
    const edges = new vis.DataSet([
    '''
    for id_ori,conns in connections.items():
        for id_dest in conns:
            if id_dest!=id_ori:
                base += "{ from: "+str(id_ori)+", to: "+str(id_dest)+", color: { color: 'green' } },\n"
    
    base += '''
    ]);

    // Create the network
    const container = document.getElementById('mynetwork');
    const data = { nodes, edges };

    // Disable physics to keep positions static
    const options = {
      physics: false,
    };

    const network = new vis.Network(container, data, options);
'''
    return base

def ping():

    ######################################################################
    ################ funcion ficticia ####################################
    for x in os.listdir(app.root_path+'/static/ips'):
        os.remove(app.root_path+'/static/ips/'+x)
    # nodos_existentes_int = get_random_numbers_from_list(range(1,255), random.sample(range(5,10), 1)[0])
    # nodos_existentes = [f'192.168.0.{x}' for x in nodos_existentes_int]
    # for n in nodos_existentes_int:
    #     with open(f'{app.root_path}/static/ips/nuc{n}_ips.txt','w+') as file:
    #         for x in get_random_numbers_from_list(nodos_existentes_int, random.choice(range(1,len(nodos_existentes_int)+1))):
    #             file.write(f'192.168.0.{x}\n')
    # with open(f'{app.root_path}/static/ips/laptop_ips.txt','w+') as file:
    #     for x in get_random_numbers_from_list(nodos_existentes_int, random.choice(range(1,len(nodos_existentes_int)+1))):
    #         file.write(f'192.168.0.{x}\n')
    ######################################################################
    ######################################################################
    
    ######################################################################
    ################ funcion ficticia ####################################
    
    # import time

    # val_hist = str(time.time())
    
    # for file in os.listdir(f"{app.root_path}/static/ips"):
    #     try:
    #         os.mkdir(f"{app.root_path}/static/historico/{file.split('_')[0]}")
    #     except:
    #         pass
    #     os.system(f"cp {app.root_path}/static/ips/{file} {app.root_path}/static/historico/{file.split('_')[0]}/{val_hist}_{file}")
    # print('----------------EJECUTANDO conexion.sh---------------')
    # print(f'bash {app.root_path}/static/conexiones.sh')
    # os.system(f'bash {app.root_path}/static/conexiones.sh')
    # print('----------------FINALIZO conexion.sh---------------')
    import time
    # print('duermo')
    # time.sleep(10)
    # print('despierto')
    
    while 'finalizado.txt' not in os.listdir(f'{app.root_path}/static/ips'):
        print('----------------EESPERANDO---------------')
        time.sleep(0.1)
            
    for arch in [x for x in os.listdir(f'{app.root_path}/static/ips') if 'ip' in x]:
        os.system(f'cp {app.root_path}/static/ips/{arch} {app.root_path}/static/ips/{arch}')
    ######################################################################
            


    print(os.listdir(app.root_path+'/static/ips'))
    base =''' // Define nodes with fixed positions
    const nodes = new vis.DataSet([
    '''
    connections = {}
    for x in [y for y in os.listdir(app.root_path+'/static/ips') if 'nuc' in y]:
        id_origen = x.split('_')[0].split('c')[1]
        id_origen = re.sub('\n','',id_origen)
        
        connections[id_origen] = []
                        
        base +=  "{ id: "+id_origen+", label: '"+id_origen+"', color: 'lightgray', x: -800+("+id_origen+"%16)*100, y: Math.round("+id_origen+"/16)*50 },\n"

        with open(app.root_path+'/static/ips/'+x,'r') as file:
            for line in file.readlines():
                id = line.split('.')[-1]
                id = re.sub('\n','',id)
                connections[id_origen]=connections[id_origen]+[id]
    
    base +=  "{ id: 0, label: 'Laptop', color: 'lightgray', x: 0, y:  -100},\n"
    connections['0'] = []
    with open(app.root_path+'/static/ips/laptop_ips.txt','r') as file:
        for line in file.readlines():
            id = line.split('.')[-1]
            id = re.sub('\n','',id)
            connections['0']+=[id]

    base += ''']);
    // Define edges with custom colors
    const edges = new vis.DataSet([
    '''
    for id_ori,conns in connections.items():
        for id_dest in conns:
            if id_dest!=id_ori:
                base += "{ from: "+str(id_ori)+", to: "+str(id_dest)+", color: { color: 'green' } },\n"
    
    base += '''
    ]);

    // Create the network
    const container = document.getElementById('mynetwork');
    const data = { nodes, edges };

    // Disable physics to keep positions static
    const options = {
      physics: false,
    };

    const network = new vis.Network(container, data, options);
'''
    return base

@app.route('/')
def home():
    return render_template('index.html',base=ping2())

@app.route('/reload')
def reload():
    return ping2(), 200, {'Content-Type': 'text/plain'}


if __name__ == '__main__':
    # from waitress import serve
    # serve(app, host="0.0.0.0", port=5000)
    app.run(host="0.0.0.0", port=5000, debug=True)