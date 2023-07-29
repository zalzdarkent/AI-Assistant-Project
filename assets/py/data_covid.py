import csv
import requests
from bs4 import BeautifulSoup
import os
import pandas as pd
from datetime import datetime  # Import modul datetime

url = "https://bit.ly/3jpMFRW"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
table = soup.find("table", {"class": "wikitable"})
rows = table.findAll("tr")

# Dapatkan path absolut direktori "assets/data"
dir_path = os.path.join(os.getcwd(), "assets", "data")
os.makedirs(dir_path, exist_ok=True)

# Dapatkan tanggal dan waktu saat ini
current_time = datetime.now()
formatted_time = current_time.strftime("%Y%m%d_%H%M%S")

# Bangun nama file dengan format tanggal_waktu.csv
filename = f"{formatted_time}.csv"

csv_file = os.path.join(dir_path, filename)

with open(csv_file, "wt+", newline="") as f:
    writer = csv.writer(f)
    for i in rows:
        row = []
        for cell in i.findAll(["td", "th"]):
            row.append(cell.get_text())
        writer.writerow(row)

data = pd.read_csv(csv_file, encoding='latin-1')
data.head()

# Menambahkan pesan bahwa file telah diunduh
print("File has been downloaded and saved as:", filename)
