# usuwanie pliku
import os
if os.path.exists("file4.txt"):
  os.remove("file4.txt")
else:
  print("Ten plik nie istnieje")