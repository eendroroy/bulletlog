**logtrail**
============

.. image:: https://badge.fury.io/py/logtrail.svg
    :target: https://badge.fury.io/py/logtrail
.. image:: https://travis-ci.org/eendroroy/logtrail.svg?branch=master
    :target: https://travis-ci.org/eendroroy/logtrail
.. image:: https://codeclimate.com/github/eendroroy/logtrail/badges/gpa.svg
    :target: https://codeclimate.com/github/eendroroy/logtrail
.. image:: https://codecov.io/gh/eendroroy/logtrail/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/eendroroy/logtrail

A tool to display bar-chart anywhere.

**installation**

use pip

::

.   $ pip install logtrail

**usage**

.. image:: https://asciinema.org/a/122942.png
    :target: https://asciinema.org/a/122942

:: 

.   >>> import logtrail
.   >>> logtrail.Logger.info("calling 'logtrail.logger.info'")
.   >>> logtrail.Logger.debug("calling 'logtrail.logger.debug'")
.   >>> logtrail.Logger.warn("calling 'logtrail.logger.warn'")
.   >>> logtrail.Logger.error("calling 'logtrail.logger.error'")
.   >>> logtrail.Logger.i("calling 'logtrail.logger.i'")
.   >>> logtrail.Logger.d("calling 'logtrail.logger.d'")
.   >>> logtrail.Logger.w("calling 'logtrail.logger.w'")
.   >>> logtrail.Logger.e("calling 'logtrail.logger.e'")


**license**

*MIT*

.. image:: https://app.fossa.io/api/projects/git%2Bhttps%3A%2F%2Fgithub.com%2Feendroroy%2Flogtrail.svg?type=large
    :target: https://app.fossa.io/projects/git%2Bhttps%3A%2F%2Fgithub.com%2Feendroroy%2Flogtrail?ref=badge_large
