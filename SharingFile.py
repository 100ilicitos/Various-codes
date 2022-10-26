# Cloud file sharing 
# by Busyman.Inc

# pip install gofile

import gofile as go
def Store_Files(file):
  cur_server = go.getServer()
  print(cur_server)
  url = go.uploadFile(file)
  print("Download Link:", url["downloadPage"])
Store_Files("/content/sample_data/mnist_test.csv") 
