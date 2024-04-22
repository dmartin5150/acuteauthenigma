def get_tao_order_counts(taoOrders):
    return taoOrders.value_counts('usedTAO')


def remove_comments(orderName):
     return orderName.split('-')[0]

def clean_up_tao_orders(taoOrders):
        taoOrders['orderName'] = taoOrders['orderName'].apply(lambda x: remove_comments(x))
        return taoOrders

def get_total_unique_counts(taoOrders, columnName):
    orderCount = taoOrders.value_counts(columnName)
    counts = [{'name': idx, 'count': val} for idx, val in orderCount.items()]
    return counts

def get_tao_data(taoOrders, columnName, selection):
    orders = taoOrders
    if len(selection) != 0:
        orders = taoOrders[taoOrders[columnName].isin(selection)]
    return orders





