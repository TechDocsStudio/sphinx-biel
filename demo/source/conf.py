"""Configuration for a real Sphinx project using the installed extension."""

import os

project = "Sphinx Biel demo"
author = "TechDocs Studio"
extensions = ["sphinx_biel"]
root_doc = "index"
html_theme = "alabaster"

biel_project = os.environ.get("BIEL_PROJECT")
biel_api_key = os.environ.get("BIEL_API_KEY")
biel_version = os.environ.get("BIEL_VERSION", "latest")
biel_button_text = 'Ask "AI" <demo>'
biel_button_style = "dark"
biel_header_title = "Sphinx demo — Ask AI"
biel_initial_messages = [
    {"text": "Hello! Ask me about your documentation.", "sender": "ai", "isPartial": False},
]
biel_suggested_questions = ["How do I get started?", "How do I configure the widget?"]
biel_render_math = False
biel_render_diagrams = False
