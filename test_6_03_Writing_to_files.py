import CSP_6_03_Writing_to_files as HW

def test_writeFile():
    assert HW.writeFile([1,2,3,4,5], "oogabooga.txt") == "oogabooga.txt"
    assert HW.writeFile([6,7,8,9],"oogabooga.txt") == "oogabooga.txt"
def test_sortNames():
    assert HW.sortNames("names.txt", "namesNew.txt") ==("namesNew.txt")

