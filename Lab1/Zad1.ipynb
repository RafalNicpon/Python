import functools

def show_list_length(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, list):
                print(f"Długość listy w args: {len(arg)}")
        
        for k, v in kwargs.items():
            if isinstance(v, list):
                print(f"Długość listy w '{k}': {len(v)}")
                
        return func(*args, **kwargs)
    return wrapper

@show_list_length
def process_data(data_list, name):
    print(f"Przetwarzanie: {name}")

if __name__ == "__main__":
    process_data([1, 2, 3], "Test_1")
    process_data(name="Test_2", data_list=[10, 20, 30, 40])
