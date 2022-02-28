n = int(input())

pat = '*'

while n > 1: 
    pat = '''
   {pat} + {pat} + {pat}
   {pat} + {pat} + {pat}
   {pat} + {pat} + {pat}
   '''
        
print(pat)




