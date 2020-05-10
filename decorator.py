import time

def timer(orginalFunc):
    def calculate(*args,**kwargs):
        def Error():
            print('Error')
        try:
            start = time.time()
            funcResult =orginalFunc(*args,**kwargs)
            finish = time.time()
            print('İşlem süresi',finish-start)
            return funcResult
        except Exception as exception:
            print('Error',exception)
        return Error()
    return calculate

@timer
def fonk(sayi):
    for i in range(100000):
        sayi+=0
    return sayi

print(fonk(5))
