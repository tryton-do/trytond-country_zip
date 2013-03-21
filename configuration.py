#This file is part country_zip module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta


__all__ = ['Configuration']
__metaclass__ = PoolMeta

class Configuration:
    __name__ = 'party.configuration'

    default_prefix_zip = fields.Property(
        fields.Char('Prefix Zip', help='Default prefix country (uppercase).'))

