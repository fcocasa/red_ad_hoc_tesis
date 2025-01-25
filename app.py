from flask import Flask, render_template, request, send_from_directory,send_file, session, redirect
from flask import Flask, jsonify, request
from datetime import datetime, timedelta
import os
import re

app = Flask(__name__)

import random

import random

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


def ping():
    for x in os.listdir('static/ips'):
        os.remove(app.root_path+'/static/ips/'+x)
    nodos_existentes_int = get_random_numbers_from_list(range(1,255), random.sample(range(5,10), 1)[0])
    nodos_existentes = [f'192.168.0.{x}' for x in nodos_existentes_int]
    for n in nodos_existentes_int:
        with open(f'{app.root_path}/static/ips/nuc_{n}.txt','w+') as file:
            for x in get_random_numbers_from_list(nodos_existentes_int, random.choice(range(1,len(nodos_existentes_int)+1))):
                file.write(f'192.168.0.{x}\n')
    with open(f'{app.root_path}/static/ips/laptop.txt','w+') as file:
        for x in get_random_numbers_from_list(nodos_existentes_int, random.choice(range(1,len(nodos_existentes_int)+1))):
            file.write(f'192.168.0.{x}\n')

    print(os.listdir(app.root_path+'/static/ips'))
    base =''' // Define nodes with fixed positions
    const nodes = new vis.DataSet([
    '''
   
    connections = {}
    for x in [y for y in os.listdir(app.root_path+'/static/ips') if 'nuc' in y]:
        id_origen = x.split('_')[1].split('.')[0]
        id_origen = re.sub('\n','',id_origen)
        
        connections[id_origen] = []
                        
        base +=  "{ id: "+id_origen+", label: '"+id_origen+"', color: 'lightgray', x: -400+("+id_origen+"%16)*100, y: Math.round("+id_origen+"/16)*50 },\n"

        with open(app.root_path+'/static/ips/'+x,'r') as file:
            for line in file.readlines():
                id = line.split('.')[-1]
                id = re.sub('\n','',id)
                connections[id_origen]+=[id]
    
    base +=  "{ id: 0, label: 'Laptop', color: 'lightgray', x: 0, y:  -100},\n"
    connections['0'] = []
    with open(app.root_path+'/static/ips/laptop.txt','r') as file:
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
    # with open(app.root_path+'/templates/base_index.html','r') as file,open(app.root_path+'/templates/index.html','w+') as index,open('algo.js','w+') as algo:
    #     index.write(re.sub('script_re',base,file.read()))
    #     algo.write(base)
    
    return render_template('index.html',base=ping())

@app.route('/reload')
def reload():
    return ping(), 200, {'Content-Type': 'text/plain'}


if __name__ == '__main__':
    # from waitress import serve
    # serve(app, host="0.0.0.0", port=5000)
    app.run(host="0.0.0.0", port=5000, debug=True)