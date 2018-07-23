import oandapyV20
import oandapyV20.endpoints.positions as positions

# Returns json specifying which positoins should be closed
def create_position_close_data(longUnits=0, shortUnits=0):
    if longUnits == 0:
        return {
            "shortUnits": str(shortUnits)
        }
    else:
        return {
            "longUnits": str(longUnits)
        }

# Returns list of all open positions
def open_positions(accountID, token):
    client = oandapyV20.API(access_token=token)
    r = positions.OpenPositions(accountID=accountID)
    request = client.request(r)
    return request

# Closes specified positions
def close_positions(accountID, token, instrument, units_type, quantity):
    if units_type == "short":
        data = create_position_close_data(shortUnits=quantity)
    elif units_type == "long":
        data = create_position_close_data(longUnits=quantity)
    else:
        return None
    client = oandapyV20.API(access_token=token)
    r = positions.PositionClose(accountID=accountID,
                                instrument=instrument,
                                data=data)
    request = client.request(r)
    return request

# Returns details on all positions on the given instruments
def positions_details(accountID, token, instrument):
    client = oandapyV20.API(access_token=token)
    r = positions.PositionDetails(accountID=accountID, instrument=instrument)
    request = client.request(r)
    return request

# Returns list of all (open/closed) positions on all instruments
def position_list(accountID, token):
    client = oandapyV20.API(access_token=token)
    r = positions.PositionList(accountID=accountID)
    request = client.request(r)
    return request