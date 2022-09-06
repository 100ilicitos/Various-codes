# Unzip file
# By Busyman.Inc

# pip install zip

from zipfile import ZipFile
with ZipFile('Files.zip', 'r') as zip_object:
    zip_object.extractall()

print(zip_object.namelist())
