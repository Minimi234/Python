# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
not (x or y or z) == (not x and not y and not z)
print('x', 'y', 'z', '  X ⋁ Y', '  X ⋁ Y ⋁ Z','  ¬(X ⋁ Y ⋁ Z)', '  ¬x', '¬y', '¬z', '  ¬X ⋀ ¬Y', '  ¬X ⋀ ¬Y ⋀ ¬Z' )
for x in range(0,2):
    for y in range(0,2):
         for z in range(0,2):
              if x==0 and y==0:
                 a=0
              else: a=1
              if a==0 and z==0:
                 b=0
              else: b=1
              if b==0:
                 c=1
              else: c=0
              if x==0 :
                 x2=1
              else: x2=0
              if y==0 :
                 y2=1 
              else: y2=0     
              if z==0 :
                 z2=1 
              else: z2=0
              if x2==1 and y2==1:
                 a2=1
              else: a2=0 
              if a2==1 and z2==1:
                 b2=1
              else: b2=0    
              print(x, y, z,'   ', a,'       ', b, '           ',c, '        ',  x2, y2, z2, '     '
             , a2,'          ', b2)
print('при любых значениях x, y, z, утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z - будет справедливо ')           
           
for x in range(2):
   for y in range(2):
      for z in range(2):
         print(f'x={x}, y={y}, z={z}')
         print(not (x or y or z) == (not x and not y and not z))