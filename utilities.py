def get_tao_order_counts(taoOrders):
    return taoOrders.value_counts('usedTAO')

def get_total_unique_counts(taoOrders, columnName):
    orderCount = taoOrders.value_counts(columnName)
    counts = list(orderCount.items())
    # counts = [[val, idx] for idx, val in orderCount.items()]
    # print(counts)
    orderUnique = orderCount.nunique()
    # print('unique', orderUnique)
    return counts, orderUnique

def get_tao_data(taoOrders, columnName, selection):
    orders = taoOrders[taoOrders[columnName].isin(selection)]
    return orders





