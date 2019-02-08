import sys

for place in sys.path:
    print(place)
def document_it(func):
    def new_function(*args,**kwargs):
        print('it is firs:', func.__name__)
        print("Позициооные аргументы", args)
        print("ключевые аргументы", kwargs)
        result=func(*args,**kwargs)
        return result
        print('result', result)

    return new_function

def square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return new_function

@document_it
@square_it
def adds_inst(a,b):
    return a+b

b=adds_inst(3,5)

#print(b)
