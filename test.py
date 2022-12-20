import requests
import pandas as pd
import numba as nb
import lxml.etree as etree


if __name__ == "__main__":
    # url = 'https://darsbazi.com/wp-content/themes/bazimooz/games/Racing%20car2/html5game/'
    # check = requests.get(url)
    #
    # data = str(check.content)
    with open('test.html' , 'r') as stream:
        data = stream.read()

    # print(data)
    cda = etree.HTML(data.replace('<pre>','').replace('</pre>',''))
    html_tables = cda.findall("body")

    ht = html_tables[0]
    table_as_list = list(ht)
    print(*(f"{v.text} \n" for v in table_as_list))

