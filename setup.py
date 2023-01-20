import os

print("initialising virtual environment")

os.system(r"python -m venv venv")
os.system(r"venv\Scripts\activate")
os.system(r"pip install -r requirements.txt")

print("virtual environment installed")

import requests
import zipfile

url = 'https://s3-eu-west-1.amazonaws.com/static.oc-static.com/prod/courses/files/Parcours_data_scientist/Projet+-+Donn%C3%A9es+%C3%A9ducatives/Projet+Python_Dataset_Edstats_csv.zip'

print("fetching csv data")

if not os.path.exists('csv_data'):
    os.makedirs('csv_data')

with open("Projet+Python_Dataset_Edstats_csv.zip", "wb") as f :
    f.write(requests.get(url, allow_redirects=True).content)

print("csv data recovered")

with zipfile.ZipFile("Projet+Python_Dataset_Edstats_csv.zip", 'r') as zip_ref:
    zip_ref.extractall("csv_data")

os.remove(r"Projet+Python_Dataset_Edstats_csv.zip")

print("launch jupyter notebook")

os.system(r"venv\Scripts\activate")
os.system(r'jupyter notebook "Projet 2 OpenClassrooms.ipynb"')