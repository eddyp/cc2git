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


# rlistdir
def test_rlistdir_no_files(tmpdir):
	d = tmpdir.mkdir('a')
	li = 'a/'

	files = rlistdir(li, just_files=True)

	assert files == []

def test_rlistdir_one_subdir_file(tmpdir):

	d = tmpdir.mkdir('a')
	d = tmpdir.mkdir('a/b')
	f = d.join('c.txt')
	f.write('test')
	li = 'a/'

	oldd = tmpdir.chdir()
	files = rlistdir(li, just_files=True)
	f_and_d = rlistdir(li)
	oldd.chdir()

	assert files == ['a/b/c.txt']
	assert f_and_d == [ 'a', 'a/b', 'a/b/c.txt']

def test_rlistdir_one_file(tmpdir):

	f = tmpdir.mkdir('a').join('b.txt')
	f.write('test')
	li = 'a/'

	oldd = tmpdir.chdir()
	files = rlistdir(li, just_files=True)
	f_and_d = rlistdir(li)
	oldd.chdir()

	assert files == ['a/b.txt']
	assert f_and_d == [ 'a', 'a/b.txt']

def test_rlistdir_3_files(tmpdir):

	d = tmpdir.mkdir('a')
	f = d.join('b.txt')
	f.write('test')
	f = d.join('c.txt')
	f.write('test')
	f = d.join('d.txt')
	f.write('test')
	li = 'a/'

	oldd = tmpdir.chdir()
	files = rlistdir(li, just_files=True)
	f_and_d = rlistdir(li)
	oldd.chdir()

	assert files == ['a/b.txt', 'a/c.txt', 'a/d.txt']
	assert f_and_d == [ 'a', 'a/b.txt', 'a/c.txt', 'a/d.txt']
