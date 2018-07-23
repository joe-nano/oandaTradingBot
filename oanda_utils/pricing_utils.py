import oandapyV20
import oandapyV20.endpoints.pricing as pricing

def create_parameters(instruments):
    instruments = ','.join(map(str, instruments))
    return {
        "instruments": instruments
    }

# Get pricing information for a specified list of Instruments within an account
def pricing_info(accountID, token, instruments):
    params = create_parameters(instruments)
    client = oandapyV20.API(access_token=token)
    r = pricing.PricingInfo(accountID=accountID, params=params)
    request = client.request(r)
    return request

# Get realtime pricing information for a specified list of Instruments
def pricing_stream(accountID, token, instruments):
    params = create_parameters(instruments)
    client = oandapyV20.API(access_token=token)
    r = pricing.PricingStream(accountID=accountID, params=params)
    request = client.request(r)
    return request