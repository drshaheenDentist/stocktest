from flask import Flask
from nsepy import get_history
from datetime import date
import pandas as pd
import numpy as np
import requests
from dateutil.relativedelta import relativedelta
import datetime
import dataframe_image as dfi
import os
import shutil
# os.getcwd()
# directory = os.getcwd() + '\\output'
# os.remove(directory)
# shutil.rmtree(directory)
# os.mkdir(directory)

app = Flask(__name__)


v40_list = ['HDFCBANK',
 'ICICIBANK',
 'KOTAKBANK',
 'HDFC',
 'BAJFINANCE',
 'ICICIGI',
 'HDFCLIFE',
 'BAJAJFINSV',
 'ICICIPRULI',
 'HDFCAMC',
 'NAM_INDIA',
 'PGHH',
 'MARICO',
 'COLPAL',
 'HINDUNILVR',
 'BAJAJHLDNG',
 'DABUR',
 'NESTLEIND',
 'ITC',
 'ASIANPAINT',
 'BERGEPAINT',
 'AKZOINDIA',
 'TITAN',
 'BATAINDIA',
 'PAGEIND',
 'WHIRLPOOL',
 'HAVELLS',
 'TCS',
 'INFY',
 'HCLTECH',
 'ABBOTINDIA',
 'GLAXO',
 'SANOFI',
 'PFIZER',
 'PIDILITIND',
 'GILLETTE',
 'NIFTYBEES',
 'BANKBEES',
 'AXISBANK',
 'BAJAJ_AUTO']
v40_next_list = ['3MINDIA',
 'ASTRAZEN',
 'AVANTIFEED',
 'BAYERCROP',
 'BOSCHLTD',
 'CAPLIPOINT',
 'CERA',
 'DIXON',
 'EICHERMOT',
 'EQUITAS',
 'EQUITASBNK',
 'ERIS',
 'FINCABLES',
 'FINEORG',
 'GODREJCP',
 'HONAUT',
 'ISEC',
 'JCHAC',
 'KANSAINER',
 'LALPATHLAB',
 'MCDOWELL_N',
 'MCX',
 'MOTILALOFS',
 'OFSS',
 'POLYCAB',
 'RADICO',
 'RAJESHEXPO',
 'RELAXO',
 'SFL',
 'SIS',
 'SUNTV',
 'SYMPHONY',
 'TASTYBITE',
 'TEAMLEASE',
 'TTKPRESTIG',
 'UJJIVAN',
 'UJJIVANSFB',
 'VGUARD',
 'VINATIORGA',
 'VIPIND']

