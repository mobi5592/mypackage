from mypackage import myModule


def test_top_n():
    """
    Make sure function works properly
    """

    assert myModule.top_n([3,5,2,65,23,4], 3) == [65, 23, 5], 'incorrect'
    assert myModule.top_n([2,5,3,6,9,1], 2) == [9, 6], 'incorrect'