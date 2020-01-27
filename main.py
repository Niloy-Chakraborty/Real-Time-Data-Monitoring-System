"""
Script Name: data_extractor
Functionality: This is the main function that merges the data, creates appropriate json and call publisher to
               publish the data
Author: Niloy Chakraborty
"""

# import dependencies
import pandas as pd
import os
import pathlib
import Publisher
import random
import json


dir_name_target = "E:\\HiWi_new\\data\\"
merged_data_path= "E:\\HiWi_new\\merged_data\\"
# Give number of days to be extracted
No_Days = 15

data_dict= dict()


"""
Function Name: merge_data
Parameters: dir_name_target,merged_data_path,No_Days
Functionality: --This function reads data for each day for all the features.
               -- Merges data for each dat
               -- Iterates over each entries of the merged data
               -- calls for publish_json for each entry 
                 
Return: 
"""


def merge_data (dir_name_target,merged_data_path,No_Days):

    for j in os.listdir(dir_name_target):  # loop through items in dir
        z = 0
        while z < (No_Days - 1):
            df = pd.DataFrame()
            for item in os.listdir(dir_name_target + j + "\\"):
                print(item)

                i = os.listdir(dir_name_target + j + "\\" + item + "\\")[z]

                path = os.path.abspath(dir_name_target + j + "\\" + item + "\\" + i + "\\")
                print(path)
                path_final = merged_data_path + j + "\\"
                # create the same directory structure in the target directory
                pathlib.Path(path_final).mkdir(parents=True, exist_ok=True)
                data = pd.read_csv(path)
                print(data.shape)

                # take the Datetime only once for each day, to fasten the process
                if item == "bytes_in":
                    df["Datetime"] = data[data.columns[0]].values
                else:
                    pass
                # take other items
                df[item] = data[data.columns[1]].values

            print(df.head())
            print(df.shape)

            for index, row in df.iterrows():
                publish_json(index, row, j, df.columns)

            df.to_csv(path_final+str(i))
            z = z + 1


"""
Function Name: publish_json
Parameters: index, row, j, columns
Functionality: --This function takes each entry from the merged dataset
               -- Creates json from the entry
               -- Calls Publisher.publisher for each json

Return: 
"""


def publish_json(index, row, j, columns):
    dict_json= dict()
    dict_val= dict()
    for i in columns[1:]:
        dict_val[i]= row[i]

    dict_json["instanceId"]= j
    dict_json["timestamp"]= row[0]
    dict_json["typeId"]= "uni-stuttgart.data-center/server"
    dict_json["value"]= dict_val

    # print(dict_json)
    json_data= json.dumps(dict(dict_json))
    # print("type of published data",type(json_data))
    print(json_data)

    Publisher.publisher("guest","guest",json_data,j,row[0])


if __name__ == "__main__":
    merge_data(dir_name_target, merged_data_path, No_Days)
    # create_json()



