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
