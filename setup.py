import os
import subprocess

print("initialising virtual environment")

subprocess.run(r"python -m venv venv && venv\Scripts\activate && pip install -r requirements.txt", shell=True)

print("virtual environment installed")

import requests
import zipfile

url = 'https://s3-eu-west-1.amazonaws.com/static.oc-static.com/prod/courses/files/Parcours_data_scientist/Projet+-+Donn%C3%A9es+%C3%A9ducatives/Projet+Python_Dataset_Edstats_csv.zip'

print("fetching csv data")

if not os.path.exists('csv_data'):
    os.makedirs('csv_data')

    with open("Projet+Python_Dataset_Edstats_csv.zip", "wb") as f :
        f.write(requests.get(url, allow_redirects=True).content)

    with zipfile.ZipFile("Projet+Python_Dataset_Edstats_csv.zip", 'r') as zip_ref:
        zip_ref.extractall("csv_data")
        info = zipfile.ZipInfo("csv_data")
        info.external_attr = 777

    os.remove(r"Projet+Python_Dataset_Edstats_csv.zip")

print("csv data recovered")

print("launch jupyter notebook")

subprocess.run(r'venv\Scripts\activate && jupyter notebook Projet_2_OpenClassrooms.ipynb', shell=True)