import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import static_function

def test_fn_returns_ok():
    assert static_function() == "OK"
