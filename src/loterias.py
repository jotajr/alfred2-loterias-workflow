import urllib2
import json
import io
import os


def mega_request():
    response = urllib2.urlopen('http://developers.agenciaideias.com.br/loterias/megasena/json')

    data = json.load(response)

    mega_file = "mega.json"

    try:
        os.remove(mega_file)
    except OSError:
        pass

    with io.open(mega_file, 'w', encoding='utf-8') as f:
        f.write(unicode(json.dumps(data, ensure_ascii=False)))


def mega_concurso():

    mega_request()

    with open('mega.json') as data_file:
        data = json.load(data_file)

    result = "Concurso: " + data['concurso']['numero'] + " - Data: " + data['concurso']['data']

    print(result)


def mega_num_sorteados():

    with open('mega.json') as data_file:
        data = json.load(data_file)

    sorteados = ""

    for item in data['concurso']['numeros_sorteados']:
        sorteados = sorteados + str(item) + " "

    print(sorteados)


def mega_ganhadores():

    with open('mega.json') as data_file:
        data = json.load(data_file)

    result = "Ganhadores: " + data['concurso']['premiacao']['sena']['ganhadores']

    print(result)


def mega_acumulada():

    with open('mega.json') as data_file:
        data = json.load(data_file)

    result = "Acumulado: R$ " + data['concurso']['valor_acumulado']

    print(result)


def quina_request():
    response = urllib2.urlopen('http://developers.agenciaideias.com.br/loterias/quina/json')

    data = json.load(response)

    quina_file = "quina.json"

    try:
        os.remove(quina_file)
    except OSError:
        pass

    with io.open(quina_file, 'w', encoding='utf-8') as f:
        f.write(unicode(json.dumps(data, ensure_ascii=False)))


def quina_concurso():

    quina_request()

    with open('quina.json') as data_file:
        data = json.load(data_file)

    result = "Concurso: " + data['concurso']['numero'] + " - Data: " + data['concurso']['data']

    print(result)


def quina_num_sorteados():

    with open('quina.json') as data_file:
        data = json.load(data_file)

    sorteados = ""

    for item in data['concurso']['numeros_sorteados']:
        sorteados = sorteados + str(item) + " "

    print(sorteados)


def quina_ganhadores():

    with open('quina.json') as data_file:
        data = json.load(data_file)

    result = "Ganhadores: " + data['concurso']['premiacao']['quina']['ganhadores']

    print(result)


def quina_acumulada():

    with open('mega.json') as data_file:
        data = json.load(data_file)

    result = "Acumulado: R$ " + data['concurso']['valor_acumulado']

    print(result)


def federal_request():
    response = urllib2.urlopen('http://developers.agenciaideias.com.br/loterias/loteriafederal/json')

    data = json.load(response)

    fed_file = "federal.json"

    try:
        os.remove(fed_file)
    except OSError:
        pass

    with io.open(fed_file, 'w', encoding='utf-8') as f:
        f.write(unicode(json.dumps(data, ensure_ascii=False)))


def federal_concurso():
    federal_request()

    with open('federal.json') as data_file:
        data = json.load(data_file)

    result = "Concurso: " + data['concurso']['numero'] + " - Data: " + data['concurso']['data']

    print(result)


def federal_premios():

    with open('federal.json') as data_file:
        data = json.load(data_file)

    result = " 1 - " + data['concurso']['premiacao']['premio_1']['bilhete'] + " - "
    result += "2 - " + data['concurso']['premiacao']['premio_2']['bilhete'] + " - "
    result += "3 - " + data['concurso']['premiacao']['premio_3']['bilhete'] + " - "
    result += "4 - " + data['concurso']['premiacao']['premio_4']['bilhete'] + " - "
    result += "5 - " + data['concurso']['premiacao']['premio_5']['bilhete']

    print(result)
