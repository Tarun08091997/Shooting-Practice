import json
from constants import  *

con = constant()





### highscore is no of target shot


# load data from json file

def load_data():
     with open('Files/saves.json') as f:
        data = json.load(f)
        return data

# save data in Json file if there is no file it makes one

def save_data(data_list):

    with open('Files/saves.json', 'w') as json_file:
        json.dump(data_list, json_file)
    pass


def check_data(no_of_shots, time, game_type):
    data_list = load_data()

    if game_type == 1:
        data = data_list[0]
        if no_of_shots > data['highscore'] or (no_of_shots == data['highscore'] and time < data['time']):
            data_easy = {'highscore': no_of_shots,
                     'time': time
                     }
            data_list[0] = data_easy
            save_data(data_list)
            return True
        else:
            return False


    if game_type == 2:
        data = data_list[1]
        if no_of_shots > data['highscore'] or (no_of_shots == data['highscore'] and time < data['time']):
            data_medium = {'highscore': no_of_shots,
                         'time': time
                         }
            data_list[1] = data_medium
            save_data(data_list)
            return True
        else:
            return False

    if game_type == 3:
        data = data_list[2]
        if no_of_shots > data['highscore'] or (no_of_shots == data['highscore'] and time < data['time']):
            data_hard = {'highscore': no_of_shots,
                         'time': time
                         }
            data_list[2] = data_hard
            save_data(data_list)
            return True
        else:
            return False


def max_noOfshot(a):
    datalist = load_data()
    datalist[3] = a
    save_data(datalist)
    pass


def reset_data():
    data = {'highscore': 0,
            'time': 0.0
            }
    list = con.datalist
    list[0] = data
    list[1] = data
    list[2] = data
    list[3] = 50

    save_data(list)



######## get data of max shoot everytime from list

con.datalist = load_data()
con.no_of_targets = int(con.datalist[3])