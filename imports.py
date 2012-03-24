import os
import sys

APP_DIR = os.path.abspath(os.path.dirname(__file__))

sys.path.insert(0, os.path.join(APP_DIR, 'libs'))

"""
sys.path.insert(0, os.path.join(APP_DIR, 'third_party'))

if 'google' in sys.modules:
  orig_google_module = sys.modules['google']
  del sys.modules['google']
  # Import google from our path, including third_party
  import google
"""