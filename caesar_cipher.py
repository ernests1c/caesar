 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encrypted(t, o): # define funkciju e ''encrypted'' un tas rotaciju apli
  r = ""
  for c in t: # 
    if (a.find(c) == -1): # ja a atrod c tad tiek nonemts viens burts
      r += c
    else: # ja neatrod c tad tiek pievienots viens burts
      r += (a[(a.find(c) + o) % len(a)])
  return r

def decrypted(t, o): # define burtu d ''decrypted'' un tas rotaciju apli
  r = ""
  for c in t: # cikls kas tiek izmantots lai parveidotu burtus
    if (a.find(c) == -1): # ja a atrod c tad tiek nonemts viens burts
      r += c
    else: 
      r += (a[(a.find(c) - o) % len(a)]) #
  return r 

w = """
1. Encrypt text
2. Decrypt text
3. Bruteforce all rotations
Choose mode: """
mode = int(input(w))

if mode == 1:# ja ievada 1, tiek printēts teksts un prasa ievadit rotaciju
  text = input("Enter the text: ")
  rotation = int(input("Enter the rotation: "))
  print("Encrypted: " + encrypted(text, rotation))
elif mode == 2:# ja ievada 2, tiek printēts teksts un prasa ievadit rotaciju
  text = input("Enter the text: ")
  rotation = int(input("Enter the rotation: "))
  print("Decrypted: " + decrypted(text, rotation))
elif mode == 3:# ja ievada 2, tiek printēts teksts un prasa ievadit rotaciju
  print("Bruteforcing...")
  print("But I don't know how to do it, sorry ¯\_(ツ)_/¯")
