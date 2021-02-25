import pandas as pd
import os



data_path = './wiki.csv'
data = pd.read_csv(data_path)
user = data['user_id'].unique()
# def gererate_data():
data_user = data[data['user_id'] == user[0]].sort_values('time').copy()
u_time = data_user['time'].values
u_seq = data_user['item_id'].values
split_point = len(u_seq) - 1
print('\ndata_user:\n', data_user)
print('\nu_time:\n', u_time)
print('\nu_seq:\n', u_seq)
print('\nsplit_point:\n', split_point)
# mkdir(train_path)
# mkdir(test_path)


def mkdir(path):
    path = path.rstrip('/')
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        return
    else:
        return