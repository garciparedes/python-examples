import pandas as pd
from .logic_data_set import LogicDataSet


class DataSets:
    @staticmethod
    def _get_path():
        return "./res"

    @staticmethod
    def get_weber_nominal():
        outLook = pd.Series(["Sunny", "Overcast", "Rain"], dtype="category")
        temp = pd.Series(["Hot", "Mild", "Cold"], dtype="category")
        humidity = pd.Series(["High", "Normal"], dtype="category")
        wind = pd.Series(["Weak", "Strong"], dtype="category")
        playTennis = pd.Series(["Yes", "No"], dtype="category")

        columns = pd.Index(["Outlook", "Temperature", "Humidity", "Wind", "PlayTennis"])

        data = [
            [outLook[0], temp[0], humidity[0], wind[0], playTennis[1]],
            [outLook[0], temp[0], humidity[0], wind[1], playTennis[1]],
            [outLook[1], temp[0], humidity[0], wind[0], playTennis[0]],
            [outLook[2], temp[1], humidity[0], wind[0], playTennis[0]],
            [outLook[2], temp[2], humidity[1], wind[0], playTennis[0]],
            [outLook[2], temp[2], humidity[1], wind[1], playTennis[1]],
            [outLook[1], temp[2], humidity[1], wind[1], playTennis[0]],
            [outLook[0], temp[1], humidity[0], wind[0], playTennis[1]],
            [outLook[0], temp[2], humidity[1], wind[0], playTennis[0]],
            [outLook[2], temp[1], humidity[1], wind[0], playTennis[0]],
            [outLook[0], temp[1], humidity[1], wind[1], playTennis[0]],
            [outLook[1], temp[1], humidity[0], wind[1], playTennis[0]],
            [outLook[1], temp[0], humidity[1], wind[0], playTennis[0]],
            [outLook[2], temp[1], humidity[0], wind[1], playTennis[1]],
        ]

        return pd.DataFrame(data, columns=columns, dtype="category")

    @staticmethod
    def get_weather():
        types = {
            'outlook': 'category',
            'temperature': 'int32', 'humidity': 'int32',
            'windy': 'category', 'play': 'category',
        }

        return pd.read_csv(DataSets._get_path() + '/weather.csv', dtype=types)

    @staticmethod
    def get_weather_semi_nominal():
        types = {
            'Nº': 'int32', 'Outlook': 'category',
            'Temperature': 'int32', 'Humidity': 'category',
            'Wind': 'category', 'PlayTennis': 'category',
        }

        return pd.read_csv(DataSets._get_path() + '/weather_semi_nominal.csv', dtype=types)

    @staticmethod
    def get_car_eval():
        return pd.read_csv(DataSets._get_path() + '/careval.csv')

    @staticmethod
    def get_credit():
        return pd.read_csv(DataSets._get_path() + '/credit.csv')

    @staticmethod
    def get_presion():
        pd_class = pd.Series(["-", "+"], dtype="category")

        columns = pd.Index(["Presion", "Clase"])

        data = [
            40, pd_class[0],
            48, pd_class[0],
            60, pd_class[0],
            72, pd_class[0],
            80, pd_class[0],
            90, pd_class[0],
        ]

        return pd.DataFrame(data, columns=columns)

    @staticmethod
    def generate_from_logic_method(logic_m):
        return LogicDataSet(logic_m)

    @staticmethod
    def get_wiki_vote():
        return pd.read_csv(DataSets._get_path() + '/wiki-Vote.csv')

    @staticmethod
    def get_followers():
        return pd.read_csv(DataSets._get_path() + '/followers.csv')

    @staticmethod
    def get_users():
        return pd.read_csv(DataSets._get_path() + '/users.csv')

    @staticmethod
    def get_thoraric_surgery():
        types = {
            'DGN': 'category', 'PRE4': 'float64', 'PRE5': 'float64', 'PRE6': 'category', 'PRE7': 'category',
            'PRE8': 'category', 'PRE9': 'category', 'PRE10': 'category', 'PRE11': 'category', 'PRE14': 'category',
            'PRE17': 'category', 'PRE19': 'category', 'PRE25': 'category', 'PRE30': 'category', 'PRE32': 'category',
            'AGE': 'int32', 'Risk1Yr': 'category'
        }

        return pd.read_csv(DataSets._get_path() + '/ThoraricSurgery.csv', dtype=types)
