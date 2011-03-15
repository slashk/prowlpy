=======
Prowlpy
=======

| Originally Written by Jacob Burch <jacoburch@gmail.com>, 7/6/2009
| Modified by Olivier Hervieu <olivier.hervieu@gmail.com>
| Updated for Prowl API 1.2 by Ken Pepple, 3/5/2011

Python module for posting to the iPhone Push Notification service Prowl: http://www.prowlapp.com/

Dependencies:
=============
The socket module must be compiled with SSL support.

Coming Backwards Incompatible Changes for 0.6
=====================================
- Anything referencing '*apikey' will be renamed to api_key
- the package is now in a prowlpy directory, not python. the python directory will be removed

- `Distribute`_
- `Buildout`_
- `modern-package-template`_

.. _Buildout: http://www.buildout.org/
.. _Distribute: http://pypi.python.org/pypi/distribute
.. _`modern-package-template`: http://pypi.python.org/pypi/modern-package-template
