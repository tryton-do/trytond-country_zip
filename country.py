#This file is part country_zip module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.model import ModelView, ModelSQL, fields

__all__ = ['CountryZip']


class CountryZip(ModelSQL, ModelView):
    'Country Zip'
    __name__ = 'country.zip'
    _rec_name = 'zip'
    zip = fields.Char('Zip', required=True, select=1)
    city = fields.Char('City', select=1)
    subdivision = fields.Many2One('country.subdivision', 'Subdivision',
        ondelete='CASCADE', select=1)
    country = fields.Function(fields.Many2One('country.country', 'Country'),
            'get_country', searcher='search_country'
        )

    def get_country(self, name):
        return self.subdivision.country.id

    @classmethod
    def search_country(cls, name, clause):
        return [('subdivision.%s' % name,) + tuple(clause[1:])]
