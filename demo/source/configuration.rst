Widget configuration
====================

Enable the extension in your Sphinx ``conf.py``:

.. code-block:: python

   extensions = ["sphinx_biel"]
   biel_project = "your-project-id"
   biel_header_title = "My documentation assistant"
   biel_button_style = "dark"

Testing different settings
--------------------------

Edit ``demo/source/conf.py`` and rebuild the site to try other settings.
Configuration names use the ``biel_`` prefix. Boolean options accept Python
``True`` and ``False``; list options accept Python lists.

The demo sets ``biel_render_math`` and ``biel_render_diagrams`` to ``False``
and supplies a list through ``biel_initial_messages``. Its button label contains
quotes and angle brackets to make plain-text rendering easy to check.

Navigate back to the home page and confirm that the button is available there
too.
