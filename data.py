import urllib.request

#Loops through each dictionary in lst. Creates a new list of the values associated with the key, k, in each dictionary.

def unique_values(k, lst):
  retVal = []
  for arrestDict in lst:
    for key in arrestDict.keys():
      if k == key:
        val = arrestDict[key]
        if not val in retVal:
          retVal.append(val)
  return retVal
  
#Returns a list of all dictionaries in lst that have the given key-value pair.

def filter_list(k, v, lst):
  retVal =[]
  for arrestDict in lst:
    if arrestDict[k] == v:
      retVal.append(arrestDict)
  return retVal

# Takes two lists of strings as parameters. Takes string with matching index from both lists and adds them to dictionary as a key-value pair.

def dict_gen(keys, values):
  retVal = {}
  index = 0
  for value in values:
    key = keys[index]
    retVal[key] = value
    index += 1
  return retVal

# Loops through each key in the list, keys. Looks in dictionary, dic, for value associated with the key. Appends that value to new list and returns said list.
    
def get_values(keys, dic):
  retVal = []
  for key in keys:
    value = dic.get(key)
    retVal.append(value)
  return retVal

import csv

# Takes a csv file as the parameter and returns the values in the header as a list.

def header_reader(f_in):
  with open(f_in) as f:
    csv_read = csv.reader(f)
    headers = next(csv_read)
    return headers

# Takes a csv file as the parameter and returns a list of lists, with each list being a row from the file.
    
def data_reader(f_in):
  retVal = []
  with open(f_in) as f:
    csv_read = csv.reader(f)
    headers = next(csv_read)
    for row in csv_read:
      retVal.append(row)
  return retVal

# Takes a list of strings and a csv file as parameters. Overwrites content in the file and adds the list of strings as a row to the file
  
def header_writer(lst, f_out):
  with open(f_out, "w") as f:
    csv_write = csv.writer(f)
    csv_write.writerow(lst)

# Takes a list of lists and a csv file as parameters. Appends each list in lst as a row to the file.

def data_writer(lst, f_out):
  with open(f_out, "a") as f:
    csv_write = csv.writer(f)
    for list in lst:
      csv_write.writerow(list)

import json
import urllib

# Function 1

def clean_list(k, lst):
  retval = []
  for dict in lst:
    if k in dict.keys():
      retval.append(dict)
  return retval

# Function 2

def data_reader_alt(f_in):
  retVal = []
  with open(f_in) as f:
    csv_read = csv.reader(f)
    headers = next(csv_read)
    for row in csv_read:
      retVal.append(row)
  return [retVal, headers]

def cache_reader(f_in):
  retval = []
  reader_val = data_reader_alt(f_in)
  data = reader_val[0]
  headers = reader_val[1]
  for list in data:
    retdict = {}
    for i in range(len(headers)):
      retdict[headers[i]] = list[i]
    retval.append(retdict)
  return retval
 
# Function 3

def cache_writer(lst, f_out):
  for dict in lst:
    header = dict.keys()
  header_writer(header, f_out)
  with open(f_out, "a") as f:
    csv_write = csv.writer(f)
    for dict in lst:
      content = dict.values()
      csv_write.writerow(content)

# Function 4

def retrieve_json(url):
  request = urllib.request.urlopen(url)
  content = request.read().decode()
  retval = json.loads(content)
  return retval





# PROJECT 4 FUNCTIONS

def line_data_gen():
  retval = {}
  list_of_dicts = cache_reader("cache.csv")
  list_of_dates = unique_values("arrest_date", list_of_dicts)
  list_of_dates.sort()
  retval["x"] = list_of_dates
  y_values = []
  for date in list_of_dates:
    acc = 0
    list_dicts_date = filter_list("arrest_date", date, list_of_dicts)
    for dict in list_dicts_date:
      acc += 1
    y_values.append(acc)
  retval["y"] = y_values
  return retval

def pie_data_gen():
  retval ={}
  total_arrests = 0
  list_of_dicts = cache_reader("cache.csv")
  list_of_boroughs = unique_values("arrest_boro", list_of_dicts)
  list_all_arrests = data_reader("cache.csv")
  for arrest in list_all_arrests:
    total_arrests += 1
  borough_val = []
  for borough in list_of_boroughs:
    num_arrests = 0
    for dict in list_of_dicts:
      if dict["arrest_boro"] == borough:
        num_arrests += 1
    percent_arrests = (num_arrests / total_arrests) * 100
    borough_val.append(percent_arrests)
  retval["values"] = borough_val  
  borough_names = ["Queens", "Brooklyn", "The Bronx", "Manhattan", "Staten Island"]
  retval["labels"] = borough_names
  retval["type"] = "pie"
  return retval

def bar_data_gen(borough):
  retval = {}
  borough_name = borough.lower()
  borough_names_code = {"queens": "Q", "brooklyn": "K", "the bronx": "B", "manhattan": "M", "staten island": "S"}
  list_of_dicts = cache_reader("cache.csv")
  list_of_ages = unique_values("age_group", list_of_dicts)
  retval["x"] = list_of_ages
  boro_code = borough_names_code[borough_name]
  boro_list = filter_list("arrest_boro", boro_code, list_of_dicts)
  y_retval = []
  for age_group in list_of_ages:
    acc = 0
    list_by_age = filter_list("age_group", age_group, boro_list)
    for dict in list_by_age:
      acc += 1
    y_retval.append(acc)
  retval["y"] = y_retval
  retval["type"] = "bar"
  retval = [retval]
  retval.append(borough)
  return retval
  
  