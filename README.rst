===========
Django demo
===========

|python-versions|

Introductie
===========

Deze code is onderdeel van een presentatie voor Bit Academy ter introductie van
Python en Django. De code is **geen** voorbeeld van hoe je goede of nette code
schrijft maar geeft een idee van de kracht en mogelijkheden van het Django 
framework.

In dit project kan een gebruiker zelf een formulier configureren en beschikbaar
stellen via de admin. Als een gebruiker het formulier invult, worden de 
antwoorden opgeslagen in de database.


Aan de slag
===========

Python installeren:

.. code:: bash

   $ sudo apt-get install python
   $ sudo apt-get install python-virtualenv

Project downloaden en installeren:

.. code:: bash

   $ git clone https://github.com/joeribekker/django-demo
   $ cd django-demo
   $ virtualenv env
   $ source env/bin/activate
   $ pip install -r requirements.txt

Configureren en starten:

.. code:: bash

   $ python manage.py migrate  # Initialize the database
   $ python manage.py createsuperuser  # Create an admin user
   $ python manage.py runserver  # Start the development webserver


Licentie
========

Licensed under the `MIT`_.

.. _`MIT`: LICENSE.md

.. |python-versions| image:: https://img.shields.io/badge/python-3.8-blue.svg
    :alt: Supported Python versions
