from byotest import assert_equal

def add (x,y):
    return x + y




assert_equal(add(5,3), 8)
assert_equal(add(2,4), 6)
assert_equal(add(2,2), 4)
assert_equal(add(-1,-5), -6)
assert_equal(add(-7,2), -5)
assert_equal(add(0,0), 0)
assert_equal(add(65535,1), 65536)


print("All test pass")





assert add(5,3) == 8
assert add(2,4) == 6
assert add(2,2) == 4
# assert add(2.3,3.4) == 5.7 Float numbers arent as precise and small as we think!
assert add(-1,-5) == -6
assert add(-7,+2)  == -5
assert add(0,0) == 0
assert add(65535,1) == 65536







print("All test pass")