import pandas as pd
from flask import Flask,  request
from flask_cors import CORS
import json

from utilities import  get_total_unique_counts, get_tao_data,clean_up_tao_orders

app = Flask(__name__)
CORS(app)
app.secret_key = "seamless care" # for encrypting the session
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

taoOrders = pd.read_csv('AuthConnectOrders.csv', usecols=['departmentId', 'deptName','clinicalOrderTypeId','orderName','orderingProvider','orderGenus','taoBucket','usedTAO'])
taoOrders.fillna(value={'orderGenus':'None'},inplace=True)
taoOrders['usedTAO'] = taoOrders['usedTAO'].astype(str)
taoOrders = clean_up_tao_orders(taoOrders)



def process_tao_filters(items):
    selected_orders = taoOrders
    first_pass = True
    for item in items['items']:
        if not item['isDisabled']:
            selected_orders = get_tao_data(selected_orders,item['alias'],item['selectedValues'])
        if (first_pass):
            item['dropDownValues']= get_total_unique_counts(taoOrders, item['alias'])
            item['results'] = get_total_unique_counts(taoOrders, item['alias'])
        else:
            item['dropDownValues']= get_total_unique_counts(selected_orders, item['alias']) 
            item['results'] = get_total_unique_counts(selected_orders, item['alias'])
        first_pass=False
    return items



def get_data(request, string):
    data_requested = request[string]
    return data_requested


@app.route('/alloptions', methods=['POST'])
def get_all_options_async():
    items = request.json
    new_items = process_tao_filters(items)
    return json.dumps(new_items), 200



app.run(host='0.0.0.0', port=5001)