"""
Contributors extension for Sphinx.
(c) 2018 - present David Garcia (@dgarcia360)
# This code is licensed under MIT license (see LICENSE.md for details)
"""

__version__ = "0.1.0"

"""
Feedback widget for Sphinx.
(c) 2023 - present PushFeedback.com
# This code is licensed under MIT license (see LICENSE.md for details)
"""

from sphinx.application import Sphinx


options = {
    'custom_font': None,
    'error_message': None,
    'error_message_4_0_3': None,
    'error_message_4_0_4': None,
    'modal_title': None,
    'modal_title_success': None,
    'modal_title_error': None,
    'modal_position': None,
    'send_button_text': None,
    'project': None,
    'screenshot_button_tooltip_text': None,
    'screenshot_topbar_text': None,
    'email': None,
    'email_placeholder': None,
    'message_placeholder': None,
    'button_style': None,
    'button_position': 'bottom-right',
    'hide_icon': None,
    'hide_screenshot_button': None,
}

def snake_to_kebab(string):
    """Convert snake_case string to kebab-case."""
    return string.replace('_', '-')

def setup(app: Sphinx):
    # Add our static path
    app.add_css_file('https://cdn.jsdelivr.net/npm/pushfeedback/dist/pushfeedback/pushfeedback.css')

    for key in options.keys():
        app.add_config_value(f'pushfeedback_{key}', options[key], 'html')

    app.connect('html-page-context', inject_feedback_scripts)

def inject_feedback_scripts(app, pagename, templatename, context, doctree):
    feedback_js_module = '''
        <script type="module" src="https://cdn.jsdelivr.net/npm/pushfeedback/dist/pushfeedback/pushfeedback.esm.js"></script>
    '''
    context['body'] += feedback_js_module

    if getattr(app.config, "pushfeedback_buttonPosition", None) != "default":
        attributes = ' '.join([
            f'{snake_to_kebab(key)}="{getattr(app.config, f"pushfeedback_{key}")}"'
            for key in options.keys() if getattr(app.config, f"pushfeedback_{key}") is not None
        ])
        feedback_script = f'''
            <script>
                window.addEventListener('DOMContentLoaded', (event) => {{
                    let feedbackBtn = document.createElement("feedback-button");
                    feedbackBtn.setAttribute('{attributes}');
                    document.body.appendChild(feedbackBtn);
                }});
            </script>
        '''
        context['body'] += feedback_script
