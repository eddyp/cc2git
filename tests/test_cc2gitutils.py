import pytest

from cc2gitutils import *

#class TestSortedList:
def test_insert_empty_list():
	l = insert_in_sorted_list(0, [])
	assert l == [0]

def test_insert_existing_middle():
	li = [1, 3, 6]
	l = insert_in_sorted_list(3, li)
	assert li == l

def test_insert_existing_last():
	li = [1, 3, 6]
	l = insert_in_sorted_list(6, li)
	assert li == l

def test_insert_before_all_small_list():
	l = insert_in_sorted_list(-1, [0])
	assert l == [-1, 0]

def test_insert_before_all_large_list():
	l = insert_in_sorted_list(-1, [0, 1, 3])
	assert l == [-1, 0, 1, 3]

def test_insert_after_all_small_list():
	l = insert_in_sorted_list(4, [0])
	assert l == [0, 4]

def test_insert_after_all_large_list():
	l = insert_in_sorted_list(4, [0, 1, 3])
	assert l == [0, 1, 3, 4]
