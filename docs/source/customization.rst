Customization
-------------

The directive ``contributors`` generates an ``<ul>`` node with class ``sphinx-pushfeedback``.
This makes the list is highly customizable through CSS.

.. tip:: See how to `add custom CSS to Sphinx Documentation <https://docs.readthedocs.io/en/stable/guides/adding-custom-css.html>`_.

For example, the following CSS snippet makes the images round:

.. code-block:: css

  .sphinx-pushfeedback img {
      border-radius: 50%;
  }
