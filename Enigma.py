import pandas as pd
from flask import Flask, flash, request, redirect, render_template, send_from_directory,abort
from flask_cors import CORS
import json

from utilities import get_tao_order_counts, get_total_unique_counts, get_tao_data,clean_up_tao_orders

app = Flask(__name__)
CORS(app)
app.secret_key = "seamless care" # for encrypting the session
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

taoOrders = pd.read_csv('AuthConnectOrders.csv', usecols=['departmentId', 'deptName','clinicalOrderTypeId','orderName','orderingProvider','orderGenus','taoBucket','usedTAO'])
taoOrders.fillna(value={'orderGenus':'None'},inplace=True)
taoOrders = clean_up_tao_orders(taoOrders)


def process_tao_filters(items):
    selected_orders = taoOrders
    for item in items['items']:
        if not item['isDisabled']:
            selected_orders = get_tao_data(selected_orders,item['alias'],item['results'])
        item['selectedValues'] = get_total_unique_counts(selected_orders, item['alias'])
    return items



# def given_tao():
#     selected_tao_orders = get_tao_data(taoOrders,'usedTAO',[255])
    # departments_count, departments_unique = get_total_unique_counts(selected_tao_orders,'departmentId')
    # genus_count, genus_unique = get_total_unique_counts(selected_tao_orders, 'orderGenus')
    # order_count, order_unique = get_total_unique_counts(selected_tao_orders, 'orderName')
    # bucket_count,bucket_unique = get_total_unique_counts(selected_tao_orders, 'taoBucket')
    # provider_count, provider_unique = get_total_unique_counts(selected_tao_orders, 'orderingProvider')
    # counts = {'departments': departments_count, 'genus':genus_count, 'orders':order_count,'bucket':bucket_count,'provider':provider_count}
    # unique = {'departments': departments_unique, 'genus':genus_unique, 'orders':order_unique,'bucket':bucket_unique,'provider':provider_unique}
    # return counts, unique


# counts, unique = given_tao()

# print(counts['bucket'])

def get_data(request, string):
    data_requested = request[string]
    return data_requested


@app.route('/alloptions', methods=['POST'])
def get_all_options_async():
    items = request.json
    new_items = process_tao_filters(items)
    return json.dumps(new_items), 200



app.run(host='0.0.0.0', port=5001)