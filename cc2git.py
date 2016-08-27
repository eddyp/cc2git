#!/usr/bin/env python2

import os
import cc2gitutils
import ccutils
import gitutils
import time


since = project['vobcreation']
current_xtime = since

# list of (unconsumed) significant xtimes
lsxts = [ since ]
commit_group = {
	'mergefrombranch' : None,
	'xtime' : 0,
	'Author' : 'Nobody',
	'group' : []
	}

xnow = time.time()

def traverse_history():
	while lsxts != [] and current_xtime < xnow:
		if lsxts = []:
			current_xtime += project['timestep']
		else:
			current_xtime = lsxts[0]

		set_cs_and_go_there(current_xtime)

		if since + 1 < current_xtime:
			statusl = git_status()
			if len(statusl) == 0:
				since = current_xtime
				continue

			files_status = git_status_files(statusl)

			st_dict = parse_git_status_list(files_status)

			if has_new_or_del(st_dict):
				a_and_d = st_dict['?'], st_dict['D']
				dirs = elems_and_parents(a_and_d, noelem=True)

				parse_dirs_cc_histories(dirs, since, current_xtime)
				if current_xtime > lsxts[0]:
					continue

		# deep_analysis will return any history before 'since' with an
		# empty time stamp (i.e. hisory of a file which was hidden
		# because its parent directory was not listing it yet)
		groups = deep_analysis(since, current_xtime)

		get_groups_xtimes(groups)
		for xtime in get_groups_xtimes:
			lsxts = insert_in_sorted_list(xtime, lsxts)

		if current_xtime > lsxts[0]:
			continue

		assert (current_xtime == lsxts[0]), "Current time is not the first significant time"
		assert (len(groups) == 1), "xtime <= first significant, but found more than 1 group"

		commit_group = git_commit(groups[0], commit_group)

		assert (current_xtime == commit_group['xtime'])
		since = current_xtime
		lsxts = lsxts[1:]

