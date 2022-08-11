from ast import arg
from concurrent.futures import ThreadPoolExecutor


'''def fun(x):
    return x+1

lista = [1,2,3,4,5,6,7,8,9,10]


result =[]
with ThreadPoolExecutor(max_workers=3) as exe: 
    print('Running')
    result = exe.map(fun,lista)

print(list(result))
print('End')'''

def myfun(a,b):
    return a+b+1

def parallel(fun,args):
    return fun(*args)

print(parallel(myfun,(5,10)))