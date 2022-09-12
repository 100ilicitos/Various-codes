# Lock your Photos
# By Busyman.INc

# pip install cryptography

from cryptografy.fernet import Fernet
key = Fernet.generate_key()
with open('key.key', 'wb') as f:
  f.write(key)

fernet = Fernet(key)
with open('image.jpg', 'rb') as f:
  Photo = f.read()

lock = fernet.encrypt(Photo)
with open('image.jpg', 'wb') as lock_Photo:
  lock_Photo.write(lock)
  
print("Your Photo is lock")
