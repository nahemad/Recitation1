from main import *

# 2 pts
def test_compare_search():
	res = compare_search(sizes=[10, 100])
	print(res)
	assert res[0][0] == 10
	assert res[1][0] == 100
	assert res[0][1] < 1
	assert res[1][1] < 1

# 2 pts
def test_binary_search_one():
	assert binary_search([1,2,3,4,5], 5) == 4
	assert binary_search([1,2,3,4,5], 1) == 0
	assert binary_search([1,2,3,4,5], 6) == -1

# 2 pts
def test_binary_search_two():
	assert binary_search([1,2,3,4,5], 2) == 1
	assert binary_search([], 2) == -1
