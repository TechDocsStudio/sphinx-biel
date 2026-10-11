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

See the `Sphinx AI chatbot integration guide <https://docs.biel.ai/installation/sphinx>`_ for installation and setup instructions.

Support
-------

Need assistance? `Contact us <https://docs.biel.ai/support>`_ for help.

License
-------

Copyright (c) 2024 Biel.ai

Licensed under the `MIT License <LICENSE>`_.

Widget compatibility and development
------------------------------------

The default CDN artifact is pinned to ``biel-search`` 0.1.94. Set ``biel_version`` explicitly to select another published artifact (including ``latest``). Options are generated from that published widget collection; quote/Unicode/script-closing values are serialized safely, booleans remain booleans, arrays/objects become properties after the element is defined, and ``biel_button_text`` is literal text. The previous error-message and think-mode config spellings remain accepted for compatibility. ``biel_button_position = "default"`` still suppresses the floating button.

The installed-wheel matrix passed real HTML builds on Sphinx 7.4.7, 8.2.3 and 9.1.0 with Python 3.13.3. The package declares Python >=3.9 and Sphinx >=7,<10; use a Python version supported by your selected Sphinx release. Browser checks use the actual pinned widget with synthetic API/WS, local module assets and blocked external requests.

Build with ``python -m build --wheel``, install the wheel into an isolated Sphinx environment, and run ``python tests/test_artifact.py /tmp/biel-sphinx-site``. With Puppeteer 24.43.1 and biel-search 0.1.94 installed in a separate local Node tool directory, set NODE_PATH to its node_modules and run ``PUPPETEER_EXECUTABLE_PATH=/path/to/trusted/chrome node tests/browser-contract.cjs /tmp/biel-sphinx-site``. This checks literal labels, safe script serialization, false booleans, arrays, the button event and actual bot props.

To refresh option metadata, unpack the chosen published widget and run ``python tools/update_widget_options.py /path/to/biel-search``; review the generated metadata/version and repeat the wheel/framework/browser checks. The generator reads compiler-emitted property JSON without executing JavaScript. No hand-copied widget declarations are maintained.

This pin selects the currently published 0.1.94 artifact. The separate widget sanitizer/dependency remediation is not yet published in that artifact; update this pin deliberately after its release and repeat the artifact/browser matrix.
