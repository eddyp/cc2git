#!/usr/bin/env python2

import os


dbg_threshold = 4
def debug(msg, lvl=7):
	if lvl <= dbg_threshold:
		print ("DBG(%d):%s\n" % (lvl, msg))


def rlistdir(dirfn, just_files=False):
	flist = []

	if not just_files:
		flist.append(dirfn.rstrip('/'))

	for root, dirs, files in os.walk(dirfn):
		if root[-1] == '/':
			root = root[:-1]
		for f in files:
			flist.append('/'.join([root, f]))
		if not just_files:
			for d in dirs:
				flist.append('/'.join([root,d]))

	flist = list(set(flist))
	flist.sort()

	return flist


def elems_and_parents(files_list, noelem=False):
	"""
	Receives a list of files and returns a list of all the parent directories.
	If noelem=True, the files themselves are not listed
	"""
	l = []

	debug("Not yet implemented",1)

	return l


def insert_in_sorted_list(x, sl):

	if sl == []:
		return [x]

	if x in sl:
		return sl

	left = 0
	right = len(sl) - 1

	while True:
		pos = left + (right - left) / 2

		if x < sl[pos]:
			right = pos - 1
		else:
			left = pos + 1

		if right < left:
			break

	l = sl[:right + 1]
	l.append(x)
	l.extend(sl[right + 1:])

	return l


def xtime_from_cctime(cctime):
	debug("Not yet implemented",1)
	return 0


def cc_hist(element, since, until):
	debug("Not yet implemented",1)
	return []


def insert_elhist_xtimes_in_significants(hist, sincextime):
	"""
	Receive a pythonified history of an element an inject in the ordered list of
	significant xtimes (lsxts) the times of modifications. For directories,
	the second immediate before the change is inserted, too.
	"""
	global lsxts

	for ver in hist:
		xtime_ver = xtime_from_cctime(ver['ccdate'])

		ante = xtime_ver - 1
		if sincextime < ante:
			lsxts = insert_in_sorted_list(ante, lsxts)

		if sincextime < xtime_ver:
			lsxts = insert_in_sorted_list(xtime_ver, lsxts)


def parse_dirs_cc_histories(dirs, since, current_xtime):
	"""
	For each d in dirs analyze ClearCase history since 'since' and inject into the
	global lsxts the times of the directory changes (dc) and dc-1
	xtimes
	"""
	for d in dirs:
		dir_hist = cc_hist(d, since, current_xtime)
		insert_elhist_xtimes_in_significants(dir_hist, since)
