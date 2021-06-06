import pandas
import matplotlib.pyplot as plt
import random


def box_plot(data, labels=None, title=None):
    plt.boxplot(data, labels=labels)
    plt.title(title)
    plt.show()
    plt.clf()


def compare_attributes(data, attr_names):
    no_class = len(pandas.unique(data['class']))
    cl = data['class'].map({'L': 0, 'B': 1, 'R': 2})
    disp = 0.15
    fig, axs = plt.subplots(2, 3, figsize=(10, 7))
    # fig.tight_layout()
    plt.subplots_adjust(left=0.03, bottom=0.04, right=0.98,
                        top=0.91, wspace=0.165, hspace=0.185)
    k, h = 0, 0
    for i in range(1, len(attr_names)):
        for j in range(i+1, len(attr_names)):
            g1 = data[attr_names[i]]
            g2 = data[attr_names[j]]
            x = [i*random.uniform(1-(disp/i), 1+(disp/i)) for i in g1]
            y = [i*random.uniform(1-(disp/i), 1+(disp/i))for i in g2]
            axs[k, h].scatter(
                x=x, y=y, c=cl, cmap=plt.cm.get_cmap('brg', no_class), s=10)
            axs[k, h].set_title('{}-{}'.format(attr_names[i], attr_names[j]))
            # axs[i-1,j-1].colorbar(ticks=range(no_class))
            # axs[i-1,j-1].xlabel(attr_names[i])
            # axs[i-1,j-1].ylabel(attr_names[j])
            h = (h+1) % 3
            if h % 3 == 0:
                k += 1

    # axs[-1,-1].colorbar(ticks=range(no_class))
    fig.suptitle('Attributes')
    plt.show()
    plt.clf()

def aggregated(data, attr_names):
    no_class = len(pandas.unique(data['class']))
    cl = data['class'].map({'L': 0, 'B': 1, 'R': 2})
    X = []
    Y = []
    for index, row in data.iterrows():
        a = row[attr_names[1]]+row[attr_names[2]]
        b = row[attr_names[3]]+row[attr_names[4]]
        X.append(a)
        Y.append(b)

    plt.scatter(x=X, y=Y, c=cl, cmap=plt.cm.get_cmap('brg', no_class), s=10)
    plt.title('')
    plt.xlabel('{} + {}'.format(attr_names[1],attr_names[2]))
    plt.ylabel('{} + {}'.format(attr_names[3],attr_names[4]))
    plt.show()


def read_data():
    file_name = 'balance-scale.data'
    '''
    Attribute Information:
    1. Class Name: 3 (L, B, R)
    2. Left-Weight: 5 (1, 2, 3, 4, 5)
    3. Left-Distance: 5 (1, 2, 3, 4, 5)
    4. Right-Weight: 5 (1, 2, 3, 4, 5)
    5. Right-Distance: 5 (1, 2, 3, 4, 5)
    '''
    attributes = ['class', 'LW', 'LD', 'RW', 'RD']
    data = pandas.read_csv(file_name, names=attributes)
    #print(data)
    # print(type(data))
    l, b, r = 0, 0, 0
    for i in data['class']:
        if i == 'L':
            l += 1
        if i == 'R':
            r += 1
        if i == 'B':
            b += 1
    print(l, b, r)
    #x = data.columns.values.tolist()

    return data,attributes



data,attributes = read_data()
aggregated(data, attributes)
compare_attributes(data, attributes)
box_plot(data=[data[i] for i in attributes[1:]],
            labels=attributes[1:], title='box plot of balance-scale dataset')
