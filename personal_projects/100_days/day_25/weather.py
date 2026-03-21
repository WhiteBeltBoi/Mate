import pandas as pd



with open("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv") as csvfile:
    df = pd.read_csv(csvfile)
    primary_color_count = df["Primary Fur Color"].value_counts().reset_index()
    primary_color_count.columns = ["Fur Color", "Count"]
    print(primary_color_count)
    primary_color_count.to_csv("squirrel_count.csv")

    # my_dict = {}
    # for row in primary_color_count:
    #     if pd.isna(row):
    #         continue
    #     if row not in my_dict:
    #         my_dict[row] = 1
    #     else:
    #         my_dict[row] += 1
    #
    # write_csv = ["Fur Color", "Count"]
    # for key, value in my_dict.items():
    #     print(f"{key}, {value}")