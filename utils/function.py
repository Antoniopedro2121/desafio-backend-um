from lojas.models import Lojas

import ipdb

def formatarArquivo(obj):

    entrada = [1, 4, 5, 6, 7, 8]
    saida = [2, 3, 9]

    conteudo_formatado = obj.file.read()

    objeto_parseado_loja = {
        'dono_da_loja': conteudo_formatado[48:62].decode('UTF-8'),
        'nome_loja': conteudo_formatado[62:81].decode('UTF-8')
    }

    loja = Lojas.objects.get_or_create(**objeto_parseado_loja)[0]

    objeto_parseado_trasacao = {
        'tipo': int(conteudo_formatado[0:1]),
        'data': conteudo_formatado[1:9].decode('UTF-8'),
        'valor': int(conteudo_formatado[9:19])/100,
        'cpf': conteudo_formatado[19:30].decode('UTF-8'),
        'cartao': conteudo_formatado[30:42].decode('UTF-8'),
        'hora': conteudo_formatado[42:48].decode('UTF-8'),
        'loja': loja.id
        }

    if objeto_parseado_trasacao['tipo'] in entrada:
        loja.saldo_loja = loja.saldo_loja + objeto_parseado_trasacao['valor']
        loja.save()
    else:
        loja.saldo_loja = loja.saldo_loja - objeto_parseado_trasacao['valor']
        loja.save()
    
    return objeto_parseado_trasacao