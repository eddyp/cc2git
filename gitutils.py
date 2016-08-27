#!/usr/bin/env python2

import re
import cc2gitutils

def git_status():
	"""
	Run git status and return a list of all the valid output lines
	"""
	l = []
	debug("Not implemented",1)

	return l

def parse_git_status_line(line):
	st_index = line[0]
	st_local = line[1]
	fn = line[3:]

	return (st_index, st_local, fn)

def git_status_files(status_str_list):
	"""
	Receives a list of status lines and returns any untracked files
	that might be present in subdirectories and all the files in the
	original list
	Rationale: git status will list '?? dir/' if dir is a new dir
	           containing untracked files.
	"""
	l = []

	for s in status_str_list:
		st_idx, st_loc, fn = parse_git_status_line(s)

		if st_idx == '?' and fn[-1]=='/':
			extrafiles = rlistdir(fn, just_files=True)
			untracked_f_list = [ ' '.join('??',ef) for ef in extrafiles ]
			l.extend(untracked_f_list)
		else:
			l.append(s)

	return l
