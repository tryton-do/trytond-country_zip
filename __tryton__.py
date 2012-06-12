# -*- encoding: utf-8 -*-
#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms

{
    'name' : 'Country, Subdivision and City from Zip',
    'name_es_ES': 'País, subdivisión y ciudad a partir de código postal',
    'name_ca_ES': 'País, subdivisió i ciutat a partir de codi postal',
    'version' : '0.0.2',
    'author' : 'Zikzakmedia SL',
    'email': 'zikzak@zikzakmedia.com',
    'website': 'http://www.zikzakmedia.com/',
    'description': '''This module helps the encoding of addresses.
It computes the Country, Subdivision and City fields from the Zip code. These information must be previously encoded.
''',
    'description_es_ES': '''Este módulo ayuda en la codificación de direcciones.
Calcula los campos país, subdivisión y ciudad a partir de código postal. Esta información debe ser previamente introducida.
''',
    'description_ca_ES': '''Aquest mòdul ajuda a la codificació d'adreces.
Calcula els camps país, subdivisió i ciutat a partir de codi postal. Aquesta informació ha de ser previament intruïda.
''',
    'depends' : [
        'party',
        'country',
    ],
    'xml' : [
        'country.xml',
    ],
    'translation': [
        'locale/ca_ES.po',
        'locale/es_ES.po',
    ],
}
