#This file is part country_zip module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.model import fields
from trytond.pyson import Eval
from trytond.pool import Pool, PoolMeta

__all__ = ['Address']
__metaclass__ = PoolMeta


class Address:
    "Address"
    __name__ = 'party.address'

    @classmethod
    def __setup__(cls):
        super(Address, cls).__setup__()
        if cls.zip.on_change is None:
            cls.zip.on_change = []
        for field in ('zip', 'city', 'subdivision', 'country'):
            if not field in cls.zip.on_change:
                cls.zip.on_change.append(field)

    @staticmethod
    def default_zip():
        Configuration = Pool().get('party.configuration')
        config = Configuration(1)
        if config.default_prefix_zip:
            return config.default_prefix_zip

    def on_change_zip(self):
        res = {}
        Zip = Pool().get('country.zip')
        Subdivision = Pool().get('country.subdivision')

        if self.zip:
            zips = Zip.search([('zip', '=', self.zip)])
            if zips:
                zip_ = zips[0]
                res['city'] = zip_.city
                if zip_.subdivision:
                    res['subdivision'] = zip_.subdivision.id
                    res['country'] = (zip_.subdivision.country.id
                        if zip_.subdivision.country else None)
        return res
