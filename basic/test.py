import csv
from config.var_config import data_dir


def csv2dict(in_file):
    new_dict = {}
    lst_key = []
    lst_value=[]
    with open(in_file, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        fieldnames = next(reader)
        reader = csv.DictReader(f, fieldnames=fieldnames, delimiter=',')
        for row in reader:
            for key, value in row.items():
                lst_key.append(key)
                lst_value.append(value)
        for key, value in zip(lst_key, lst_value):
            new_dict[key] = value

    return new_dict


def row_csv2dict(csv_file):
    dict_club={}
    with open(csv_file, 'r')as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            dict_club[row[0]] = row[1]
            dict_club[row[2]] = row[3]
            dict_club[row[4]] = row[5]
    return dict_club


def csv2dict1( filename, delimiter = ',', has_header = True, text_columns = None ):

    # Open the csv file, extract the first line and initialize the data dict
    csvreader = csv.reader(open(filename, 'rb'), delimiter=delimiter)
    first_line = next(csvreader)
    data = {}

    # If there's a header line, use the items in the first line to generate the dict keys
    # If there isn't, use numeric keys and put the first item already in the data arrays
    if has_header:
        for item in first_line:
            data[item] = []
    else:
        counter = 0
        for value in first_line:
            if text_columns and counter in text_columns:
                data[counter] = [value]
            else:
                data[counter] = [to_float(value)]
            counter += 1

    # Extract the rest of the data
    for line in csvreader:
        if has_header:
            for key, value in zip( first_line, line ):
                if text_columns and key in text_columns:
                    data[key].append(value)
                else:
                    data[key].append(to_float(value))

        else:
            for key, value in zip( range(len(line)), line ):
                if text_columns and key in text_columns:
                    data[key].append(value)
                else:
                    data[key].append(to_float(value))

    # Return the extracted data
    return data

# Extract a float from a string and return a NaN if not possible
def to_float( str_value ):

    number = None

    try:
        number = float( str_value )
    except ValueError:
        number = float('nan')

    return number

def csv2dict_update(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f, skipinitialspace=True)
        header = next(reader)
        csv_dict = [dict(zip(header, map(int, row))) for row in reader]
        return csv_dict

if __name__ == '__main__':
    print(csv2dict_update(data_dir+'multi_record_1.csv'))
    # print(csv2dict(data_dir+'multi_record_1.csv'))


