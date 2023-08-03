sphinx-pushfeedback
===================

``sphinx-pushfeedback`` is a Sphinx extension that helps you recognize the people who have contributed to an open-source project.

.. image:: https://raw.githubusercontent.com/dgarcia360/sphinx-pushfeedback/master/docs/source/_static/example_avatars.png

Features
---------

**Celebrate contributions**

Show the list of users who have contributed to a repository in your docs.

**Configurable**

Choose how many contributors show and sort them by the number of commits.

Supported platforms
---------------------

``sphinx-pushfeedback`` only works with GitHub public repositories.

Installation
------------

#. Install ``sphinx-pushfeedback`` using PIP.

   .. code-block:: bash

      pip install sphinx-pushfeedback


#. Add the extension to your Sphinx project ``conf.py`` file.

   .. code-block:: python

      extensions = ['sphinx_pushfeedback']

Usage
-----

Using the directive:

.. code-block:: rst

   ..  contributors:: sphinx-doc/sphinx

Renders:

.. image:: https://raw.githubusercontent.com/dgarcia360/sphinx-pushfeedback/master/docs/source/_static/example.png

Check out the full documentation for more customizable options at https://sphinx-pushfeedback.readthedocs.io/

Contributing
------------

We encourage public contributions!
Please review `CONTRIBUTING <https://sphinx-pushfeedback.readthedocs.io/en/latest/contribute.html>`_ for details on our code of conduct and development process.

License
-------

Copyright (c) 2018 - present David Garcia (`@dgarcia360 <https://twitter.com/dgarcia360>`_).

Licensed under the `MIT License <https://github.com/dgarcia360/sphinx-pushfeedback/blob/main/LICENSE.md>`_.
