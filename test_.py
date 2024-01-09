from dynaconfFileConf import name_check

def test_pass():
    name=name_check()
    assert "Test Jim" == name