v200_list = ['AAVAS',
'ABB',
 'ABBOTINDIA',
 'ABCAPITAL',
 'ACC',
 'AEGISCHEM',
 'AIAENG',
 'AJANTPHARM',
 'AKZOINDIA',
 'ALKEM',
 'ALKYLAMINE',
 'AMARAJABAT',
 'AMBUJACEM',
 'ANDHRAPET',
 'ANGELONE',
 'APARINDS',
 'APLAPOLLO',
 'APLLTD',
 'ASIANPAINT',
 'ASTRAL',
 'ATGL',
 'ATUL',
 'AUBANK',
 'AUROPHARMA',
 'AVANTIFEED',
 'AXISBANK',
 'BAJAJ-AUTO',
 'BAJAJCON',
 'BAJAJFINSV',
 'BAJAJHLDNG',
 'BAJFINANCE',
 'BALAMINES',
 'BALKRISIND',
 'BALRAMCHIN',
 'BANKBARODA',
 'BANKINDIA',
 'BASF',
 'BAYERCROP',
 'BCG',
 'BEL',
 'BEPL',
 'BERGEPAINT',
 'BFINVEST',
 'BSOFT',
 'CAMS',
 'CANBK',
 'CANFINHOME',
 'CAPLIPOINT',
 'CARBORUNIV',
 'CASTROLIND',
 'CDSL',
 'CENTURYPLY',
 'CHOLAFIN',
 'CHOLAHLDNG',
 'CIPLA',
 'CLEAN',
 'COALINDIA',
 'COCHINSHIP',
 'COFORGE',
 'COLPAL',
 'CONSOFINVT',
 'CONSOFINVT',
 'COROMANDEL',
 'CRISIL',
 'CROMPTON',
 'CSBBANK',
 'CUB',
 'CUMMINSIND',
 'CYIENT',
 'DABUR',
 'DCBBANK',
 'DCMSHRIRAM',
 'DEEPAKNTR',
 'DHANUKA',
 'DIVISLAB',
 'DRREDDY',
 'DVL',
 'ECLERX',
 'EDELWEISS',
 'EICHERMOT',
 'EIDPARRY',
 'EMAMILTD',
 'ENDURANCE',
 'EPL',
 'EQUITAS',
 'EQUITASBNK',
 'ERIS',
 'ESCORTS',
 'EXIDEIND',
 'FDC',
 'FEDERALBNK',
 'FINCABLES',
 'FINPIPE',
 'FSL',
 'GAEL',
 'GALAXYSURF',
 'GHCL',
 'GILLETTE',
 'GLAND',
 'GLAXO',
 'GLS',
 'GNFC',
 'GODFRYPHLP',
 'GODREJCP',
 'GPIL',
 'GRANULES',
 'GRINDWELL',
 'GSPL',
 'GUJGASLTD',
 'GULFOILLUB',
 'HAL',
 'HAVELLS',
 'HCLTECH',
 'HDFC',
 'HDFCAMC',
 'HDFCAMC',
 'HDFCBANK',
 'HDFCLIFE',
 'HEIDELBERG',
 'HEROMOTOCO',
 'HFCL',
 'HGS',
 'HIL',
 'HINDUNILVR',
 'HINDZINC',
 'HONAUT',
 'HUDCO',
 'IBULHSGFIN',
 'ICICIBANK',
 'ICICIGI',
 'IDBI',
 'IEX',
 'IGL',
 'IGPL',
 'IIFL',
 'IIFLSEC',
 'IIFLSEC',
 'IIFLWAM',
 'INDIAMART',
 'INDIANB',
 'INDUSINDBK',
 'INEOSSTYRO',
 'INFY',
 'INTELLECT',
 'IOB',
 'IOLCP',
 'IPCALAB',
 'IRCTC',
 'IRFC',
 'ISEC',
 'ITC',
 'J&KBANK',
 'JBCHEPHARM',
 'JINDALPHOT',
 'JINDALPOLY',
 'JMFINANCIL',
 'JPOLYINVST',
 'JSLHISAR',
 'KAJARIACER',
 'KANSAINER',
 'KARURVYSYA',
 'KCP',
 'KEI',
 'KIMS',
 'KIOCL',
 'KIRLFER',
 'KIRLOSIND',
 'KIRLOSIND',
 'KOTAKBANK',
 'KPRMILL',
 'KRBL',
 'KSCL',
 'KSL',
 'KTKBANK',
 'L&TFH',
 'LALPATHLAB',
 'LGBBROSLTD',
 'LICHSGFIN',
 'LINDEINDIA',
 'LTI',
 'LTTS',
 'LUXIND',
 'MAHABANK',
 'MAITHANALL',
 'MANALIPETC',
 'MANAPPURAM',
 'MARICO',
 'MARKSANS',
 'MASTEK',
 'MAZDOCK',
 'METROPOLIS',
 'MFSL',
 'MFSL',
 'MGL',
 'MINDTREE',
 'MOL',
 'MOTILALOFS',
 'MPHASIS',
 'MUTHOOTFIN',
 'NAM-INDIA',
 'NAM-INDIA',
 'NAVINFLUOR',
 'NBCC',
 'NESTLEIND',
 'NMDC',
 'OFSS',
 'ORIENTCEM',
 'PAGEIND',
 'PANAMAPET',
 'PCBL',
 'PERSISTENT',
 'PETRONET',
 'PFC',
 'PFIZER',
 'PGHH',
 'PIDILITIND',
 'PIIND',
 'PNB',
 'PNBGILTS',
 'PNBHOUSING',
 'POLYCAB',
 'POLYPLEX',
 'PRINCEPIPE',
 'RADICO',
 'RATNAMANI',
 'RECLTD',
 'REDINGTON',
 'RELAXO',
 'REPCOHOME',
 'RITES',
 'SANOFI',
 'SBICARD',
 'SBILIFE',
 'SBIN',
 'SCHAEFFLER',
 'SFL',
 'SHARDACROP',
 'SHREECEM',
 'SHRIRAMCIT',
 'SHYAMMETL',
 'SJVN',
 'SKFINDIA',
 'SONACOMS',
 'SONATSOFTW',
 'SOTL',
 'SRF',
 'SRTRANSFIN',
 'SUMICHEM',
 'SUNDARMFIN',
 'SUNDRMFAST',
 'SUNTV',
 'SUPPETRO',
 'SUPRAJIT',
 'SUPREMEIND',
 'SUULD',
 'SUVENPHAR',
 'TANLA',
 'TATAELXSI',
 'TATAMETALI',
 'TCS',
 'TECHM',
 'THYROCARE',
 'TINPLATE',
 'TIRUMALCHM',
 'TRITURBINE',
 'TRIVENI',
 'TTKPRESTIG',
 'UCOBANK',
 'ULTRACEMCO',
 'UNIONBANK',
 'UTIAMC',
 'UTIAMC',
 'VAIBHAVGBL',
 'VENKEYS',
 'VGUARD',
 'VHL',
 'VINATIORGA',
 'VLSFINANCE',
 'VOLTAS',
 'VSTIND',
 'WELCORP',
 'WHIRLPOOL',
 'WIPRO',
 'ZENSARTECH']


