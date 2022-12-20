import os
import time
from utils.get import *
import requests
import argparse
import yaml
import lxml.etree as etree
from utils.utils import r_kwarg_print, kwarg_print, download

pars = argparse.ArgumentParser()

pars.add_argument('-url', '--url', nargs='+', type=str, default=None)
pars.add_argument('-use-method', '--use-method', action='store_true')
pars.add_argument('-links', '--links', default='data/links.yaml')
pars.add_argument('-methods', '--methods', default='data/methods.yaml')

options = pars.parse_args()

base_url = 'https://darsbazi.com/wp-content/themes/bazimooz/games/'


def create_pap_file(pap):
    if not os.path.exists(pap):
        start_path = mv = os.getcwd()
        for go_to_p in pap.split('/'):
            if not os.path.exists(go_to_p):
                os.mkdir(go_to_p)
            os.chdir(go_to_p)
            print(f'{os.getcwd()}')
            mv = mv + '/' + go_to_p
        os.chdir(start_path)
        print(f'{os.getcwd()}')
        print(f'\t\t\t\t+!+ {pap} Created +!+')


def _main(opt):
    if opt.url is None:
        with open(opt.links, 'r') as stream:
            urls = yaml.safe_load(stream)['urls']
    else:
        urls = opt.url

    methods = yaml.safe_load(open(opt.methods, 'r'))
    print(*(f'\033[1;36m{m} |\n' for m in methods))
    query = methods['methods']['game_name']
    print('\t\t\t\t Founded Games \n\t\t\t\t NAME : QUERY')
    print(*(f'\033[1;36m\t\t| {k} : {v} |\n' for k, v in query.items()))
    if not os.path.exists('games'):
        os.mkdir('games')
    os.chdir('games')
    oopa_path = os.getcwd()
    for url in urls:
        kwarg_print(url=url)
        game_name = url.split('/')[-2]

        print('\t\t\tGame Query Status :: True :: Found !')
        if not os.path.exists(f"{game_name}"):
            os.mkdir(f"{game_name}")
            pngs = methods['methods']['pngs']
            for i, png in enumerate(pngs):
                uri = f'{url}{png}'
                print(f'\t\t\t Getting Item {png}')
                print(f'\t\t\t sending Request TO : {uri}')

                path = uri.split('/')[uri.split('/').index(game_name):]
                path = os.path.join(*(k for k in path))
                pprp = path.split('/')[0:len(path.split('/')) - 1]
                pap = os.path.join(*(k for k in pprp))
                pap = pap
                create_pap_file(pap)

                data_req = requests.get(url, stream=True)

                print(f'\t\t\t Status CODE : {data_req.status_code}')
                if data_req.status_code != 200:
                    print('\t\t\t\t\t SKIP')
                else:
                    print(f'\t\t\t Saving TO {game_name}/{png}')
                    c_path = f'{game_name}/{png}'
                    gpa = c_path.split('/')
                    gpa = gpa[0:len(gpa) - 1]
                    gp = os.path.join(*(v for v in gpa))
                    cva = os.getcwd()
                    os.chdir(gp)
                    download(uri)
                    os.chdir(cva)
                    print('-' * 50)
            os.chdir(oopa_path)
            game_namee = game_name.replace('1', '').replace('2', '').replace('3', '').replace('4', '').replace('5',
                                                                                                              '').replace(
                '6', '').replace('7', '').replace('8', '').replace('9', '')

            script = url + f'html5game/{game_namee}.js'
            current = os.getcwd()
            go_to = game_name + '/html5game'
            os.chdir(go_to)
            print(f'\t\t\t\t DOWNLOADING MAIN SCRIPT : {script}')
            download(script)
            # os.chdir(current)
            for i in range(10):
                check = url + f'html5game/{game_name}_texture_{i}.png'
                print(check)
                data_check = requests.get(check, stream=True)
                if data_check.status_code == 200:
                    download(check)
                else:
                    break
        else:
            print(
                f'\t\t\t\t\033[1;33m ! WARNING ! Game folder already exists at games/{game_name} ! WARNING ! Time Pass  \033[1;36m')


        os.chdir(oopa_path)


def _on_air(url):
    get_inside_files_from_url(url=url)


if __name__ == "__main__":
    _main(opt=options)
