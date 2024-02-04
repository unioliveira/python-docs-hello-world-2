#def func(a):
#	return a - 1

#def test_testmethod():
#	assert func(6) == 5

def pytest_collection_modifyitems(items):
    test_name = 'test_1'
    test_index = next((i for i, item in enumerate(items) if item.name == test_name), -1)
    test_item = items.pop(test_index)
    items.append(test_item)
