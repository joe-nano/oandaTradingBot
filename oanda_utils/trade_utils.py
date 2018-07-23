import oandapyV20
import oandapyV20.endpoints.trades as trades

def create_trade_close_data(units):
    return {
        "units": str(units)
    }

def create_trade_list_parameters(instruments):
    instruments = ','.join(map(str, instruments))
    return {
        "instruments": instruments
    }

# Get the list of open Trades for an Account
def open_trades(accountID, token):
    client = oandapyV20.API(access_token=token)
    r = trades.OpenTrades(accountID=accountID)
    request = client.request(r)
    return request

# Close (partially or fully) a specific open Trade in an Account
def close_trade(accountID, token, tradeID, units):
    data = create_trade_close_data(units)
        
    client = oandapyV20.API(access_token=token)
    r = trades.TradeClose(accountID=accountID, tradeID=tradeID, data=data)
    request = client.request(r)
    return request

# Get the details of a specific Trade in an Account
def trade_details(accountID, token, tradeID):
    client = oandapyV20.API(access_token=token)
    r = trades.TradeDetails(accountID=accountID, tradeID=tradeID)
    request = client.request(r)
    return request

# Get a list of trades for an Account
def trades_list(accountID, token, instruments):
    params = create_trade_list_parameters(instruments)
    client = oandapyV20.API(access_token=token)
    r = trades.TradesList(accountID=accountID, params=params)
    request = client.request(r)
    return request
