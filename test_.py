from dynaconfFileConf import name_check

import os
import subprocess
import sys

os.environ['FLASK_ENV'] = "test"

def test_pass():
    name=name_check()
    assert "Test Jim" == name