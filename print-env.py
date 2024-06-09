import os 
BACKEND_PATH = os.path.dirname(os.path.realpath(__file__))
STORAGE_PATH = os.path.join(BACKEND_PATH, 'storage/')

def print_backend_path():
    content = []
    content.append(str(f'BASE_PATH={BACKEND_PATH}'))
    content.append(str(f'STORAGE_PATH={STORAGE_PATH}'))
    print(BACKEND_PATH)
    print(STORAGE_PATH)
    with open('.env', 'w') as file:
        for c in content:
            file.write(f'{c}\n')
try:
    print_backend_path()
    try:
        from modules.pathData import *
        print_backend_path()
        # print('a')
    except Exception as err:
        print(err)

except Exception as err:
    print(err)





