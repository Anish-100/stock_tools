import api
import matplotlib.pyplot as plt



def print_world():
    commodity = api.COMMODITY()
    plot_data = commodity.get_wheat()
    data = plot_data["data"]
   # print('data',data)
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

if __name__ == '__main__':
    print_world()


