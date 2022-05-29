from app import sum

def test_sum():
    assert sum(2,3)==5

def test_sum2():
    assert sum(3,2)==5

def test_sum3():
    assert sum(0,0)==0