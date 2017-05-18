#!/home/hostmachine/parser-dnipro/bin/python3.5
#  -*- coding: utf-8 -*-
import urllib.request
import pandas as pd
from spyre import server
import datetime
import os
import fileinput
import pickle
import time
import subprocess


class SpyreServer(server.App):
    title = "Днепропетровская область"
    inputs = [{
              "type": "dropdown",
              "label": "Начальное значение годового диапазона",
              "options": [
                  {"label": "Не выбрано", "value": ""},
                  {"label": "1981", "value": 1981},
                  {"label": "1982", "value": 1982},
                  {"label": "1983", "value": 1983},
                  {"label": "1984", "value": 1984},
                  {"label": "1985", "value": 1985},
                  {"label": "1986", "value": 1986},
                  {"label": "1987", "value": 1987},
                  {"label": "1988", "value": 1988},
                  {"label": "1989", "value": 1989},
                  {"label": "1990", "value": 1990},
                  {"label": "1991", "value": 1991},
                  {"label": "1992", "value": 1992},
                  {"label": "1993", "value": 1993},
                  {"label": "1994", "value": 1994},
                  {"label": "1995", "value": 1995},
                  {"label": "1996", "value": 1996},
                  {"label": "1997", "value": 1997},
                  {"label": "1998", "value": 1998},
                  {"label": "1999", "value": 1999},
                  {"label": "2000", "value": 2000},
                  {"label": "2001", "value": 2001},
                  {"label": "2002", "value": 2002},
                  {"label": "2003", "value": 2003},
                  {"label": "2004", "value": 2004},
                  {"label": "2005", "value": 2005},
                  {"label": "2006", "value": 2006},
                  {"label": "2007", "value": 2007},
                  {"label": "2008", "value": 2008},
                  {"label": "2009", "value": 2009},
                  {"label": "2010", "value": 2010},
                  {"label": "2011", "value": 2011},
                  {"label": "2012", "value": 2012},
                  {"label": "2013", "value": 2013},
                  {"label": "2014", "value": 2014},
                  {"label": "2015", "value": 2015},
                  {"label": "2016", "value": 2016},
                  {"label": "2017", "value": 2017}
              ],
              "key": "year_begin",
              "action_id": "update_data"
              },
              {
              "type": "dropdown",
              "label": "Конечное значение годового диапазона",
              "options": [
                  {"label": "Не выбрано", "value": ""},
                  {"label": "1981", "value": 1981},
                  {"label": "1982", "value": 1982},
                  {"label": "1983", "value": 1983},
                  {"label": "1984", "value": 1984},
                  {"label": "1985", "value": 1985},
                  {"label": "1986", "value": 1986},
                  {"label": "1987", "value": 1987},
                  {"label": "1988", "value": 1988},
                  {"label": "1989", "value": 1989},
                  {"label": "1990", "value": 1990},
                  {"label": "1991", "value": 1991},
                  {"label": "1992", "value": 1992},
                  {"label": "1993", "value": 1993},
                  {"label": "1994", "value": 1994},
                  {"label": "1995", "value": 1995},
                  {"label": "1996", "value": 1996},
                  {"label": "1997", "value": 1997},
                  {"label": "1998", "value": 1998},
                  {"label": "1999", "value": 1999},
                  {"label": "2000", "value": 2000},
                  {"label": "2001", "value": 2001},
                  {"label": "2002", "value": 2002},
                  {"label": "2003", "value": 2003},
                  {"label": "2004", "value": 2004},
                  {"label": "2005", "value": 2005},
                  {"label": "2006", "value": 2006},
                  {"label": "2007", "value": 2007},
                  {"label": "2008", "value": 2008},
                  {"label": "2009", "value": 2009},
                  {"label": "2010", "value": 2010},
                  {"label": "2011", "value": 2011},
                  {"label": "2012", "value": 2012},
                  {"label": "2013", "value": 2013},
                  {"label": "2014", "value": 2014},
                  {"label": "2015", "value": 2015},
                  {"label": "2016", "value": 2016},
                  {"label": "2017", "value": 2017}
              ],
              "key": "year_end",
              "action_id": "update_data"
              },
              {
              "type": "dropdown",
              "label": "Нумерация недель",
              "options": [
                  {"label": "Не выбрано", "value": ''},
                  {"label": "1", "value": 1},
                  {"label": "2", "value": 2},
                  {"label": "3", "value": 3},
                  {"label": "4", "value": 4},
                  {"label": "5", "value": 5},
                  {"label": "6", "value": 6},
                  {"label": "7", "value": 7},
                  {"label": "8", "value": 8},
                  {"label": "9", "value": 9},
                  {"label": "10", "value": 10},
                  {"label": "11", "value": 11},
                  {"label": "12", "value": 12},
                  {"label": "13", "value": 13},
                  {"label": "14", "value": 14},
                  {"label": "15", "value": 15},
                  {"label": "16", "value": 16},
                  {"label": "17", "value": 17},
                  {"label": "18", "value": 18},
                  {"label": "19", "value": 19},
                  {"label": "20", "value": 20},
                  {"label": "21", "value": 21},
                  {"label": "22", "value": 22},
                  {"label": "23", "value": 23},
                  {"label": "24", "value": 24},
                  {"label": "25", "value": 25},
                  {"label": "26", "value": 26},
                  {"label": "27", "value": 27},
                  {"label": "28", "value": 28},
                  {"label": "29", "value": 29},
                  {"label": "30", "value": 30},
                  {"label": "31", "value": 31},
                  {"label": "32", "value": 32},
                  {"label": "33", "value": 33},
                  {"label": "34", "value": 34},
                  {"label": "35", "value": 35},
                  {"label": "36", "value": 36},
                  {"label": "37", "value": 37},
                  {"label": "38", "value": 38},
                  {"label": "39", "value": 39},
                  {"label": "40", "value": 40},
                  {"label": "41", "value": 41},
                  {"label": "42", "value": 42},
                  {"label": "43", "value": 43},
                  {"label": "44", "value": 44},
                  {"label": "45", "value": 45},
                  {"label": "46", "value": 46},
                  {"label": "47", "value": 47},
                  {"label": "48", "value": 48},
                  {"label": "49", "value": 49},
                  {"label": "50", "value": 50},
                  {"label": "51", "value": 51},
                  {"label": "52", "value": 52}
              ],
              "key": "weeks",
              "action_id": "update_data"
              },
              {
              "type": "checkboxgroup",
              "label": "Поиск экстремумов индекса VHI",
              "options": [
                      {"label": "MAX - значение", "value": "max"},
                      {"label": "MIN - значение", "value": "min"}],
              "key": "vhi_extremum",
              "action_id": "update_data",
              },
              {
              "type": "dropdown",
              "label": "Соотношение вегетационного индекса",
              "options": [
                  {"label": "Не выбрано", "value": ""},
                  {"label": "Благоприятные условия", "value": 60},
                  {"label": "Стрессовые условия", "value": 40},
                  {"label": "Интенсивность засухи от средней до чрезвычайной", "value": 15},
                  {"label": "Интенсивность засухи от умеренной до чрезвычайной", "value": 35}
              ],
              "key": "vhi_correlation",
              "action_id": "update_data"
              },
              {
              "type": "dropdown",
              "label": "Экстремальные засухи, что коснулись больше указанного процента области",
              "options": [
                  {"label": "Не выбрано", "value": ""},
                  {"label": "0%", "value": "0"},
                  {"label": "5%", "value": "5"},
                  {"label": "10%", "value": "10"},
                  {"label": "15%", "value": "15"},
                  {"label": "20%", "value": "20"},
                  {"label": "25%", "value": "25"},
                  {"label": "30%", "value": "30"},
                  {"label": "35%", "value": "35"},
                  {"label": "40%", "value": "40"},
                  {"label": "45%", "value": "45"},
                  {"label": "50%", "value": "50"},
                  {"label": "55%", "value": "55"},
                  {"label": "60%", "value": "60"},
                  {"label": "65%", "value": "65"},
                  {"label": "70%", "value": "70"},
                  {"label": "75%", "value": "75"},
                  {"label": "80%", "value": "80"},
                  {"label": "85%", "value": "85"},
                  {"label": "90%", "value": "90"},
                  {"label": "95%", "value": "95"},
                  {"label": "100%", "value": "100"}
              ],
              "key": "vhi_rate",
              "action_id": "update_data"
              },
              {
              "type": "dropdown",
              "label": "Умеренные засухи, что коснулись больше указанного процента области",
              "options": [
                  {"label": "Не выбрано", "value": ""},
                  {"label": "0%", "value": "0"},
                  {"label": "5%", "value": "5"},
                  {"label": "10%", "value": "10"},
                  {"label": "15%", "value": "15"},
                  {"label": "20%", "value": "20"},
                  {"label": "25%", "value": "25"},
                  {"label": "30%", "value": "30"},
                  {"label": "35%", "value": "35"},
                  {"label": "40%", "value": "40"},
                  {"label": "45%", "value": "45"},
                  {"label": "50%", "value": "50"},
                  {"label": "55%", "value": "55"},
                  {"label": "60%", "value": "60"},
                  {"label": "65%", "value": "65"},
                  {"label": "70%", "value": "70"},
                  {"label": "75%", "value": "75"},
                  {"label": "80%", "value": "80"},
                  {"label": "85%", "value": "85"},
                  {"label": "90%", "value": "90"},
                  {"label": "95%", "value": "95"},
                  {"label": "100%", "value": "100"}
              ],
              "key": "vhi_mild",
              "action_id": "update_data"
              },
              ]
    controls = [{
                "type": "hidden",
                "id": "update_data",
                },
                {
                "type": "hidden",
                "id": "update_data",
                },
                {
                "type": "hidden",
                "id": "update_data",
                },
                {
                "type": "hidden",
                "id": "update_data",
                },
                {
                "type": "hidden",
                "id": "update_data",
                },
                {
                "type": "hidden",
                "id": "update_data",
                },
                {
                "type": "hidden",
                "id": "update_data",
                }
                ]
    tabs = ["Table", "VHI-индексы", "TCI-индексы", "VCI-индексы"]
    outputs = [
        {
            "type": "table",
            "id": "table_id",
            "control_id": 'update_data',
            "tab": "Table",
            "on_page_load": True
        },
        {
            "type": "plot",
            "id": "vhi_plot",
            "control_id": "update_data",
            "tab": "VHI-индексы",
            "on_page_load": True
        },
        {
            "type": "plot",
            "id": "tci_plot",
            "control_id": "update_data",
            "tab": "TCI-индексы",
            "on_page_load": True
        },
        {
            "type": "plot",
            "id": "vci_plot",
            "control_id": "update_data",
            "tab": "VCI-индексы",
            "on_page_load": True
        }
    ]

    def vhi_data_parsing(self, fname):
        url = urllib.request.urlopen('https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_provinceData.php?country=UKR&provinceID=5&year1=1981&year2=2017&type=Mean')
        parsed_data = url.read()
        with open(fname, 'wb') as data:
            data.write(parsed_data)
        while True:
            try:
                with fileinput.FileInput(fname, inplace=True) as file:
                    for line in file:
                        print(line.replace(', provinceID,', '').replace('  ', ',').replace(' ', ',').replace(',,', ',').replace(',', ', ').replace('</pre></tt>', ''), end='')
                return False
            except ValueError:
                time.sleep(0.7)
                with fileinput.FileInput(fname, inplace=True) as file:
                    for line in file:
                        print(line.replace(', provinceID,', '').replace('  ', ',').replace(' ', ',').replace(',,', ',').replace(',', ', ').replace('</pre></tt>', ''), end='')
                return False

    def vh_data_parsing(self, fname):
        url = urllib.request.urlopen('https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_provinceData.php?country=UKR&provinceID=5&year1=1981&year2=2017&type=VHI_Parea')
        parsed_data = url.read()
        with open(fname, 'wb') as data:
            data.write(parsed_data)
        while True:
            try:
                with fileinput.FileInput(fname, inplace=True) as file:
                    for line in file:
                        print(line.replace(', provinceID,', '').replace('  ', ',').replace(' ', ',').replace(',,', ',').replace(',', ', ').replace('</pre></tt>', ''), end='')
                return False
            except ValueError:
                time.sleep(0.7)
                with fileinput.FileInput(fname, inplace=True) as file:
                    for line in file:
                        print(line.replace(', provinceID,', '').replace('  ', ',').replace(' ', ',').replace(',,', ',').replace(',', ', ').replace('</pre></tt>', ''), end='')
                return False

    def vhi_filename_creation(self):
        global serial_data
        serial_data = {}
        serial_filepath = os.path.abspath('filenames.pickle')
        curr_date = str(datetime.datetime.now())[0:10]
        full_date = str(datetime.datetime.now()).replace(' ', '-')[:-7]

        while True:
            try:
                with open(serial_filepath, 'rb') as d:
                    serial_data = pickle.load(d)
                    break
            except FileNotFoundError:
                open(serial_filepath, 'wb').close()
                continue
            except EOFError:
                serial_data = {}
                break

        date = serial_data.get(curr_date, None)
        if not date:
            serial_data[curr_date] = {}

        vhi = serial_data.get(curr_date).get('vhi', None)

        if not vhi:
            serial_data[curr_date]['vhi'] = ''

        fname = serial_data.get(curr_date).get('vhi', None)

        if not fname:
            serial_data[curr_date]['vhi'] = 'vhi_dnipropetrovska_3_%s.csv' % full_date
            with open(serial_filepath, 'wb') as file:
                pickle.dump(serial_data, file)
            return serial_data.get(curr_date).get('vhi', None)

        return fname

    def vh_filename_creation(self):
        global serial_data
        serial_data = {}
        serial_filepath = os.path.abspath('filenames.pickle')
        curr_date = str(datetime.datetime.now())[0:10]
        full_date = str(datetime.datetime.now()).replace(' ', '-')[:-7]

        while True:
            try:
                with open(serial_filepath, 'rb') as d:
                    serial_data = pickle.load(d)
                    break
            except FileNotFoundError:
                open(serial_filepath, 'wb').close()
                continue
            except EOFError:
                serial_data = {}
                break

        date = serial_data.get(curr_date, None)
        if not date:
            serial_data[curr_date] = {}

        vh = serial_data.get(curr_date).get('vh', None)

        if not vh:
            serial_data[curr_date]['vh'] = ''

        fname = serial_data.get(curr_date).get('vh', None)

        if not fname:
            serial_data[curr_date]['vh'] = 'vh_dnipropetrovska_3_%s.csv' % full_date
            with open(serial_filepath, 'wb') as file:
                pickle.dump(serial_data, file)
            return serial_data.get(curr_date).get('vh', None)

        return fname

    def vhi_frame_creator(self):
        fname = self.vhi_filename_creation()
        curr_date = str(datetime.datetime.now())[0:10]
        fname_path = os.path.join(os.path.abspath(os.getcwd()), curr_date, fname)
        upload_dir = os.path.join(os.path.abspath(curr_date))
        if not os.path.isdir(os.path.join(os.path.abspath(os.getcwd()), curr_date)):
            try:
                subprocess.call(['mkdir %s' % upload_dir], stdout=subprocess.PIPE, shell=True)
            except:
                pass

        if not os.path.isfile(os.path.join(os.path.abspath(os.getcwd()), curr_date, fname)):
            self.vhi_data_parsing(fname_path)

        data_frame = pd.read_csv(os.path.join(os.path.abspath(os.getcwd()), curr_date, fname), index_col=False, header=1, names=['year', 'week', 'smn', 'smt', 'vci', 'tci', 'vhi'], delimiter=',', error_bad_lines=False)
        return data_frame

    def vh_frame_creator(self):
        fname = self.vh_filename_creation()
        curr_date = str(datetime.datetime.now())[0:10]
        fname_path = os.path.join(os.path.abspath(os.getcwd()), curr_date, fname)
        upload_dir = os.path.join(os.path.abspath(curr_date))
        if not os.path.isdir(os.path.join(os.path.abspath(os.getcwd()), curr_date)):
            try:
                subprocess.call(['mkdir %s' % upload_dir], stdout=subprocess.PIPE, shell=True)
            except:
                pass

        if not os.path.isfile(os.path.join(os.path.abspath(os.getcwd()), curr_date, fname)):
            self.vh_data_parsing(fname_path)

        data_frame = pd.read_csv(os.path.join(os.path.abspath(os.getcwd()), curr_date, fname), index_col=False, header=1, names=['year', 'week', '0%', '5%', '10%', '15%', '20%', '25%', '30%', '35%', '40%', '45%', '50%', '55%', '60%', '65%', '70%', '75%', '80%', '85%', '90%', '95%', '100%'], delimiter=',', error_bad_lines=False)
        return data_frame

    def plot_maker_vhi(self):
        fname = self.vhi_filename_creation()
        upload_dir = str(datetime.datetime.now())[0:10]
        if not os.path.isdir(os.path.join(os.path.abspath(os.getcwd()), upload_dir)):
            try:
                subprocess.call(['mkdir %s' % upload_dir], stdout=subprocess.PIPE, shell=True)
            except:
                pass

        fname_path = os.path.join(os.path.abspath(os.getcwd()), upload_dir, fname)

        while True:
            r = os.path.isfile(fname_path)
            if r:
                break
            time.sleep(0.7)
        data_frame = pd.read_csv(fname_path, index_col=False, header=1, names=['year', 'week', 'smn', 'smt', 'vci', 'tci', 'vhi'], delimiter=',', error_bad_lines=False)
        return data_frame

    def plot_maker_vh(self):
        fname = self.vh_filename_creation()
        upload_dir = str(datetime.datetime.now())[0:10]
        if not os.path.isdir(os.path.join(os.path.abspath(os.getcwd()), upload_dir)):
            try:
                subprocess.call(['mkdir %s' % upload_dir], stdout=subprocess.PIPE, shell=True)
            except:
                pass

        fname_path = os.path.join(os.path.abspath(os.getcwd()), upload_dir, fname)

        while True:
            r = os.path.isfile(fname_path)
            if r:
                break
            time.sleep(0.7)
        data_frame = pd.read_csv(fname_path, index_col=False, header=1, names=['year', 'week', '0%', '5%', '10%', '15%', '20%', '25%', '30%', '35%', '40%', '45%', '50%', '55%', '60%', '65%', '70%', '75%', '80%', '85%', '90%', '95%', '100%'], delimiter=',', error_bad_lines=False)
        return data_frame

    def getData(self, params):
        year_begin = params['year_begin']
        year_end = params['year_end']
        weeks = params['weeks']
        vhi_extremum = params['vhi_extremum']
        vhi_correlation = params['vhi_correlation']
        vhi_rate = params['vhi_rate']
        vhi_mild = params['vhi_mild']

        if year_begin and year_end:
            if year_end < year_begin:
                current = year_begin
                year_begin = year_end
                year_end = current

        if not vhi_rate and not vhi_mild:
            df = self.vhi_frame_creator()

            if year_begin:
                if weeks and not year_end:
                    return df[(df['year'] == int(year_begin)) & (df['week'] == int(weeks))]
                elif vhi_extremum and not year_end:
                    if vhi_extremum[0] == 'max':
                        return df[(df['year'] == int(year_begin)) & (df['vhi'] == df.groupby('year')['vhi'].transform('max'))]
                    else:
                        return df[(df['year'] == int(year_begin)) & (df['vhi'] == df.groupby('year')['vhi'].transform('min'))]
                elif year_end:
                    if vhi_extremum:
                        if vhi_extremum[0] == 'max':
                            return df[(df['year'].between(int(year_begin), int(year_end))) & (df['vhi'] == df.groupby('year')['vhi'].transform('max'))]
                        else:
                            return df[(df['year'].between(int(year_begin), int(year_end))) & (df['vhi'] == df.groupby('year')['vhi'].transform('min'))]
                    elif weeks:
                        if vhi_correlation and year_end and weeks:
                            if int(vhi_correlation) == 60:
                                return df[(df['year'].between(int(year_begin), int(year_end))) & (df['week'] == int(weeks)) & (df['vhi'] > 60)]
                            elif int(vhi_correlation) == 40:
                                return df[(df['year'].between(int(year_begin), int(year_end))) & (df['week'] == int(weeks)) & (df['vhi'] < 40)]
                            elif int(vhi_correlation) == 15:
                                return df[(df['year'].between(int(year_begin), int(year_end))) & (df['week'] == int(weeks)) & (df['vhi'] < 15)]
                            else:
                                return df[(df['year'].between(int(year_begin), int(year_end))) & (df['week'] == int(weeks)) & (df['vhi'] < 35)]
                        else:
                            return df[(df['year'].between(int(year_begin), int(year_end))) & (df['week'] == int(weeks))]
                    elif vhi_correlation and year_end:
                        if int(vhi_correlation) == 60:
                            return df[(df['year'].between(int(year_begin), int(year_end))) & (df['vhi'] > 60)]
                        elif int(vhi_correlation) == 40:
                            return df[(df['year'].between(int(year_begin), int(year_end))) & (df['vhi'] < 40)]
                        elif int(vhi_correlation) == 15:
                            return df[(df['year'].between(int(year_begin), int(year_end))) & (df['vhi'] < 15)]
                        else:
                            return df[(df['year'].between(int(year_begin), int(year_end))) & (df['vhi'] < 35)]
                    else:
                        return df[df['year'].between(int(year_begin), int(year_end))]

                elif vhi_correlation and not year_end:
                    if int(vhi_correlation) == 60:
                        return df[(df['year'] == int(year_begin)) & (df['vhi'] > 60)]
                    elif int(vhi_correlation) == 40:
                        return df[(df['year'] == int(year_begin)) & (df['vhi'] < 40)]
                    elif int(vhi_correlation) == 15:
                        return df[(df['year'] == int(year_begin)) & (df['vhi'] < 15)]
                    else:
                        return df[(df['year'] == int(year_begin)) & (df['vhi'] < 35)]
                else:
                    return df[(df['year'] == int(year_begin))]
            elif vhi_extremum:
                if vhi_extremum[0] == 'max':
                        return df[df['vhi'] == df.groupby('year')['vhi'].transform('max')]
                else:
                    return df[df['vhi'] == df.groupby('year')['vhi'].transform('min')]
            elif vhi_correlation:
                    if int(vhi_correlation) == 60:
                        return df[(df['vhi'] > 60)]
                    elif int(vhi_correlation) == 40:
                        return df[(df['vhi'] < 40)]
                    elif int(vhi_correlation) == 15:
                        return df[(df['vhi'] < 15)]
                    else:
                        return df[(df['vhi'] < 35)]
            elif year_end:
                if year_begin:
                    return df[df['year'].between(int(year_begin), int(year_end))]
                else:
                    return df[df['year'] == int(year_end)]
            else:
                return df
        elif vhi_rate:
            df = self.vh_frame_creator()
            if year_begin:
                if vhi_rate and not year_end:
                    if vhi_rate == '0':
                        return df[(df['year'] == int(year_begin)) & (df['5%'] + df['10%'] + df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)]
                    elif vhi_rate == '5':
                        return df[(df['year'] == int(year_begin)) & (df['10%'] + df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)]
                    elif vhi_rate == '10':
                        return df[(df['year'] == int(year_begin)) & (df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)]
                    elif vhi_rate == '15':
                        return df[(df['year'] == int(year_begin)) & (df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)]
                    elif vhi_rate == '20':
                        return df[(df['year'] == int(year_begin)) & (df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)]
                    elif vhi_rate == '25':
                        return df[(df['year'] == int(year_begin)) & (df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)]
                    elif vhi_rate == '30':
                        return df[(df['year'] == int(year_begin)) & (df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)]
                    elif vhi_rate == '35':
                        return df[(df['year'] == int(year_begin)) & (df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)]
                    elif vhi_rate == '40':
                        return df[(df['year'] == int(year_begin)) & (df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)]
                    elif vhi_rate == '45':
                        return df[(df['year'] == int(year_begin)) & (df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)]
                    elif vhi_rate == '50':
                        return df[(df['year'] == int(year_begin)) & (df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)]
                    elif vhi_rate == '55':
                        return df[(df['year'] == int(year_begin)) & (df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)]
                    elif vhi_rate == '60':
                        return df[(df['year'] == int(year_begin)) & (df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)]
                    elif vhi_rate == '65':
                        return df[(df['year'] == int(year_begin)) & (df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)]
                    elif vhi_rate == '70':
                        return df[(df['year'] == int(year_begin)) & (df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)]
                    elif vhi_rate == '75':
                        return df[(df['year'] == int(year_begin)) & (df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)]
                    elif vhi_rate == '80':
                        return df[(df['year'] == int(year_begin)) & (df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)]
                    elif vhi_rate == '85':
                        return df[(df['year'] == int(year_begin)) & (df['90%'] + df['95%'] + df['100%'] < 15)]
                    elif vhi_rate == '90':
                        return df[(df['year'] == int(year_begin)) & (df['95%'] + df['100%'] < 15)]
                    elif vhi_rate == '95':
                        return df[(df['year'] == int(year_begin) & df['100%'] < 15)]
                    elif vhi_rate == '100':
                        return df[(df['year'] == int(year_begin) & df['100%'] < 15)]
                    else:
                        return df

                elif vhi_rate and year_end:
                    if vhi_rate == '0':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['5%'] + df['10%'] + df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)]
                    elif vhi_rate == '5':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['10%'] + df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)]
                    elif vhi_rate == '10':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)]
                    elif vhi_rate == '15':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)]
                    elif vhi_rate == '20':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)]
                    elif vhi_rate == '25':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)]
                    elif vhi_rate == '30':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)]
                    elif vhi_rate == '35':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)]
                    elif vhi_rate == '40':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)]
                    elif vhi_rate == '45':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)]
                    elif vhi_rate == '50':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)]
                    elif vhi_rate == '55':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)]
                    elif vhi_rate == '60':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)]
                    elif vhi_rate == '65':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)]
                    elif vhi_rate == '70':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)]
                    elif vhi_rate == '75':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)]
                    elif vhi_rate == '80':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)]
                    elif vhi_rate == '85':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['90%'] + df['95%'] + df['100%'] < 15)]
                    elif vhi_rate == '90':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['95%'] + df['100%'] < 15)]
                    elif vhi_rate == '95':
                        return df[(df['year'].between(int(year_begin), int(year_end)) & df['100%'] < 15)]
                    elif vhi_rate == '100':
                        return df[(df['year'].between(int(year_begin), int(year_end)) & df['100%'] < 15)]
                    else:
                        return df

            elif vhi_rate and not year_begin:
                if vhi_rate == '0':
                    return df[(df['year']) & (df['5%'] + df['10%'] + df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)]
                elif vhi_rate == '5':
                    return df[(df['year']) & (df['10%'] + df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)]
                elif vhi_rate == '10':
                    return df[(df['year']) & (df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)]
                elif vhi_rate == '15':
                    return df[(df['year']) & (df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)]
                elif vhi_rate == '20':
                    return df[(df['year']) & (df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)]
                elif vhi_rate == '25':
                    return df[(df['year']) & (df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)]
                elif vhi_rate == '30':
                    return df[(df['year']) & (df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)]
                elif vhi_rate == '35':
                    return df[(df['year']) & (df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)]
                elif vhi_rate == '40':
                    return df[(df['year']) & (df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)]
                elif vhi_rate == '45':
                    return df[(df['year']) & (df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)]
                elif vhi_rate == '50':
                    return df[(df['year']) & (df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)]
                elif vhi_rate == '55':
                    return df[(df['year']) & (df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)]
                elif vhi_rate == '60':
                    return df[(df['year']) & (df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)]
                elif vhi_rate == '65':
                    return df[(df['year']) & (df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)]
                elif vhi_rate == '70':
                    return df[(df['year']) & (df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)]
                elif vhi_rate == '75':
                    return df[(df['year']) & (df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)]
                elif vhi_rate == '80':
                    return df[(df['year']) & (df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)]
                elif vhi_rate == '85':
                    return df[(df['year']) & (df['90%'] + df['95%'] + df['100%'] < 15)]
                elif vhi_rate == '90':
                    return df[(df['year']) & (df['95%'] + df['100%'] < 15)]
                elif vhi_rate == '95':
                    return df[(df['year'] & df['100%'] < 15)]
                elif vhi_rate == '100':
                    return df[(df['year'] & df['100%'] < 15)]
                else:
                    return df

        elif vhi_mild and not vhi_rate:
            df = self.vh_frame_creator()
            if year_begin:
                if vhi_mild and not year_end:
                    if vhi_mild == '0':
                        return df[(df['year'] == int(year_begin)) & (df['5%'] + df['10%'] + df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)]
                    elif vhi_mild == '5':
                        return df[(df['year'] == int(year_begin)) & (df['10%'] + df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)]
                    elif vhi_mild == '10':
                        return df[(df['year'] == int(year_begin)) & (df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)]
                    elif vhi_mild == '15':
                        return df[(df['year'] == int(year_begin)) & (df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)]
                    elif vhi_mild == '20':
                        return df[(df['year'] == int(year_begin)) & (df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)]
                    elif vhi_mild == '25':
                        return df[(df['year'] == int(year_begin)) & (df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)]
                    elif vhi_mild == '30':
                        return df[(df['year'] == int(year_begin)) & (df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)]
                    elif vhi_mild == '35':
                        return df[(df['year'] == int(year_begin)) & (df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)]
                    elif vhi_mild == '40':
                        return df[(df['year'] == int(year_begin)) & (df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)]
                    elif vhi_mild == '45':
                        return df[(df['year'] == int(year_begin)) & (df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)]
                    elif vhi_mild == '50':
                        return df[(df['year'] == int(year_begin)) & (df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)]
                    elif vhi_mild == '55':
                        return df[(df['year'] == int(year_begin)) & (df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)]
                    elif vhi_mild == '60':
                        return df[(df['year'] == int(year_begin)) & (df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)]
                    elif vhi_mild == '65':
                        return df[(df['year'] == int(year_begin)) & (df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)]
                    elif vhi_mild == '70':
                        return df[(df['year'] == int(year_begin)) & (df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)]
                    elif vhi_mild == '75':
                        return df[(df['year'] == int(year_begin)) & (df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)]
                    elif vhi_mild == '80':
                        return df[(df['year'] == int(year_begin)) & (df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)]
                    elif vhi_mild == '85':
                        return df[(df['year'] == int(year_begin)) & (df['90%'] + df['95%'] + df['100%'] < 35)]
                    elif vhi_mild == '90':
                        return df[(df['year'] == int(year_begin)) & (df['95%'] + df['100%'] < 35)]
                    elif vhi_mild == '95':
                        return df[(df['year'] == int(year_begin) & df['100%'] < 35)]
                    elif vhi_mild == '100':
                        return df[(df['year'] == int(year_begin) & df['100%'] < 35)]
                    else:
                        return df
                elif vhi_mild and year_end:
                    if vhi_mild == '0':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['5%'] + df['10%'] + df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)]
                    elif vhi_mild == '5':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['10%'] + df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)]
                    elif vhi_mild == '10':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)]
                    elif vhi_mild == '15':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)]
                    elif vhi_mild == '20':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)]
                    elif vhi_mild == '25':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)]
                    elif vhi_mild == '30':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)]
                    elif vhi_mild == '35':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)]
                    elif vhi_mild == '40':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)]
                    elif vhi_mild == '45':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)]
                    elif vhi_mild == '50':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)]
                    elif vhi_mild == '55':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)]
                    elif vhi_mild == '60':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)]
                    elif vhi_mild == '65':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)]
                    elif vhi_mild == '70':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)]
                    elif vhi_mild == '75':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)]
                    elif vhi_mild == '80':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)]
                    elif vhi_mild == '85':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['90%'] + df['95%'] + df['100%'] < 35)]
                    elif vhi_mild == '90':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['95%'] + df['100%'] < 35)]
                    elif vhi_mild == '95':
                        return df[(df['year'].between(int(year_begin), int(year_end)) & df['100%'] < 35)]
                    elif vhi_mild == '100':
                        return df[(df['year'].between(int(year_begin), int(year_end)) & df['100%'] < 35)]
                    else:
                        return df

            elif vhi_mild and not year_begin:
                if vhi_mild == '0':
                    return df[(df['year']) & (df['5%'] + df['10%'] + df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)]
                elif vhi_mild == '5':
                    return df[(df['year']) & (df['10%'] + df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)]
                elif vhi_mild == '10':
                    return df[(df['year']) & (df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)]
                elif vhi_mild == '15':
                    return df[(df['year']) & (df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)]
                elif vhi_mild == '20':
                    return df[(df['year']) & (df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)]
                elif vhi_mild == '25':
                    return df[(df['year']) & (df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)]
                elif vhi_mild == '30':
                    return df[(df['year']) & (df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)]
                elif vhi_mild == '35':
                    return df[(df['year']) & (df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)]
                elif vhi_mild == '40':
                    return df[(df['year']) & (df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)]
                elif vhi_mild == '45':
                    return df[(df['year']) & (df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)]
                elif vhi_mild == '50':
                    return df[(df['year']) & (df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)]
                elif vhi_mild == '55':
                    return df[(df['year']) & (df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)]
                elif vhi_mild == '60':
                    return df[(df['year']) & (df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)]
                elif vhi_mild == '65':
                    return df[(df['year']) & (df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)]
                elif vhi_mild == '70':
                    return df[(df['year']) & (df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)]
                elif vhi_mild == '75':
                    return df[(df['year']) & (df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)]
                elif vhi_mild == '80':
                    return df[(df['year']) & (df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)]
                elif vhi_mild == '85':
                    return df[(df['year']) & (df['90%'] + df['95%'] + df['100%'] < 35)]
                elif vhi_mild == '90':
                    return df[(df['year']) & (df['95%'] + df['100%'] < 35)]
                elif vhi_mild == '95':
                    return df[(df['year'] & df['100%'] < 35)]
                elif vhi_mild == '100':
                    return df[(df['year'] & df['100%'] < 35)]
                else:
                    return df

    def vhi_plot(self, params):
        year_begin = params['year_begin']
        year_end = params['year_end']
        weeks = params['weeks']
        vhi_extremum = params['vhi_extremum']
        vhi_correlation = params['vhi_correlation']
        vhi_rate = params['vhi_rate']
        vhi_mild = params['vhi_mild']

        if year_begin and year_end:
            if year_end < year_begin:
                current = year_begin
                year_begin = year_end
                year_end = current

        if not vhi_rate and not vhi_mild:
            df = self.plot_maker_vhi()

            if year_begin:
                if weeks and not year_end:
                    return df[(df['year'] == int(year_begin)) & (df['week'] == int(weeks))].drop(['vci', 'tci'], axis=1).plot.area(x='year', figsize=(11, 6))
                elif vhi_extremum and not year_end:

                    if vhi_extremum[0] == 'max':
                        return df[(df['year'] == int(year_begin)) & (df['vhi'] == df.groupby('year')['vhi'].transform('max'))].drop(['vci', 'tci'], axis=1).plot.area(x='year', figsize=(11, 6))
                    else:
                        return df[(df['year'] == int(year_begin)) & (df['vhi'] == df.groupby('year')['vhi'].transform('min'))].drop(['vci', 'tci'], axis=1).plot.area(x='year', figsize=(11, 6))
                elif year_end:
                    if vhi_extremum:
                        if vhi_extremum[0] == 'max':
                            return df[(df['year'].between(int(year_begin), int(year_end))) & (df['vhi'] == df.groupby('year')['vhi'].transform('max'))].drop(['vci', 'tci'], axis=1).plot.area(x='year', figsize=(11, 6))
                        else:
                            return df[(df['year'].between(int(year_begin), int(year_end))) & (df['vhi'] == df.groupby('year')['vhi'].transform('min'))].drop(['vci', 'tci'], axis=1).plot.area(x='year', figsize=(11, 6))
                    elif weeks:
                        if vhi_correlation and year_end and weeks:
                            if int(vhi_correlation) == 60:
                                return df[(df['year'].between(int(year_begin), int(year_end))) & (df['week'] == int(weeks)) & (df['vhi'] > 60)].drop(['vci', 'tci'], axis=1).plot.area(x='year', figsize=(11, 6))
                            elif int(vhi_correlation) == 40:
                                return df[(df['year'].between(int(year_begin), int(year_end))) & (df['week'] == int(weeks)) & (df['vhi'] < 40)].drop(['vci', 'tci'], axis=1).plot.area(x='year', figsize=(11, 6))
                            elif int(vhi_correlation) == 15:
                                return df[(df['year'].between(int(year_begin), int(year_end))) & (df['week'] == int(weeks)) & (df['vhi'] < 15)].drop(['vci', 'tci'], axis=1).plot.area(x='year', figsize=(11, 6))
                            else:
                                return df[(df['year'].between(int(year_begin), int(year_end))) & (df['week'] == int(weeks)) & (df['vhi'] < 35)].drop(['vci', 'tci'], axis=1).plot.area(x='year', figsize=(11, 6))
                        else:
                            return df[(df['year'].between(int(year_begin), int(year_end))) & (df['week'] == int(weeks))].drop(['vci', 'tci'], axis=1).plot.area(x='year', figsize=(11, 6))

                    elif vhi_correlation and year_end:
                        if int(vhi_correlation) == 60:

                            return df[(df['year'].between(int(year_begin), int(year_end))) & (df['vhi'] > 60)].drop(['vci', 'tci'], axis=1).plot.area(x='year', figsize=(11, 6))
                        elif int(vhi_correlation) == 40:

                            return df[(df['year'].between(int(year_begin), int(year_end))) & (df['vhi'] < 40)].drop(['vci', 'tci'], axis=1).plot.area(x='year', figsize=(11, 6))
                        elif int(vhi_correlation) == 15:

                            return df[(df['year'].between(int(year_begin), int(year_end))) & (df['vhi'] < 15)].drop(['vci', 'tci'], axis=1).plot.area(x='year', figsize=(11, 6))
                        else:

                            return df[(df['year'].between(int(year_begin), int(year_end))) & (df['vhi'] < 35)].drop(['vci', 'tci'], axis=1).plot.area(x='year', figsize=(11, 6))

                    else:
                        return df[df['year'].between(int(year_begin), int(year_end))].drop(['vci', 'tci'], axis=1).plot.area(x='year', figsize=(11, 6))

                elif vhi_correlation and not year_end:
                    if int(vhi_correlation) == 60:

                        return df[(df['year'] == int(year_begin)) & (df['vhi'] > 60)].drop(['vci', 'tci'], axis=1).plot.area(x='year', figsize=(11, 6))
                    elif int(vhi_correlation) == 40:

                        return df[(df['year'] == int(year_begin)) & (df['vhi'] < 40)].drop(['vci', 'tci'], axis=1).plot.area(x='year', figsize=(11, 6))
                    elif int(vhi_correlation) == 15:

                        return df[(df['year'] == int(year_begin)) & (df['vhi'] < 15)].drop(['vci', 'tci'], axis=1).plot.area(x='year', figsize=(11, 6))
                    else:

                        return df[(df['year'] == int(year_begin)) & (df['vhi'] < 35)].drop(['vci', 'tci'], axis=1).plot.area(x='year', figsize=(11, 6))
                else:
                    return df[(df['year'] == int(year_begin))].drop(['vci', 'tci'], axis=1).plot.area(x='year', figsize=(11, 6))
            elif vhi_extremum:
                if vhi_extremum[0] == 'max':
                        return df[df['vhi'] == df.groupby('year')['vhi'].transform('max')].drop(['vci', 'tci'], axis=1).plot.area(x='year', figsize=(11, 6))
                else:
                    return df[df['vhi'] == df.groupby('year')['vhi'].transform('min')].drop(['vci', 'tci'], axis=1).plot.area(x='year', figsize=(11, 6))

            elif vhi_correlation:
                    if int(vhi_correlation) == 60:

                        return df[(df['vhi'] > 60)].drop(['vci', 'tci'], axis=1).plot.area(x='year', figsize=(11, 6))
                    elif int(vhi_correlation) == 40:

                        return df[(df['vhi'] < 40)].drop(['vci', 'tci'], axis=1).plot.area(x='year', figsize=(11, 6))
                    elif int(vhi_correlation) == 15:

                        return df[(df['vhi'] < 15)].drop(['vci', 'tci'], axis=1).plot.area(x='year', figsize=(11, 6))
                    else:

                        return df[(df['vhi'] < 35)].drop(['vci', 'tci'], axis=1).plot.area(x='year', figsize=(11, 6))

            elif year_end:

                if year_begin:
                    return df[df['year'].between(int(year_begin), int(year_end))].drop(['vci', 'tci'], axis=1).plot.area(x='year', figsize=(11, 6))
                else:

                    return df[df['year'] == int(year_end)].drop(['vci', 'tci'], axis=1).plot.area(x='year', figsize=(11, 6))
            else:
                return df.drop(['vci', 'tci'], axis=1).plot.area(x='year', figsize=(11, 6))

        elif vhi_rate:
            df = self.plot_maker_vh()

            if year_begin:
                if vhi_rate and not year_end:
                    if vhi_rate == '0':
                        return df[(df['year'] == int(year_begin)) & (df['5%'] + df['10%'] + df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '5':
                        return df[(df['year'] == int(year_begin)) & (df['10%'] + df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '10':
                        return df[(df['year'] == int(year_begin)) & (df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '15':
                        return df[(df['year'] == int(year_begin)) & (df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '20':
                        return df[(df['year'] == int(year_begin)) & (df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '25':
                        return df[(df['year'] == int(year_begin)) & (df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '30':
                        return df[(df['year'] == int(year_begin)) & (df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '35':
                        return df[(df['year'] == int(year_begin)) & (df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '40':
                        return df[(df['year'] == int(year_begin)) & (df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '45':
                        return df[(df['year'] == int(year_begin)) & (df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '50':
                        return df[(df['year'] == int(year_begin)) & (df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '55':
                        return df[(df['year'] == int(year_begin)) & (df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '60':
                        return df[(df['year'] == int(year_begin)) & (df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '65':
                        return df[(df['year'] == int(year_begin)) & (df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '70':
                        return df[(df['year'] == int(year_begin)) & (df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '75':
                        return df[(df['year'] == int(year_begin)) & (df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '80':
                        return df[(df['year'] == int(year_begin)) & (df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '85':
                        return df[(df['year'] == int(year_begin)) & (df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '90':
                        return df[(df['year'] == int(year_begin)) & (df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '95':
                        return df[(df['year'] == int(year_begin) & df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '100':
                        return df[(df['year'] == int(year_begin) & df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    else:
                        return df.plot.area(x='year', figsize=(11, 6))

                elif vhi_rate and year_end:
                    if vhi_rate == '0':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['5%'] + df['10%'] + df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '5':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['10%'] + df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '10':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '15':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '20':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '25':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '30':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '35':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '40':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '45':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '50':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '55':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '60':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '65':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '70':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '75':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '80':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '85':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '90':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '95':
                        return df[(df['year'].between(int(year_begin), int(year_end)) & df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '100':
                        return df[(df['year'].between(int(year_begin), int(year_end)) & df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    else:
                        return df.plot.area(x='year', figsize=(11, 6))

            elif vhi_rate and not year_begin:
                if vhi_rate == '0':
                    return df[(df['year']) & (df['5%'] + df['10%'] + df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                elif vhi_rate == '5':
                    return df[(df['year']) & (df['10%'] + df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                elif vhi_rate == '10':
                    return df[(df['year']) & (df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                elif vhi_rate == '15':
                    return df[(df['year']) & (df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                elif vhi_rate == '20':
                    return df[(df['year']) & (df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                elif vhi_rate == '25':
                    return df[(df['year']) & (df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                elif vhi_rate == '30':
                    return df[(df['year']) & (df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                elif vhi_rate == '35':
                    return df[(df['year']) & (df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                elif vhi_rate == '40':
                    return df[(df['year']) & (df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                elif vhi_rate == '45':
                    return df[(df['year']) & (df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                elif vhi_rate == '50':
                    return df[(df['year']) & (df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                elif vhi_rate == '55':
                    return df[(df['year']) & (df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                elif vhi_rate == '60':
                    return df[(df['year']) & (df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                elif vhi_rate == '65':
                    return df[(df['year']) & (df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                elif vhi_rate == '70':
                    return df[(df['year']) & (df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                elif vhi_rate == '75':
                    return df[(df['year']) & (df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                elif vhi_rate == '80':
                    return df[(df['year']) & (df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                elif vhi_rate == '85':
                    return df[(df['year']) & (df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                elif vhi_rate == '90':
                    return df[(df['year']) & (df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                elif vhi_rate == '95':
                    return df[(df['year'] & df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                elif vhi_rate == '100':
                    return df[(df['year'] & df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                else:
                    return df.plot.area(x='year', figsize=(11, 6))

        elif vhi_mild and not vhi_rate:
            df = self.plot_maker_vh()

            if year_begin:
                if vhi_mild and not year_end:
                    if vhi_mild == '0':
                        return df[(df['year'] == int(year_begin)) & (df['5%'] + df['10%'] + df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '5':
                        return df[(df['year'] == int(year_begin)) & (df['10%'] + df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '10':
                        return df[(df['year'] == int(year_begin)) & (df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '15':
                        return df[(df['year'] == int(year_begin)) & (df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '20':
                        return df[(df['year'] == int(year_begin)) & (df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '25':
                        return df[(df['year'] == int(year_begin)) & (df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '30':
                        return df[(df['year'] == int(year_begin)) & (df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '35':
                        return df[(df['year'] == int(year_begin)) & (df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '40':
                        return df[(df['year'] == int(year_begin)) & (df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '45':
                        return df[(df['year'] == int(year_begin)) & (df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '50':
                        return df[(df['year'] == int(year_begin)) & (df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '55':
                        return df[(df['year'] == int(year_begin)) & (df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '60':
                        return df[(df['year'] == int(year_begin)) & (df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '65':
                        return df[(df['year'] == int(year_begin)) & (df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '70':
                        return df[(df['year'] == int(year_begin)) & (df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '75':
                        return df[(df['year'] == int(year_begin)) & (df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '80':
                        return df[(df['year'] == int(year_begin)) & (df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '85':
                        return df[(df['year'] == int(year_begin)) & (df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '90':
                        return df[(df['year'] == int(year_begin)) & (df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '95':
                        return df[(df['year'] == int(year_begin) & df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '100':
                        return df[(df['year'] == int(year_begin) & df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    else:
                        return df.plot.area(x='year', figsize=(11, 6))

                elif vhi_mild and year_end:
                    if vhi_mild == '0':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['5%'] + df['10%'] + df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '5':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['10%'] + df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '10':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '15':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '20':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '25':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '30':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '35':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '40':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '45':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '50':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '55':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '60':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '65':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '70':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '75':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '80':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '85':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '90':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '95':
                        return df[(df['year'].between(int(year_begin), int(year_end)) & df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '100':
                        return df[(df['year'].between(int(year_begin), int(year_end)) & df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    else:
                        return df.plot.area(x='year', figsize=(11, 6))

            elif vhi_mild and not year_begin:
                if vhi_mild == '0':
                    return df[(df['year']) & (df['5%'] + df['10%'] + df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                elif vhi_mild == '5':
                    return df[(df['year']) & (df['10%'] + df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                elif vhi_mild == '10':
                    return df[(df['year']) & (df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                elif vhi_mild == '15':
                    return df[(df['year']) & (df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                elif vhi_mild == '20':
                    return df[(df['year']) & (df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                elif vhi_mild == '25':
                    return df[(df['year']) & (df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                elif vhi_mild == '30':
                    return df[(df['year']) & (df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                elif vhi_mild == '35':
                    return df[(df['year']) & (df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                elif vhi_mild == '40':
                    return df[(df['year']) & (df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                elif vhi_mild == '45':
                    return df[(df['year']) & (df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                elif vhi_mild == '50':
                    return df[(df['year']) & (df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                elif vhi_mild == '55':
                    return df[(df['year']) & (df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                elif vhi_mild == '60':
                    return df[(df['year']) & (df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                elif vhi_mild == '65':
                    return df[(df['year']) & (df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                elif vhi_mild == '70':
                    return df[(df['year']) & (df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                elif vhi_mild == '75':
                    return df[(df['year']) & (df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                elif vhi_mild == '80':
                    return df[(df['year']) & (df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                elif vhi_mild == '85':
                    return df[(df['year']) & (df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                elif vhi_mild == '90':
                    return df[(df['year']) & (df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                elif vhi_mild == '95':
                    return df[(df['year'] & df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                elif vhi_mild == '100':
                    return df[(df['year'] & df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                else:
                    return df.plot.area(x='year', figsize=(11, 6))

    def tci_plot(self, params):
        year_begin = params['year_begin']
        year_end = params['year_end']
        weeks = params['weeks']
        vhi_extremum = params['vhi_extremum']
        vhi_correlation = params['vhi_correlation']
        vhi_rate = params['vhi_rate']
        vhi_mild = params['vhi_mild']

        if year_begin and year_end:
            if year_end < year_begin:
                current = year_begin
                year_begin = year_end
                year_end = current

        if not vhi_rate and not vhi_mild:
            df = self.plot_maker_vhi()

            if year_begin:
                if weeks and not year_end:
                    return df[(df['year'] == int(year_begin)) & (df['week'] == int(weeks))].drop(['vhi', 'vci'], axis=1).plot.area(x='year', figsize=(11, 6))
                elif vhi_extremum and not year_end:

                    if vhi_extremum[0] == 'max':
                        return df[(df['year'] == int(year_begin)) & (df['vhi'] == df.groupby('year')['vhi'].transform('max'))].drop(['vhi', 'vci'], axis=1).plot.area(x='year', figsize=(11, 6))
                    else:
                        return df[(df['year'] == int(year_begin)) & (df['vhi'] == df.groupby('year')['vhi'].transform('min'))].drop(['vhi', 'vci'], axis=1).plot.area(x='year', figsize=(11, 6))
                elif year_end:
                    if vhi_extremum:
                        if vhi_extremum[0] == 'max':
                            return df[(df['year'].between(int(year_begin), int(year_end))) & (df['vhi'] == df.groupby('year')['vhi'].transform('max'))].drop(['vhi', 'vci'], axis=1).plot.area(x='year', figsize=(11, 6))
                        else:
                            return df[(df['year'].between(int(year_begin), int(year_end))) & (df['vhi'] == df.groupby('year')['vhi'].transform('min'))].drop(['vhi', 'vci'], axis=1).plot.area(x='year', figsize=(11, 6))
                    elif weeks:
                        if vhi_correlation and year_end and weeks:
                            if int(vhi_correlation) == 60:
                                return df[(df['year'].between(int(year_begin), int(year_end))) & (df['week'] == int(weeks)) & (df['vhi'] > 60)].drop(['vhi', 'vci'], axis=1).plot.area(x='year', figsize=(11, 6))
                            elif int(vhi_correlation) == 40:
                                return df[(df['year'].between(int(year_begin), int(year_end))) & (df['week'] == int(weeks)) & (df['vhi'] < 40)].drop(['vhi', 'vci'], axis=1).plot.area(x='year', figsize=(11, 6))
                            elif int(vhi_correlation) == 15:
                                return df[(df['year'].between(int(year_begin), int(year_end))) & (df['week'] == int(weeks)) & (df['vhi'] < 15)].drop(['vhi', 'vci'], axis=1).plot.area(x='year', figsize=(11, 6))
                            else:
                                return df[(df['year'].between(int(year_begin), int(year_end))) & (df['week'] == int(weeks)) & (df['vhi'] < 35)].drop(['vhi', 'vci'], axis=1).plot.area(x='year', figsize=(11, 6))
                        else:
                            return df[(df['year'].between(int(year_begin), int(year_end))) & (df['week'] == int(weeks))].drop(['vhi', 'vci'], axis=1).plot.area(x='year', figsize=(11, 6))

                    elif vhi_correlation and year_end:
                        if int(vhi_correlation) == 60:

                            return df[(df['year'].between(int(year_begin), int(year_end))) & (df['vhi'] > 60)].drop(['vhi', 'vci'], axis=1).plot.area(x='year', figsize=(11, 6))
                        elif int(vhi_correlation) == 40:

                            return df[(df['year'].between(int(year_begin), int(year_end))) & (df['vhi'] < 40)].drop(['vhi', 'vci'], axis=1).plot.area(x='year', figsize=(11, 6))
                        elif int(vhi_correlation) == 15:

                            return df[(df['year'].between(int(year_begin), int(year_end))) & (df['vhi'] < 15)].drop(['vhi', 'vci'], axis=1).plot.area(x='year', figsize=(11, 6))
                        else:

                            return df[(df['year'].between(int(year_begin), int(year_end))) & (df['vhi'] < 35)].drop(['vhi', 'vci'], axis=1).plot.area(x='year', figsize=(11, 6))

                    else:
                        return df[df['year'].between(int(year_begin), int(year_end))].drop(['vhi', 'vci'], axis=1).plot.area(x='year', figsize=(11, 6))

                elif vhi_correlation and not year_end:
                    if int(vhi_correlation) == 60:

                        return df[(df['year'] == int(year_begin)) & (df['vhi'] > 60)].drop(['vhi', 'vci'], axis=1).plot.area(x='year', figsize=(11, 6))
                    elif int(vhi_correlation) == 40:

                        return df[(df['year'] == int(year_begin)) & (df['vhi'] < 40)].drop(['vhi', 'vci'], axis=1).plot.area(x='year', figsize=(11, 6))
                    elif int(vhi_correlation) == 15:

                        return df[(df['year'] == int(year_begin)) & (df['vhi'] < 15)].drop(['vhi', 'vci'], axis=1).plot.area(x='year', figsize=(11, 6))
                    else:

                        return df[(df['year'] == int(year_begin)) & (df['vhi'] < 35)].drop(['vhi', 'vci'], axis=1).plot.area(x='year', figsize=(11, 6))
                else:
                    return df[(df['year'] == int(year_begin))].drop(['vhi', 'vci'], axis=1).plot.area(x='year', figsize=(11, 6))
            elif vhi_extremum:
                if vhi_extremum[0] == 'max':
                        return df[df['vhi'] == df.groupby('year')['vhi'].transform('max')].drop(['vhi', 'vci'], axis=1).plot.area(x='year', figsize=(11, 6))
                else:
                    return df[df['vhi'] == df.groupby('year')['vhi'].transform('min')].drop(['vhi', 'vci'], axis=1).plot.area(x='year', figsize=(11, 6))

            elif vhi_correlation:
                    if int(vhi_correlation) == 60:

                        return df[(df['vhi'] > 60)].drop(['vhi', 'vci'], axis=1).plot.area(x='year', figsize=(11, 6))
                    elif int(vhi_correlation) == 40:

                        return df[(df['vhi'] < 40)].drop(['vhi', 'vci'], axis=1).plot.area(x='year', figsize=(11, 6))
                    elif int(vhi_correlation) == 15:

                        return df[(df['vhi'] < 15)].drop(['vhi', 'vci'], axis=1).plot.area(x='year', figsize=(11, 6))
                    else:

                        return df[(df['vhi'] < 35)].drop(['vhi', 'vci'], axis=1).plot.area(x='year', figsize=(11, 6))

            elif year_end:

                if year_begin:
                    return df[df['year'].between(int(year_begin), int(year_end))].drop(['vhi', 'vci'], axis=1).plot.area(x='year', figsize=(11, 6))
                else:

                    return df[df['year'] == int(year_end)].drop(['vhi', 'vci'], axis=1).plot.area(x='year', figsize=(11, 6))
            else:
                return df.drop(['vhi', 'vci'], axis=1).plot.area(x='year', figsize=(11, 6))

        elif vhi_rate:
            df = self.plot_maker_vh()
            if year_begin:
                if vhi_rate and not year_end:
                    if vhi_rate == '0':
                        return df[(df['year'] == int(year_begin)) & (df['5%'] + df['10%'] + df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '5':
                        return df[(df['year'] == int(year_begin)) & (df['10%'] + df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '10':
                        return df[(df['year'] == int(year_begin)) & (df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '15':
                        return df[(df['year'] == int(year_begin)) & (df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '20':
                        return df[(df['year'] == int(year_begin)) & (df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '25':
                        return df[(df['year'] == int(year_begin)) & (df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '30':
                        return df[(df['year'] == int(year_begin)) & (df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '35':
                        return df[(df['year'] == int(year_begin)) & (df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '40':
                        return df[(df['year'] == int(year_begin)) & (df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '45':
                        return df[(df['year'] == int(year_begin)) & (df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '50':
                        return df[(df['year'] == int(year_begin)) & (df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '55':
                        return df[(df['year'] == int(year_begin)) & (df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '60':
                        return df[(df['year'] == int(year_begin)) & (df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '65':
                        return df[(df['year'] == int(year_begin)) & (df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '70':
                        return df[(df['year'] == int(year_begin)) & (df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '75':
                        return df[(df['year'] == int(year_begin)) & (df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '80':
                        return df[(df['year'] == int(year_begin)) & (df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '85':
                        return df[(df['year'] == int(year_begin)) & (df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '90':
                        return df[(df['year'] == int(year_begin)) & (df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '95':
                        return df[(df['year'] == int(year_begin) & df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '100':
                        return df[(df['year'] == int(year_begin) & df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    else:
                        return df.plot.area(x='year', figsize=(11, 6))

                elif vhi_rate and year_end:
                    if vhi_rate == '0':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['5%'] + df['10%'] + df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '5':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['10%'] + df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '10':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '15':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '20':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '25':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '30':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '35':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '40':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '45':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '50':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '55':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '60':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '65':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '70':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '75':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '80':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '85':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '90':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '95':
                        return df[(df['year'].between(int(year_begin), int(year_end)) & df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '100':
                        return df[(df['year'].between(int(year_begin), int(year_end)) & df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    else:
                        return df.plot.area(x='year', figsize=(11, 6))

            elif vhi_rate and not year_begin:
                if vhi_rate == '0':
                    return df[(df['year']) & (df['5%'] + df['10%'] + df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                elif vhi_rate == '5':
                    return df[(df['year']) & (df['10%'] + df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                elif vhi_rate == '10':
                    return df[(df['year']) & (df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                elif vhi_rate == '15':
                    return df[(df['year']) & (df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                elif vhi_rate == '20':
                    return df[(df['year']) & (df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                elif vhi_rate == '25':
                    return df[(df['year']) & (df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                elif vhi_rate == '30':
                    return df[(df['year']) & (df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                elif vhi_rate == '35':
                    return df[(df['year']) & (df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                elif vhi_rate == '40':
                    return df[(df['year']) & (df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                elif vhi_rate == '45':
                    return df[(df['year']) & (df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                elif vhi_rate == '50':
                    return df[(df['year']) & (df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                elif vhi_rate == '55':
                    return df[(df['year']) & (df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                elif vhi_rate == '60':
                    return df[(df['year']) & (df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                elif vhi_rate == '65':
                    return df[(df['year']) & (df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                elif vhi_rate == '70':
                    return df[(df['year']) & (df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                elif vhi_rate == '75':
                    return df[(df['year']) & (df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                elif vhi_rate == '80':
                    return df[(df['year']) & (df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                elif vhi_rate == '85':
                    return df[(df['year']) & (df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                elif vhi_rate == '90':
                    return df[(df['year']) & (df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                elif vhi_rate == '95':
                    return df[(df['year'] & df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                elif vhi_rate == '100':
                    return df[(df['year'] & df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                else:
                    return df.plot.area(x='year', figsize=(11, 6))

        elif vhi_mild and not vhi_rate:
            df = self.plot_maker_vh()

            if year_begin:
                if vhi_mild and not year_end:
                    if vhi_mild == '0':
                        return df[(df['year'] == int(year_begin)) & (df['5%'] + df['10%'] + df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '5':
                        return df[(df['year'] == int(year_begin)) & (df['10%'] + df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '10':
                        return df[(df['year'] == int(year_begin)) & (df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '15':
                        return df[(df['year'] == int(year_begin)) & (df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '20':
                        return df[(df['year'] == int(year_begin)) & (df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '25':
                        return df[(df['year'] == int(year_begin)) & (df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '30':
                        return df[(df['year'] == int(year_begin)) & (df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '35':
                        return df[(df['year'] == int(year_begin)) & (df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '40':
                        return df[(df['year'] == int(year_begin)) & (df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '45':
                        return df[(df['year'] == int(year_begin)) & (df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '50':
                        return df[(df['year'] == int(year_begin)) & (df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '55':
                        return df[(df['year'] == int(year_begin)) & (df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '60':
                        return df[(df['year'] == int(year_begin)) & (df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '65':
                        return df[(df['year'] == int(year_begin)) & (df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '70':
                        return df[(df['year'] == int(year_begin)) & (df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '75':
                        return df[(df['year'] == int(year_begin)) & (df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '80':
                        return df[(df['year'] == int(year_begin)) & (df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '85':
                        return df[(df['year'] == int(year_begin)) & (df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '90':
                        return df[(df['year'] == int(year_begin)) & (df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '95':
                        return df[(df['year'] == int(year_begin) & df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '100':
                        return df[(df['year'] == int(year_begin) & df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    else:
                        return df.plot.area(x='year', figsize=(11, 6))

                elif vhi_mild and year_end:
                    if vhi_mild == '0':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['5%'] + df['10%'] + df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '5':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['10%'] + df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '10':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '15':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '20':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '25':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '30':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '35':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '40':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '45':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '50':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '55':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '60':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '65':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '70':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '75':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '80':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '85':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '90':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '95':
                        return df[(df['year'].between(int(year_begin), int(year_end)) & df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '100':
                        return df[(df['year'].between(int(year_begin), int(year_end)) & df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    else:
                        return df.plot.area(x='year', figsize=(11, 6))

            elif vhi_mild and not year_begin:
                if vhi_mild == '0':
                    return df[(df['year']) & (df['5%'] + df['10%'] + df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                elif vhi_mild == '5':
                    return df[(df['year']) & (df['10%'] + df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                elif vhi_mild == '10':
                    return df[(df['year']) & (df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                elif vhi_mild == '15':
                    return df[(df['year']) & (df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                elif vhi_mild == '20':
                    return df[(df['year']) & (df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                elif vhi_mild == '25':
                    return df[(df['year']) & (df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                elif vhi_mild == '30':
                    return df[(df['year']) & (df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                elif vhi_mild == '35':
                    return df[(df['year']) & (df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                elif vhi_mild == '40':
                    return df[(df['year']) & (df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                elif vhi_mild == '45':
                    return df[(df['year']) & (df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                elif vhi_mild == '50':
                    return df[(df['year']) & (df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                elif vhi_mild == '55':
                    return df[(df['year']) & (df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                elif vhi_mild == '60':
                    return df[(df['year']) & (df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                elif vhi_mild == '65':
                    return df[(df['year']) & (df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                elif vhi_mild == '70':
                    return df[(df['year']) & (df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                elif vhi_mild == '75':
                    return df[(df['year']) & (df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                elif vhi_mild == '80':
                    return df[(df['year']) & (df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                elif vhi_mild == '85':
                    return df[(df['year']) & (df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                elif vhi_mild == '90':
                    return df[(df['year']) & (df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                elif vhi_mild == '95':
                    return df[(df['year'] & df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                elif vhi_mild == '100':
                    return df[(df['year'] & df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                else:
                    return df.plot.area(x='year', figsize=(11, 6))


    def vci_plot(self, params):
        year_begin = params['year_begin']
        year_end = params['year_end']
        weeks = params['weeks']
        vhi_extremum = params['vhi_extremum']
        vhi_correlation = params['vhi_correlation']
        vhi_rate = params['vhi_rate']
        vhi_mild = params['vhi_mild']

        if year_begin and year_end:
            if year_end < year_begin:
                current = year_begin
                year_begin = year_end
                year_end = current

        if not vhi_rate and not vhi_mild:
            df = self.plot_maker_vhi()

            if year_begin:
                if weeks and not year_end:
                    return df[(df['year'] == int(year_begin)) & (df['week'] == int(weeks))].drop(['vhi', 'tci'], axis=1).plot.area(x='year', figsize=(11, 6))
                elif vhi_extremum and not year_end:

                    if vhi_extremum[0] == 'max':
                        return df[(df['year'] == int(year_begin)) & (df['vhi'] == df.groupby('year')['vhi'].transform('max'))].drop(['vhi', 'tci'], axis=1).plot.area(x='year', figsize=(11, 6))
                    else:
                        return df[(df['year'] == int(year_begin)) & (df['vhi'] == df.groupby('year')['vhi'].transform('min'))].drop(['vhi', 'tci'], axis=1).plot.area(x='year', figsize=(11, 6))
                elif year_end:
                    if vhi_extremum:
                        if vhi_extremum[0] == 'max':
                            return df[(df['year'].between(int(year_begin), int(year_end))) & (df['vhi'] == df.groupby('year')['vhi'].transform('max'))].drop(['vhi', 'tci'], axis=1).plot.area(x='year', figsize=(11, 6))
                        else:
                            return df[(df['year'].between(int(year_begin), int(year_end))) & (df['vhi'] == df.groupby('year')['vhi'].transform('min'))].drop(['vhi', 'tci'], axis=1).plot.area(x='year', figsize=(11, 6))
                    elif weeks:
                        if vhi_correlation and year_end and weeks:
                            if int(vhi_correlation) == 60:
                                return df[(df['year'].between(int(year_begin), int(year_end))) & (df['week'] == int(weeks)) & (df['vhi'] > 60)].drop(['vhi', 'tci'], axis=1).plot.area(x='year', figsize=(11, 6))
                            elif int(vhi_correlation) == 40:
                                return df[(df['year'].between(int(year_begin), int(year_end))) & (df['week'] == int(weeks)) & (df['vhi'] < 40)].drop(['vhi', 'tci'], axis=1).plot.area(x='year', figsize=(11, 6))
                            elif int(vhi_correlation) == 15:
                                return df[(df['year'].between(int(year_begin), int(year_end))) & (df['week'] == int(weeks)) & (df['vhi'] < 15)].drop(['vhi', 'tci'], axis=1).plot.area(x='year', figsize=(11, 6))
                            else:
                                return df[(df['year'].between(int(year_begin), int(year_end))) & (df['week'] == int(weeks)) & (df['vhi'] < 35)].drop(['vhi', 'tci'], axis=1).plot.area(x='year', figsize=(11, 6))
                        else:
                            return df[(df['year'].between(int(year_begin), int(year_end))) & (df['week'] == int(weeks))].drop(['vhi', 'tci'], axis=1).plot.area(x='year', figsize=(11, 6))

                    elif vhi_correlation and year_end:
                        if int(vhi_correlation) == 60:

                            return df[(df['year'].between(int(year_begin), int(year_end))) & (df['vhi'] > 60)].drop(['vhi', 'tci'], axis=1).plot.area(x='year', figsize=(11, 6))
                        elif int(vhi_correlation) == 40:

                            return df[(df['year'].between(int(year_begin), int(year_end))) & (df['vhi'] < 40)].drop(['vhi', 'tci'], axis=1).plot.area(x='year', figsize=(11, 6))
                        elif int(vhi_correlation) == 15:

                            return df[(df['year'].between(int(year_begin), int(year_end))) & (df['vhi'] < 15)].drop(['vhi', 'tci'], axis=1).plot.area(x='year', figsize=(11, 6))
                        else:

                            return df[(df['year'].between(int(year_begin), int(year_end))) & (df['vhi'] < 35)].drop(['vhi', 'tci'], axis=1).plot.area(x='year', figsize=(11, 6))

                    else:
                        return df[df['year'].between(int(year_begin), int(year_end))].drop(['vhi', 'tci'], axis=1).plot.area(x='year', figsize=(11, 6))

                elif vhi_correlation and not year_end:
                    if int(vhi_correlation) == 60:

                        return df[(df['year'] == int(year_begin)) & (df['vhi'] > 60)].drop(['vhi', 'tci'], axis=1).plot.area(x='year', figsize=(11, 6))
                    elif int(vhi_correlation) == 40:

                        return df[(df['year'] == int(year_begin)) & (df['vhi'] < 40)].drop(['vhi', 'tci'], axis=1).plot.area(x='year', figsize=(11, 6))
                    elif int(vhi_correlation) == 15:

                        return df[(df['year'] == int(year_begin)) & (df['vhi'] < 15)].drop(['vhi', 'tci'], axis=1).plot.area(x='year', figsize=(11, 6))
                    else:

                        return df[(df['year'] == int(year_begin)) & (df['vhi'] < 35)].drop(['vhi', 'tci'], axis=1).plot.area(x='year', figsize=(11, 6))
                else:
                    return df[(df['year'] == int(year_begin))].drop(['vhi', 'tci'], axis=1).plot.area(x='year', figsize=(11, 6))
            elif vhi_extremum:
                if vhi_extremum[0] == 'max':
                        return df[df['vhi'] == df.groupby('year')['vhi'].transform('max')].drop(['vhi', 'tci'], axis=1).plot.area(x='year', figsize=(11, 6))
                else:
                    return df[df['vhi'] == df.groupby('year')['vhi'].transform('min')].drop(['vhi', 'tci'], axis=1).plot.area(x='year', figsize=(11, 6))

            elif vhi_correlation:
                    if int(vhi_correlation) == 60:

                        return df[(df['vhi'] > 60)].drop(['vhi', 'tci'], axis=1).plot.area(x='year', figsize=(11, 6))
                    elif int(vhi_correlation) == 40:

                        return df[(df['vhi'] < 40)].drop(['vhi', 'tci'], axis=1).plot.area(x='year', figsize=(11, 6))
                    elif int(vhi_correlation) == 15:

                        return df[(df['vhi'] < 15)].drop(['vhi', 'tci'], axis=1).plot.area(x='year', figsize=(11, 6))
                    else:

                        return df[(df['vhi'] < 35)].drop(['vhi', 'tci'], axis=1).plot.area(x='year', figsize=(11, 6))

            elif year_end:

                if year_begin:
                    return df[df['year'].between(int(year_begin), int(year_end))].drop(['vhi', 'tci'], axis=1).plot.area(x='year', figsize=(11, 6))
                else:

                    return df[df['year'] == int(year_end)].drop(['vhi', 'tci'], axis=1).plot.area(x='year', figsize=(11, 6))
            else:
                return df.drop(['vhi', 'tci'], axis=1).plot.area(x='year', figsize=(11, 6))

        elif vhi_rate:
            df = self.plot_maker_vh()

            if year_begin:
                if vhi_rate and not year_end:
                    if vhi_rate == '0':
                        return df[(df['year'] == int(year_begin)) & (df['5%'] + df['10%'] + df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '5':
                        return df[(df['year'] == int(year_begin)) & (df['10%'] + df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '10':
                        return df[(df['year'] == int(year_begin)) & (df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '15':
                        return df[(df['year'] == int(year_begin)) & (df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '20':
                        return df[(df['year'] == int(year_begin)) & (df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '25':
                        return df[(df['year'] == int(year_begin)) & (df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '30':
                        return df[(df['year'] == int(year_begin)) & (df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '35':
                        return df[(df['year'] == int(year_begin)) & (df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '40':
                        return df[(df['year'] == int(year_begin)) & (df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '45':
                        return df[(df['year'] == int(year_begin)) & (df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '50':
                        return df[(df['year'] == int(year_begin)) & (df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '55':
                        return df[(df['year'] == int(year_begin)) & (df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '60':
                        return df[(df['year'] == int(year_begin)) & (df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '65':
                        return df[(df['year'] == int(year_begin)) & (df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '70':
                        return df[(df['year'] == int(year_begin)) & (df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '75':
                        return df[(df['year'] == int(year_begin)) & (df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '80':
                        return df[(df['year'] == int(year_begin)) & (df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '85':
                        return df[(df['year'] == int(year_begin)) & (df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '90':
                        return df[(df['year'] == int(year_begin)) & (df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '95':
                        return df[(df['year'] == int(year_begin) & df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '100':
                        return df[(df['year'] == int(year_begin) & df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    else:
                        return df.plot.area(x='year', figsize=(11, 6))

                elif vhi_rate and year_end:
                    if vhi_rate == '0':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['5%'] + df['10%'] + df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '5':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['10%'] + df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '10':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '15':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '20':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '25':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '30':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '35':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '40':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '45':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '50':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '55':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '60':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '65':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '70':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '75':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '80':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '85':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '90':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '95':
                        return df[(df['year'].between(int(year_begin), int(year_end)) & df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_rate == '100':
                        return df[(df['year'].between(int(year_begin), int(year_end)) & df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                    else:
                        return df.plot.area(x='year', figsize=(11, 6))

            elif vhi_rate and not year_begin:
                if vhi_rate == '0':
                    return df[(df['year']) & (df['5%'] + df['10%'] + df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                elif vhi_rate == '5':
                    return df[(df['year']) & (df['10%'] + df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                elif vhi_rate == '10':
                    return df[(df['year']) & (df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                elif vhi_rate == '15':
                    return df[(df['year']) & (df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                elif vhi_rate == '20':
                    return df[(df['year']) & (df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                elif vhi_rate == '25':
                    return df[(df['year']) & (df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                elif vhi_rate == '30':
                    return df[(df['year']) & (df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                elif vhi_rate == '35':
                    return df[(df['year']) & (df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                elif vhi_rate == '40':
                    return df[(df['year']) & (df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                elif vhi_rate == '45':
                    return df[(df['year']) & (df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                elif vhi_rate == '50':
                    return df[(df['year']) & (df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                elif vhi_rate == '55':
                    return df[(df['year']) & (df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                elif vhi_rate == '60':
                    return df[(df['year']) & (df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                elif vhi_rate == '65':
                    return df[(df['year']) & (df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                elif vhi_rate == '70':
                    return df[(df['year']) & (df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                elif vhi_rate == '75':
                    return df[(df['year']) & (df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                elif vhi_rate == '80':
                    return df[(df['year']) & (df['85%'] + df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                elif vhi_rate == '85':
                    return df[(df['year']) & (df['90%'] + df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                elif vhi_rate == '90':
                    return df[(df['year']) & (df['95%'] + df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                elif vhi_rate == '95':
                    return df[(df['year'] & df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                elif vhi_rate == '100':
                    return df[(df['year'] & df['100%'] < 15)].plot.area(x='year', figsize=(11, 6))
                else:
                    return df.plot.area(x='year', figsize=(11, 6))

        elif vhi_mild and not vhi_rate:
            df = self.plot_maker_vh()

            if year_begin:
                if vhi_mild and not year_end:
                    if vhi_mild == '0':
                        return df[(df['year'] == int(year_begin)) & (df['5%'] + df['10%'] + df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '5':
                        return df[(df['year'] == int(year_begin)) & (df['10%'] + df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '10':
                        return df[(df['year'] == int(year_begin)) & (df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '15':
                        return df[(df['year'] == int(year_begin)) & (df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '20':
                        return df[(df['year'] == int(year_begin)) & (df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '25':
                        return df[(df['year'] == int(year_begin)) & (df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '30':
                        return df[(df['year'] == int(year_begin)) & (df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '35':
                        return df[(df['year'] == int(year_begin)) & (df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '40':
                        return df[(df['year'] == int(year_begin)) & (df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '45':
                        return df[(df['year'] == int(year_begin)) & (df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '50':
                        return df[(df['year'] == int(year_begin)) & (df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '55':
                        return df[(df['year'] == int(year_begin)) & (df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '60':
                        return df[(df['year'] == int(year_begin)) & (df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '65':
                        return df[(df['year'] == int(year_begin)) & (df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '70':
                        return df[(df['year'] == int(year_begin)) & (df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '75':
                        return df[(df['year'] == int(year_begin)) & (df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '80':
                        return df[(df['year'] == int(year_begin)) & (df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '85':
                        return df[(df['year'] == int(year_begin)) & (df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '90':
                        return df[(df['year'] == int(year_begin)) & (df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '95':
                        return df[(df['year'] == int(year_begin) & df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '100':
                        return df[(df['year'] == int(year_begin) & df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    else:
                        return df.plot.area(x='year', figsize=(11, 6))

                elif vhi_mild and year_end:
                    if vhi_mild == '0':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['5%'] + df['10%'] + df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '5':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['10%'] + df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '10':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '15':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '20':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '25':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '30':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '35':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '40':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '45':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '50':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '55':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '60':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '65':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '70':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '75':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '80':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '85':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '90':
                        return df[(df['year'].between(int(year_begin), int(year_end))) & (df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '95':
                        return df[(df['year'].between(int(year_begin), int(year_end)) & df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    elif vhi_mild == '100':
                        return df[(df['year'].between(int(year_begin), int(year_end)) & df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                    else:
                        return df.plot.area(x='year', figsize=(11, 6))

            elif vhi_mild and not year_begin:
                if vhi_mild == '0':
                    return df[(df['year']) & (df['5%'] + df['10%'] + df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                elif vhi_mild == '5':
                    return df[(df['year']) & (df['10%'] + df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                elif vhi_mild == '10':
                    return df[(df['year']) & (df['15%'] + df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                elif vhi_mild == '15':
                    return df[(df['year']) & (df['20%'] + df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                elif vhi_mild == '20':
                    return df[(df['year']) & (df['25%'] + df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                elif vhi_mild == '25':
                    return df[(df['year']) & (df['30%'] + df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                elif vhi_mild == '30':
                    return df[(df['year']) & (df['35%'] + df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                elif vhi_mild == '35':
                    return df[(df['year']) & (df['40%'] + df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                elif vhi_mild == '40':
                    return df[(df['year']) & (df['45%'] + df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                elif vhi_mild == '45':
                    return df[(df['year']) & (df['50%'] + df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                elif vhi_mild == '50':
                    return df[(df['year']) & (df['55%'] + df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                elif vhi_mild == '55':
                    return df[(df['year']) & (df['60%'] + df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                elif vhi_mild == '60':
                    return df[(df['year']) & (df['65%'] + df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                elif vhi_mild == '65':
                    return df[(df['year']) & (df['70%'] + df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                elif vhi_mild == '70':
                    return df[(df['year']) & (df['75%'] + df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                elif vhi_mild == '75':
                    return df[(df['year']) & (df['80%'] + df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                elif vhi_mild == '80':
                    return df[(df['year']) & (df['85%'] + df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                elif vhi_mild == '85':
                    return df[(df['year']) & (df['90%'] + df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                elif vhi_mild == '90':
                    return df[(df['year']) & (df['95%'] + df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                elif vhi_mild == '95':
                    return df[(df['year'] & df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                elif vhi_mild == '100':
                    return df[(df['year'] & df['100%'] < 35)].plot.area(x='year', figsize=(11, 6))
                else:
                    return df.plot.area(x='year', figsize=(11, 6))
if __name__ == '__main__':
    socket = SpyreServer()
    socket.launch(host='0.0.0.0', port=8888)
