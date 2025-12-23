import api
import matplotlib.pyplot as plt



def print_wheat():
    '''Just a test function that gets the value of wheat and plots it over time'''
    commodity = api.COMMODITY()
    plot_data = commodity.get_wheat()
    data = plot_data["data"]
    value_dict = {}
    print('data',data)
    for element in reversed(data):
        print(element)
        if(element['value'] == '.'):
            pass
        else:
            value_dict [element['date'][2:4]] = float(element['value'])
    fig,ax = plt.subplots()


    ax.plot(list(value_dict.keys()),list(value_dict.values()))
    plt.xlabel('Dates')
    plt.ylabel('Price in $')
    plt.ylim(0, None)
    plt.title('Price in $ of a metric ton of wheat')
    plt.grid(True,alpha=0.5)
    plt.xticks(rotation=45, ha='right')
    plt.show()


def plot_data(time_data,symbol)->None:
    x_list = []
    for element in time_data:
        x_list.append(element[:-3])
    plt.plot(x_list,list(time_data.values()))
    plt.xlabel('Dates')
    plt.ylabel('Value Over Time')
    plt.ylim(0, None)
    plt.title(f'Price of {symbol} over time' )
    plt.grid(True,alpha=0.5)
    plt.xticks(rotation=45, ha='right')
    plt.show()


def stock_value(symbol):
    stock = api.STOCK()
    stock_data = stock.get_data(symbol)
    print('STOCK')
    get_meta_data(stock_data)
    time_data = print_stock_data(stock_data)
    plot_data(time_data,symbol)

def get_meta_data(stock_data : 'json') -> None:
    '''Prints all the initial info based on the stock data'''
    meta_data = stock_data['Meta Data']
    print('Ticker is',meta_data['2. Symbol'])
    print('Last Refreshed',meta_data['3. Last Refreshed'])
    print('Time Zone',meta_data['4. Time Zone'])

def print_stock_data(stock_data:'json')-> 'json':
    time_series_data = stock_data['Monthly Adjusted Time Series']
    date_dict = {}
    for date in reversed(time_series_data):
        data = time_series_data[date]
        avg = float(data['5. adjusted close'])
        date_dict[date] = avg
    return date_dict



def run_loop():
    symbol = input('Please enter a symbol which you want data of: ')
    stock_value(symbol)

if __name__ == '__main__':
    run_loop()


