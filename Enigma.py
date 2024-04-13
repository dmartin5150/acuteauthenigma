import pandas as pd

from utilities import get_tao_order_counts, get_total_unique_counts, get_tao_data


taoOrders = pd.read_csv('AuthConnectOrders.csv', usecols=['departmentId', 'deptName','clinicalOrderTypeId','orderName','orderingProvider','orderGenus','taoBucket','usedTAO'])
taoOrders.fillna(value={'orderGenus':'None'},inplace=True)


def given_tao():
    selected_tao_orders = get_tao_data(taoOrders,'usedTAO',[13624])
    departments_count, departments_unique = get_total_unique_counts(selected_tao_orders,'departmentId')
    genus_count, genus_unique = get_total_unique_counts(selected_tao_orders, 'orderGenus')
    order_count, order_unique = get_total_unique_counts(selected_tao_orders, 'orderName')
    bucket_count,bucket_unique = get_total_unique_counts(selected_tao_orders, 'taoBucket')
    provider_count, provider_unique = get_total_unique_counts(selected_tao_orders, 'orderingProvider')
    counts = {'departments': departments_count, 'genus':genus_count, 'orders':order_count,'bucket':bucket_count,'provider':provider_count}
    unique = {'departments': departments_unique, 'genus':genus_unique, 'orders':order_unique,'bucket':bucket_unique,'provider':provider_unique}
    return counts, unique


given_tao()

