"""Build a site using the installed wheel; keep providers entirely out of validation."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

import sphinx
import sphinx_biel


class WheelContract(unittest.TestCase):
    def test_installed_wheel_builds_safe_configuration(self):
        self.assertNotIn('/src/', sphinx_biel.__file__)
        with tempfile.TemporaryDirectory(prefix='biel-sphinx-site-') as temporary:
            root = Path(temporary)
            text = 'Ask "quoted" 日本語 </script><script>window.injected=1</script><img src=x onerror="window.injected=2">'
            props = {
                'project': text,
                'button_text': text,
                'disable_input': True,
                'render_math': False,
                'render_diagrams': False,
                'initial_messages': [{'text': 'Hello 日本語', 'sender': 'ai', 'isPartial': False}],
                'hide_think_mode_button': False,
                'think_mode_button_text': 'Legacy 日本語',
                'error_message_4_0_3': 'Access "quoted" 日本語',
            }
            (root / 'conf.py').write_text("extensions=['sphinx_biel']\nmaster_doc='index'\n" + ''.join(f'biel_{key}={value!r}\n' for key, value in props.items()))
            (root / 'index.rst').write_text('Test documentation\n==================\n\nLocal fixture.\n')
            subprocess.run([sys.executable, '-m', 'sphinx', '-b', 'html', '-W', '--keep-going', str(root), str(root / 'build')], check=True)
            html = (root / 'build/index.html').read_text()
            self.assertNotIn('window.injected=1</script>', html)
            self.assertIn('\\u003c/script\\u003e', html)
            self.assertIn('biel-search@0.1.94', html)
            self.assertNotIn('bielBtn.innerHTML', html)
            self.assertIn('"errorMessage403", "error-message-4-0-3"', html)
            self.assertIn('"renderMath", "render-math", false', html)
            self.assertIn('"initialMessages", null, [', html)
            self.assertIn('"hideThinkModeButton", "hide-think-mode-button", false', html)
            self.assertIn('"thinkModeButtonText", "think-mode-button-text", "Legacy 日本語"', html)
            output = Path(sys.argv[1]) if len(sys.argv) > 1 else None
            if output:
                output.mkdir(parents=True, exist_ok=True)
                (output / 'index.html').write_text(html)
                (output / 'expected.json').write_text(json.dumps(props))
            print(f'PASS installed Sphinx {sphinx.__version__}: wheel metadata, real HTML build and safe serialized options')


if __name__ == '__main__':
    unittest.main(argv=[sys.argv[0]])
