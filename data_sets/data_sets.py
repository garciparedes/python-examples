import pandas as pd


class DataSets:
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
    def get_car_eval():
        return pd.read_csv('./data_sets/careval.csv')
