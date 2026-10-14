Local Sphinx demo
================

This two-page documentation project uses the extension through Sphinx's normal
``extensions`` configuration. Run these commands from the repository root:

.. code-block:: console

   python3 -m venv .venv
   source .venv/bin/activate
   python -m pip install -e .
   export BIEL_PROJECT="your-project-id"
   python -m sphinx -b html -W --keep-going demo/source demo/_build/html
   python -m http.server 8000 --bind 127.0.0.1 --directory demo/_build/html

Open http://127.0.0.1:8000. Use an existing Biel project ID for live chat replies
and allow the local origin in that project's settings if required. Without
``BIEL_PROJECT``, the documentation still builds, but live chat requires a
configured project. The widget loads from the CDN, so browser testing needs
internet access.

You can optionally set ``BIEL_VERSION`` to a specific widget release before
building; it defaults to ``latest``. ``BIEL_API_KEY`` is also read when provided.
Rebuild after changing environment variables or ``demo/source/conf.py``.

Things to check
---------------

* The floating button appears on both pages and opens the assistant.
* Its label displays ``Ask "AI" <demo>`` literally, including the angle brackets.
* The header displays ``Sphinx demo — Ask AI``.
* The initial message and suggested questions appear in the assistant.
* You can enter a question and get a reply with your configured Biel project.

For an installed-package check, build a wheel with ``python -m build --wheel``
and install it into a separate environment instead of using the editable install.
The automated artifact and browser tests are documented in the root README.

The demo source stays in the repository for development. It is excluded from
published wheels and source distributions, and ``demo/_build/`` is ignored by Git.
