import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


N = 100000
inter_arrival_time = {
    '1': 0,
    '2': 0,
    '3': 0,
    '4': 0,
    '6': 0,
    '8': 0
}

service_time = {
    '1': 0,
    '2': 0,
}


def get_dict_sum_and_mean(d):
    s = 0
    for k, v in d.items():
        val = int(k) * v
        s += val
    return s, s / N


iat_list = []
for i in range(N):
    # Calculating inter-arrival
    r = np.random.rand()
    iat_list.append(r)
    if r < 0.1:
        inter_arrival_time['1'] += 1
    elif r < 0.4:
        inter_arrival_time['2'] += 1
    elif r < 0.5:
        inter_arrival_time['3'] += 1
    elif r < 0.7:
        inter_arrival_time['4'] += 1
    elif r < 0.9:
        inter_arrival_time['6'] += 1
    else:
        inter_arrival_time['8'] += 1

    s = np.random.rand()
    # Calculating service time
    if s < 0.6:
        service_time['1'] += 1
    else:
        service_time['2'] += 1

data = pd.DataFrame({
    'cat': ['one', 'two', 'three', 'four', 'six', 'eight'],
    'val': list(inter_arrival_time.values()),
})
print(data)
print(inter_arrival_time)
iat_sum, iat_mean = get_dict_sum_and_mean(inter_arrival_time)
print('inter-arrival time mean = {}'.format(iat_mean))

print(service_time)
st_sum, st_mean = get_dict_sum_and_mean(service_time)
print('service time mean = {}'.format(st_mean))

print(
    'Estimated Server Utilization = {:.2f}%'.format((st_mean / iat_mean) * 100)
)

# viz
flatui = ['#9b59b6', '#3498db', '#95a5a6', '#e74c3c', '#34495e', '#2ecc71']
ax = sns.barplot(
    x='cat', y='val',
    data=data,
    palette=sns.color_palette(flatui),
)
ax.set(xlabel='Inter-arrival time (N = {:,})'.format(N), ylabel='Frequency')
plt.show()
