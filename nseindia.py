import requests
import json
import pandas as pd
def GetNSEOptionChain (symbol, expiry):
    URL = f"https://www.nseindia.com/api/option-chain-indices?symbol={symbol}"
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0'}
    page=requests.get(URL,headers=headers)
    date=dataset['records']['expiryDates']
    stock_data=dataset['records']['data']
    data=[]
    for x in stock_data:
        if x['expiryDate'] == expiry:
            stock_dict={}
            if 'PE' in x:
                stock_dict['PE_strikePrice']=x['PE']['strikePrice']
                stock_dict['PE_expiryDate']=x['PE']['expiryDate']
                stock_dict['PE_underlying']=x['PE']['underlying']
                stock_dict['PE_identifier']=x['PE']['identifier']
                stock_dict['PE_openInterest']=x['PE']['openInterest']
                stock_dict['PE_changeinOpenInterest']=x['PE']['changeinOpenInterest']
                stock_dict['PE_totalTradedVolume']=x['PE']['totalTradedVolume']
                stock_dict['PE_impliedVolatility']=x['PE']['impliedVolatility']
                stock_dict['PE_bidQty']=x['PE']['bidQty']
                stock_dict['PE_bidprice']=x['PE']['bidprice']
                stock_dict['PE_askQty']=x['PE']['askQty']
                stock_dict['PE_askPrice']=x['PE']['askPrice']
                stock_dict['PE_underlyingValue']=x['PE']['underlyingValue']
            else:
                stock_dict['PE_strikePrice']='-'
                stock_dict['PE_expiryDate']='-'
                stock_dict['PE_underlying']='-'
                stock_dict['PE_identifier']='-'
                stock_dict['PE_openInterest']='-'
                stock_dict['PE_changeinOpenInterest']='-'
                stock_dict['PE_totalTradedVolume']='-'
                stock_dict['PE_impliedVolatility']='-'
                stock_dict['PE_bidQty']='-'
                stock_dict['PE_bidprice']='-'
                stock_dict['PE_askQty']='-'
                stock_dict['PE_askPrice']='-'
                stock_dict['PE_underlyingValue']='-'
            if 'CE' in x:
                stock_dict['CE_strikePrice']=x['CE']['strikePrice']
                stock_dict['CE_expiryDate']=x['CE']['expiryDate']
                stock_dict['CE_underlying']=x['CE']['underlying']
                stock_dict['CE_identifier']=x['CE']['identifier']
                stock_dict['CE_openInterest']=x['CE']['openInterest']
                stock_dict['CE_changeinOpenInterest']=x['CE']['changeinOpenInterest']
                stock_dict['CE_totalTradedVolume']=x['CE']['totalTradedVolume']
                stock_dict['CE_impliedVolatility']=x['CE']['impliedVolatility']
                stock_dict['CE_bidQty']=x['CE']['bidQty']
                stock_dict['CE_bidprice']=x['CE']['bidprice']
                stock_dict['CE_askQty']=x['CE']['askQty']
                stock_dict['CE_askPrice']=x['CE']['askPrice']
                stock_dict['CE_underlyingValue']=x['CE']['underlyingValue']
            else:
                stock_dict['CE_strikePrice']='-'
                stock_dict['CE_expiryDate']='-'
                stock_dict['CE_underlying']='-'
                stock_dict['CE_identifier']='-'
                stock_dict['CE_openInterest']='-'
                stock_dict['CE_changeinOpenInterest']='-'
                stock_dict['CE_totalTradedVolume']='-'
                stock_dict['CE_impliedVolatility']='-'
                stock_dict['CE_bidQty']='-'
                stock_dict['CE_bidprice']='-'
                stock_dict['CE_askQty']='-'
                stock_dict['CE_askPrice']='-'
                stock_dict['CE_underlyingValue']='-'
            data.append(stock_dict)    
    return pd.DataFrame(data)

GetNSEOptionChain('NIFTY','26-Aug-2021')