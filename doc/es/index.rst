========================
Códigos postales de país
========================

Ayuda en la introducción de direcciones.

Calcula los campos país, subdivisión y ciudad a partir del código postal. Esta
información debe ser previamente introducida. En el caso de códigos postales
españoles, se debe instalar el módulo `Códigos postales de España`_

.. _Códigos postales de España: ../country_zip_es/index.html

En el formulario de las direcciones de la empresa, podemos introducir el código
postal y Tryton nos rellenará automáticamente la ciudad, la subdivisión y el
país a que corresponde ese código postal.

Por ejemplo, el código ES08720, rellenará los campos:

* Localidad: Vilafranca del Penedès,
* Provincia: Barcelona,
* País: España.

.. warning::  Si la localidad que le da relacionado con el código postal no es el deseado,
              siempre puede cambiar el que se le ofrece por otro. Este módulo sólo
              ayuda a autocompletar información con datos existentes.


Configuración
-------------

En la configuración del tercero puede añadir el prefijo por defecto los códigos postales.
En el caso de España, puede añadir el prefijo 'ES'. De este modo, al crear un nuevo
tercero ya dispondrá del código y con sólo escribir el número ya se autocompletará
con la localidad.


Módulos de los que depende
==========================

Instalados
----------

.. toctree::
   :maxdepth: 1

   /country/index
   /party/index

Dependencias
------------

* `País`_
* Terceros_

.. _País: ../country/index.html
.. _Terceros: ../party/index.html
