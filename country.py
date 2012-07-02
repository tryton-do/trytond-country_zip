# -*- encoding: utf-8 -*-
#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms

from trytond.model import ModelView, ModelSQL, fields

class CountryZip(ModelSQL, ModelView):
    "Country Zip"
    _name = "country.zip"
    _description = __doc__

    zip = fields.Char('Zip', required=True, select=1)
    city = fields.Char('City', select=1)
    subdivision = fields.Many2One('country.subdivision', 'Subdivision',
            ondelete='CASCADE', select=1)

CountryZip()
