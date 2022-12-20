def kwarg_print(ch: int = 36, **kwargs):
    print(*(f'\033[1;{ch}m{k} : {v} |' for k, v in kwargs.items()))


def r_kwarg_print(ch: int = 36, **kwargs):
    print(*(f'\r\033[1;{ch}m{k} : {v} |' for k, v in kwargs.items()), end='')


import requests
import shutil


def download(path, filename=None):
    filename = path.split("/")[-1] if filename is None else filename

    r = requests.get(path, stream=True)

    if r.status_code == 200:

        r.raw.decode_content = True

        with open(filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)

        print('Image successfully Downloaded: ', filename)
    else:
        print("\t\t\tImage Couldn't be received")


def fprint(*args,**kwargs):
    print('\033[1;36m',*(f"{v} " for v in args),**kwargs)