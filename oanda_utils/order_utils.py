import oandapyV20
import oandapyV20.endpoints.orders as orders

def create_order_data(enter_price, take_profit_price, stop_price, instrument, quantity, order_type="LIMIT"):
    return {
        "order": {
            "price": '%.2f' % enter_price,
            "stopLossOnFill": {
                "timeInForce": "GTC",
                "price": '%.2f' % stop_price
            },
            "takeProfitOnFill": {
                "timeInForce": "GTC",
                "price": '%.2f' % take_profit_price
            },
            "timeInForce": "GTC",
            "instrument": instrument,
            "units": str(quantity),
            "type": order_type,
            "positionFill": "DEFAULT"
        }
    }

def send_order(accountID, token, enter_price, take_profit_price, stop_price, instrument, quantity, order_type="LIMIT"):
    order_data = create_order_data(enter_price, take_profit_price, stop_price, instrument, quantity, order_type)
    client = oandapyV20.API(access_token=token)
    r = orders.OrderCreate(accountID, data=order_data)
    request = client.request(r)
    return request

def cancel_order(accountID, token, orderID):
    client = oandapyV20.API(access_token=token)
    r = orders.OrderCancel(accountID=accountID, orderID=orderID)
    request = client.request(r)
    return request

def order_details(accountID, token, orderID):
    client = oandapyV20.API(access_token=token)
    r = orders.OrderDetails(accountID=accountID, orderID=orderID)
    request = client.request(r)
    return request

def order_list(accountID, token):
    client = oandapyV20.API(access_token=token)
    r = orders.OrderList(accountID)
    request = client.request(r)
    return request

def replace_order(accountID, token, orderID, enter_price, take_profit_price, stop_price, instrument, quantity, order_type="LIMIT"):
    send_request = send_order(accountID, token, enter_price, take_profit_price, stop_price, instrument, quantity, order_type="LIMIT")
    cancel_request = cancel_order(accountID, token, orderID)
    return [send_request, cancel_request]

def order_pending(accountID, token):
    client = oandapyV20.API(access_token=token)
    r = orders.OrdersPending(accountID)
    request = client.request(r)
    return request