def cal_sma(df):
    # create 20 days simple moving average column
    df['20_SMA'] = df['Close'].rolling(window=20, min_periods=1).mean()
    # create 50 days simple moving average column
    df['50_SMA'] = df['Close'].rolling(window=50, min_periods=1).mean()

    df['200_SMA'] = df['Close'].rolling(window=200, min_periods=1).mean()

    return df


# ------------ Fetching History data for list of stock---------
def history_data_with_sma(stock_list, month):
    today = date.today()

    # Start date for data fetch
    start_date = (today - relativedelta(months=month))
    appended_data = []
    # list of stock, for which data is missing
    data_issue_stock_list = []
    # final list of data missing stock
    final_data_issue_list = []
    for i in stock_list:
        print('Fetching data for ---> {}'.format(i))
        try:
            df_data = get_history(symbol=i,
                                  start=start_date,
                                  end=date.today())
            df_data = cal_sma(df_data)
        except:
            data_issue_stock_list.append(i)
            print('Error while fetching data for {}'.format(i))

        appended_data.append(df_data)

    ## re attempt for the stock which has missing data
    for i in data_issue_stock_list:
        print('Fetching data for ---> {}'.format(i))
        try:
            df_data_issue = get_history(symbol=i,
                                        start=start_date,
                                        end=date.today())

            df_data_issue = cal_sma(df_data_issue)
            appended_data.append(df_data_issue)
        except:
            final_data_issue_list.append(i)
            print('Error while fetching data for {}'.format(i))

        # appended_data.append(df_data_issue)

    appended_data = pd.concat(appended_data)

    # filter data for 2 months for further analysis
    data_filter_date = (today - relativedelta(months=2))

    appended_data = appended_data.reset_index()

    data_filtered = appended_data[appended_data['Date'] > data_filter_date]

    return data_filtered


# ---V20 Strategy (Operator food print)
def v20_strategy(df):
    # stock list
    value = df['Symbol'].unique()
    df_append = []

    try:
        for j in value:
            print('Stock name--->{}'.format(j))
            df_select = df[df['Symbol'] == j]
            # creating Candle type(Gren/Red) based on Open and CLose Price
            df_select['candleType'] = np.where(df_select['Close'] > df_select['Open'], 'Green', 'Red')
            # Assigning Open Price for series (to have percentage change of that series)
            df_select['open_series'] = np.where(df_select['candleType'] != (df_select['candleType'].shift()),
                                                df_select['Open'], 0)
            # filling same open price across the series
            df_select['open_series'] = df_select['open_series'].replace(to_replace=0, method='ffill')
            # Calculating Price change percentage for the series
            df_select['percent_change_series'] = ((df_select['High'] - df_select['open_series']) / df_select[
                'open_series']) * 100
            # filter for Green Candle only
            df_select['final_flag'] = np.where(
                (df_select['candleType'] == 'Green') & (df_select['percent_change_series'] >= 20), 'select', 'unselect')
            # filtering the condition meet case
            df_select = df_select[df_select['final_flag'] == 'select']
            df_select = df_select.reset_index()
            df_append.append(df_select)

        final_selected_list = pd.concat(df_append)
        # selecting first records for selected series
        final_selected_list_date = final_selected_list.groupby('Symbol').first()
        final_selected_list_date = final_selected_list_date.reset_index()
        # result with selected columns
        final_selected_list_date = final_selected_list_date[['Symbol', 'Date', 'percent_change_series']]

    except:
        print("No List")
        final_selected_list_date = pd.DataFrame()
    return final_selected_list_date


