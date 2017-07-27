exec(open("./functions.py").read())



print("checking that function add exists: ", end = "")
add
print(" ...correct")

print("testing that add(3,4) returns 7", end = "")
assert add(3,4) == 7
print(" ...correct")

print("testing that add(-3,5) returns 2", end = "")
assert add(-3,5) == 2
print(" ...correct")

print("check that square([1,2]) returns [1,4]", end = "")
assert square([1,2]) == [1,4]
print(" ...correct")

print("check that square([2,4]) returns [4,16]", end = "")
assert square([2,4]) == [4,16]
print(" ...correct")

print("check that square(9) returns [81]", end = "")
assert square(9) == 81
print(" ...correct")



