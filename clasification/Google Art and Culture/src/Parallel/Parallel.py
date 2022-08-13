from ast import arg
from concurrent.futures import ThreadPoolExecutor

def parallel(fun,values):
    result =[]
    with ThreadPoolExecutor(max_workers=None) as exe: 
        print('Running')
        result = exe.map(fun,values)
    return list(result)

