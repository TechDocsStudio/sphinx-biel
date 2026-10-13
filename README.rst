AI chatbot extension for Sphinx
===============================

Ask AI chatbot plugin for Sphinx sites, powered by `Biel.ai <https://biel.ai>`_.

.. image:: https://docs.biel.ai/assets/images/biel-widget-docs-bd28548cf26a37bcb7c496487280bbfe.png
   :alt: AI chatbot Sphinx

Add an AI chatbot to your Sphinx documentation using Biel.ai's extension. The integration works with any Sphinx theme, including Read the Docs, and adds both chat and search capabilities.

**Note:** A Biel.ai plan is required to use this plugin. Try it free for 14 days—no credit card required.

Key features
------------

- AI chatbot that provides instant responses to documentation queries.  
- AI search engine for quick and relevant information retrieval.  
- Integration with Sphinx.  
- Customizable to match your site's branding and user needs.  

Get started
-----------

See the `Sphinx AI chatbot integration guide <https://docs.biel.ai/installation/sphinx>`_ for installation and setup instructions, including `selecting a widget version <https://docs.biel.ai/installation/sphinx#select-a-widget-version>`_.

The extension loads the widget's JavaScript and CSS from the CDN. It uses
``latest`` by default; set ``biel_version`` in ``conf.py`` to choose a specific
release. You do not need to install ``biel-search`` with npm.

Support
-------

Need assistance? `Contact us <https://docs.biel.ai/support>`_ for help.

License
-------

Copyright (c) 2024 Biel.ai

Licensed under the `MIT License <LICENSE>`_.

Development
-----------

For a reusable Sphinx project to test locally, see ``demo/README.rst``.
The demo is excluded from published wheels and source distributions.

Widget option metadata is included in the Python package. To refresh it, unpack
the published widget and run
``python tools/update_widget_options.py /path/to/biel-search``. This reads the
widget's property definitions without executing its JavaScript.

Build with ``python -m build --wheel``, install the wheel in a separate Sphinx
environment, and run ``python tests/test_artifact.py /tmp/biel-sphinx-site``.
This checks the generated HTML, typed settings and version overrides.

The browser test also needs Puppeteer and a local widget package for its test
fixtures. Set ``NODE_PATH`` to that test environment's ``node_modules`` and run
``PUPPETEER_EXECUTABLE_PATH=/path/to/chrome node tests/browser-contract.cjs /tmp/biel-sphinx-site``.
It uses local sample replies to check the button and chatbot settings.
