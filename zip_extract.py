import os, zipfile

# with zipfile.ZipFile('data/202004-divvy-tripdata.zip', 'r') as my_zip:
    # print(my_zip.namelist())

dir_name = '/home/condexter/Documents/Projects/Cyclistic/archives'
extension = '.zip'

os.chdir(dir_name)

for item in os.listdir(dir_name):
    if item.endswith(extension):
        file_name = os.path.abspath(item)
        zip_ref = zipfile.ZipFile(file_name)
        zip_ref.extractall(path=f'../data')
        print("Extracting: ", file_name)
        zip_ref.close()
    