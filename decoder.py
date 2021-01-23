class decoding:

 def decrypt(self,key,str):
      import string
      l = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation + " \n"
      key = [l.index(x)+1 for x in key]
      n = 0
      decrypted = ""
      for c in str:
         n += 1
         c_num = l.index(c)
         k = key[n%len(key)-1]-1
         if k > c_num:
            decrypted += l[c_num+len(l)-k]
         else:
            decrypted += l[c_num-k]
      print(decrypted)
      return decrypted

 '''str2 = "FM JWOUWFJL"
 n = 0
 encrypted = ""

 for c in str:
     n += 1
     ind = l.index(c)
     num = ind + l.index(key[n%len(key)-1])
     num = num%len(l)
     encrypted += l[num]
 print(encrypted)
 '''