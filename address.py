# -*- encoding: utf-8 -*-
#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms

from trytond.model import ModelView, ModelSQL, fields
from trytond.pyson import Eval
from trytond.pool import Pool

STATES = {
    'readonly': ~Eval('active'),
    }
DEPENDS = ['active']

class Address(ModelSQL, ModelView):
    "Address"
    _name = 'party.address'
    
    zip = fields.Char('Zip', states=STATES, depends=DEPENDS, 
        on_change=['zip', 'city', 'subdivision', 'country'])
    
    def on_change_zip(self, vals):
        pool = Pool()
        country_zip_obj = pool.get('country.zip')
        subdivision_obj = pool.get('country.subdivision')
        res = {}
        
        if vals.get('zip'):
            country_zips = country_zip_obj.search_read([('zip', '=', vals['zip'])])
            country_zip = country_zips and country_zips[0] or False
            if country_zip:
                res['city'] = country_zip['city']
                if country_zip['subdivision']:
                    subdivision = subdivision_obj.read(country_zip['subdivision'])
                    res['subdivision'] = country_zip['subdivision']
                    res['country'] = subdivision['country']

        return res

Address()
