import csv
import sys
import pandas as pd

def read_dict(file):
    df = pd.read_csv(file).head()
    df_t = df.T
    df.to_csv("men1.csv", header=True, index=False)
    with open("men1.csv", newline = "") as f:
        read_dict = csv.DictReader(f, delimiter=",", quotechar='"')
        ks = read_dict.fieldnames
        return_dict = {k: [] for k in ks}

        for row in read_dict:
            for k, v in row.items():
                return_dict[k].append(v)

    return return_dict


def write_csv(file, save_dict):
    with open(file,'w') as f:
        writer = csv.DictWriter(f, fieldnames=save_dict.keys(),delimiter=",",quotechar='"')
        writer.writeheader()
        writer.writerow(save_dict)
