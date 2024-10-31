from myPackage import myModule

def test_top_n():
    assert myModule.top_n([8, 3, 2, 7, 4], 3) == [8, 7, 4] , 'incorrect'