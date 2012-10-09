# -*- encoding: utf-8 -*-
#This file is part country_zip module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.

from trytond.model import ModelView, ModelSQL, fields
from trytond.pyson import Eval
from trytond.pool import Pool

__all__ = ['Address']

STATES = {
    'readonly': ~Eval('active'),
    }
DEPENDS = ['active']

class Address(ModelSQL, ModelView):
    "Address"
    __name__ = 'party.address'
    
    zip = fields.Char('Zip', states=STATES, depends=DEPENDS, 
        on_change=['zip', 'city', 'subdivision', 'country'])
    
    def on_change_zip(self):
        res = {}
        Zip = Pool().get('country.zip')
        Subdivision = Pool().get('country.subdivision')

        if self.zip:
            country_zips = Zip.search_read([('zip','=',self.zip)])
            country_zip = country_zips and country_zips[0] or False
            if country_zip:
                res['city'] = country_zip['city']
                if country_zip.get('subdivision'):
                    subdivisions = Subdivision.read([country_zip['subdivision']])
                    res['subdivision'] = country_zip['subdivision']
                    res['country'] = subdivisions[0]['country']

        return res