# --------SMA Strategy based on 200 , 50, 20 ------
def sma_strategy(df):
    df['sma_strategy'] = np.where(
        (df['200_SMA'] > df['50_SMA']) & (df['200_SMA'] > df['20_SMA']) & (df['50_SMA'] > df['20_SMA']) & (
                    df['20_SMA'] > df['Close']), 'Selected_by_sma', 'Not Selected')
    df2 = df.groupby(['Symbol'])['sma_strategy'].agg(list).apply(lambda x: x[-1]).reset_index()
    df2 = df2.rename(columns={'sma_strategy': 'current_status'})
    df = df[df['sma_strategy'] == 'Selected_by_sma'].reset_index()
    df = df[['Symbol', 'Date', '200_SMA', '50_SMA', '20_SMA', 'Close', 'sma_strategy']].groupby('Symbol').first()

    df = df.reset_index()
    df3 = pd.merge(df, df2, on="Symbol", how='left')
    return df3


@app.route('/')
def hello_world():
    directory = os.getcwd() + '\\output'
    shutil.rmtree(directory)
    os.mkdir(directory)
    #---Strategy  for V40
    V40_sma_startegy_list = sma_strategy(history_data_with_sma(v40_list,12))
    print('Done-1')
    V40_v20_strategy_list = v20_strategy(history_data_with_sma(v40_list,12))
    print('V40 Done')


    #---Strategy  for V40 Next
    V40_next_v20_strategy_list = v20_strategy(history_data_with_sma(v40_next_list,12))
    print('V40 Next Done')

    #---Strategy  for V200
    V200_v20_strategy_list = v20_strategy(history_data_with_sma(v200_list,12))

    #####---- DataFrame to Picture-------
    #@@@@@ V40
    V40_sma_startegy_list = V40_sma_startegy_list.sort_values('Date', ascending = False , ignore_index = False)
    print('Done-2')
    df_styled = V40_sma_startegy_list.style.background_gradient()
    print('Done-3')
    dfi.export(df_styled,(directory + '\\' +"SMA-V40.png"))
    print('Done-4')

    V40_v20_strategy_list = V40_v20_strategy_list.sort_values('Date', ascending = False , ignore_index = True)
    df_styled = V40_v20_strategy_list.style.background_gradient()
    dfi.export(df_styled,(directory + '\\' +"BigBluePrint-V40.png"))

    #@@@@ V40 Next
    V40_next_v20_strategy_list = V40_next_v20_strategy_list.sort_values('Date', ascending = False , ignore_index = True)
    df_styled = V40_next_v20_strategy_list.style.background_gradient()
    dfi.export(df_styled,(directory + '\\' +"BigBluePrint-V40Next.png"))

    #@@@@ V200
    V200_v20_strategy_list = V200_v20_strategy_list.sort_values('Date', ascending = False , ignore_index = True)
    df_styled = V200_v20_strategy_list.style.background_gradient()
    dfi.export(df_styled,(directory + '\\' +"BigBluePrint-V200.png"))


    pic_list = ['SMA-V40' , 'BigBluePrint-V40' , 'BigBluePrint-V40Next' , 'BigBluePrint-V200']
    today_fileSave = datetime.datetime.now().strftime("%d-%m")
    for i in pic_list:
        files = {'photo' : open(directory + '\\' + i + '.png','rb')}
        resp =requests.post('https://api.telegram.org/bot5398734255:AAGaHbxU4DnD5MZ0cFApon9cKxDEhE54oL8/sendPhoto?chat_id=1918031531&caption={}_{}'.format(i,today_fileSave),files=files)
        print(resp.status_code)

if __name__ == "__main__":
    app.run(debug= True)
