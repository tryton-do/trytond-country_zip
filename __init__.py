#This file is part country_zip module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.
from trytond.pool import Pool
from .configuration import *
from .address import *

def register():
    Pool.register(
        Configuration,
        Address,
        module='country_zip', type_='model')
