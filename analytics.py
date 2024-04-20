import pandas as pd


taoOrders = pd.read_csv('AuthConnectOrders.csv', usecols=['departmentId', 'deptName','clinicalOrderTypeId','orderName','orderingProvider','orderGenus','taoBucket','usedTAO','documentId'])
current_status = pd.read_csv('FLJAC_Submitted.csv')
print(current_status.shape[0])
taoOrders.drop_duplicates(subset=['documentId'],inplace=True)
current_status['order id'] = pd.to_numeric(current_status['order id'])
current_status.rename(columns={'order id':'documentId'}, inplace=True)




combined = taoOrders.set_index('documentId').join(other=current_status.set_index('documentId'))
combined.fillna(value={'order status':'NOT MATCHED'}, inplace=True)
submitted=combined[combined['order status'] == 'SUBMITTED']
submitted.to_csv('submitted.csv')
not_matched = combined[combined['order status'] == 'NOT MATCHED']
submit = combined[combined['order status'] == 'SUBMIT']
combined.to_csv('combined.csv')
not_matched.to_csv('not_matched.csv')
submit.to_csv('submit.csv')
# print(combined['order status'].value_counts)
