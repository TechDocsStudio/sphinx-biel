"""
ASK AI chatbot for Sphinx.

(c) 2024 - present Biel.ai
This code is licensed under MIT license (see LICENSE.md for details).
"""

__version__ = "0.1.11"

import json
from importlib.resources import files
from urllib.parse import quote

from sphinx.application import Sphinx

_WIDGET = json.loads(files(__package__).joinpath("widget_options.json").read_text())


def _script_json(value):
    encoded = json.dumps(value, ensure_ascii=False)
    for char in "<>&\u2028\u2029":
        encoded = encoded.replace(char, f"\\u{ord(char):04x}")
    return encoded


class BielExtension:
    DEFAULT_OPTIONS = {key: None for key in _WIDGET["options"]}
    DEFAULT_OPTIONS.update({
        "project": None,
        "button_position": "bottom-right",
        "button_text": "Ask AI",
        "button_style": "dark",
        "header_title": "Biel.ai chatbot",
        "version": "latest",
        # Retain the earlier config spellings as aliases of canonical widget props.
        "error_message_4_0_3": None,
        "error_message_4_0_4": None,
        "hide_think_mode_button": None,
        "think_mode_button_text": None,
    })
    ALIASES = {"error_message_4_0_3": "error_message403", "error_message_4_0_4": "error_message404"}
    LEGACY_OPTIONS = {
        "hide_think_mode_button": {"property": "hideThinkModeButton", "attribute": "hide-think-mode-button"},
        "think_mode_button_text": {"property": "thinkModeButtonText", "attribute": "think-mode-button-text"},
    }

    def __init__(self, app: Sphinx):
        self.app = app
        self.setup_options()
        self.setup_events()

    def inject_biel_scripts(self, app, pagename, templatename, context, doctree):
        version = quote(str(app.config.biel_version), safe="")
        context.setdefault("body", "")
        context["body"] += (
            '<script type="module" src="https://cdn.jsdelivr.net/npm/biel-search@'
            f'{version}/dist/biel-search/biel-search.esm.js"></script>'
        )
        if app.config.biel_button_position == "default":
            return
        props = []
        for key in self.DEFAULT_OPTIONS:
            value = getattr(app.config, f"biel_{key}")
            canonical = self.ALIASES.get(key, key)
            metadata = _WIDGET["options"].get(canonical) or self.LEGACY_OPTIONS.get(canonical)
            if value is not None and metadata:
                props.append([metadata["property"], metadata["attribute"], value])
        payload = _script_json({"props": props, "text": app.config.biel_button_text})
        context["body"] += f"""
            <script>
                window.addEventListener('DOMContentLoaded', async () => {{
                    await customElements.whenDefined('biel-button');
                    const options = {payload};
                    const bielBtn = document.createElement('biel-button');
                    options.props.forEach(([property, attribute, value]) => {{
                        bielBtn[property] = value;
                        if (attribute && (value === null || typeof value !== 'object')) {{
                            bielBtn.setAttribute(attribute, String(value));
                        }}
                    }});
                    bielBtn.textContent = options.text;
                    document.body.appendChild(bielBtn);
                }});
            </script>
        """

    def setup_options(self):
        for key, default in self.DEFAULT_OPTIONS.items():
            self.app.add_config_value(f"biel_{key}", default, "html")

    def setup_events(self):
        version = quote(str(self.app.config.biel_version), safe="")
        self.app.add_css_file(
            f"https://cdn.jsdelivr.net/npm/biel-search@{version}/dist/biel-search/biel-search.css"
        )
        self.app.connect("html-page-context", self.inject_biel_scripts)


def setup(app: Sphinx):
    BielExtension(app)
    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
