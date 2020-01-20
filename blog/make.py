#!/usr/local/bin/python

import os
import time

print '[j]ekyll'
print '[g]o live'
print '?'

task = raw_input().strip().lower()

if task == 'j':
    os.system('jekyll')
    print('check http://yuvalg.com/draftblog')

if task == 'g':
    backup_fn = 'backup%s' % time.strftime('%Y-%m')

    if os.path.exists(backup_fn):
        os.system('rm -rf %s' % backup_fn)

    os.system('mv live %s' % backup_fn)
    os.system('mv _site live')

