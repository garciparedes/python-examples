from numerical.data_science.res import DataSets


def discretize_AGE(value):
    if value <= 62:
        return 'AGE_1'
    elif 62 < value <= 65:
        return 'AGE_3'
    elif 65 < value <= 70:
        return 'AGE_2'
    else:
        return 'AGE_4'

def discretize_PRE4(value):
    if value <= 2.66:
        return 'PRE4_1'
    elif 2.66 < value <= 2.88:
        return 'PRE4_2'
    else:
        return 'PRE4_3'


def discretize_PRE5(value):
    if value <= 2.05:
        return 'PRE5_1'
    else:
        return 'PRE5_2'



if __name__ == '__main__':
    pd_data = DataSets.get_thoraric_surgery()

    pd_data['PRE4'] = pd_data['PRE4'].apply(discretize_PRE4,1).astype('category')
    pd_data['PRE5'] = pd_data['PRE5'].apply(discretize_PRE5,1).astype('category')
    pd_data['AGE'] = pd_data['AGE'].apply(discretize_AGE,1).astype('category')

    print(pd_data)
    pd_data.to_csv('ThoraricSurgery_discrete.csv', index=False)
