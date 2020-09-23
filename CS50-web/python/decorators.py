# They can take function as input and return modified function

def announce(f):
    def wrapper():
        print("About to run the function")
        f()
        print("Done with the function.")
    return wrapper

@announce                   # Telling to wrap hello() around the decorator announce
def hello():
    print("Hello, World!")

hello()