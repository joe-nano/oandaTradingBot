import oandapyV20
import oandapyV20.endpoints.transactions as trans

def create_transaction_ID_range_data(start, end):
    return {
        "from": start,
        "to": end
    }

# Get the details of a single Account Transaction
def transaction_details(accountID, token, transactionID):
    client = oandapyV20.API(access_token=token)
    r = trans.TransactionDetails(accountID=accountID, transactionID=transactionID)
    request = client.request(r)
    return request

# Get a range of Transactions for an Account based on Transaction IDs
def transaction_ID_range(accountID, token, start, end):
    params = create_transaction_ID_range_data(start, end)
    client = oandapyV20.API(access_token=token)
    r = trans.TransactionIDRange(accountID=accountID, params=params)
    request = client.request(r)
    return request

# Get a list of Transactions pages that satisfy a time-based Transaction query. 
# Query is optional (in case of no query - all transactions will be returned)
def transaction_list(accountID, token, params=None):
    client = oandapyV20.API(access_token=token)
    if params == None:
        r = trans.TransactionList(accountID)
    else:
        r = trans.TransactionList(accountID, params=params)
    request = client.request(r)
    return request

# Get a stream of Transactions for an Account starting from when the request is made
def transactions_stream(accountID, token):
    client = oandapyV20.API(access_token=token)
    r = trans.TransactionsStream(accountID=accountID)
    request = client.request(r)
    return request
