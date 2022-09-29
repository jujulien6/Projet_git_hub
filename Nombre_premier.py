#Lire les nombre entier entre 1 et 100 000
min = 1
max = 100000
for n in range(min,max + 1):
   if n > 1:
       for i in range(2,n):
           if (n % i) == 0:
               break
       else:
           print(n)