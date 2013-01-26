#!/usr/bin/python

import jinja2
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

copies = [
    {
        'name': 'generic',
        'id': 'generic',
        'logo': '',
    },
    {
        'name': 'dropbox',
        'id': 'bcvo',
        'logo': 'dropbox.png',
    },
    {
        'name': 'twitch',
        'id': 'gubk',
        'logo': 'twitch.png',
    },
    {
        'name': 'blizzard',
        'id': 'rohc',
        'logo': 'blizzard.gif',
        'logo_style': 'background-color: black;',
    },
    {
        'name': 'riot',
        'id': 'keok',
        'logo': '',
        'logo_style': '',
    },
    {
        'name': 'reddit', # NOT USED YET
        'id': 'nlcs',
        'logo': '',
        'logo_style': '',
    },
    {
        'name': 'blizz_ibb',
        'id': 'knsz',
        'logo': '',
        'logo_style': '',
    },
    {
        'name': 'twit_blizz_ibb',
        'id': 'taei',
        'logo': '',
        'logo_style': '',
    },
    {
        'name': 'facebook', # NOT USED YET
        'id': 'oyau',
        'logo': '',
        'logo_style': '',
    },
]

html = open('secret_template.html', 'rb').read()
template = jinja2.Template(html)

for info in copies:
    rendered = template.render(**info)
    fname = '%s.html' % info['id']
    with open(fname, 'wb') as f:
        f.write(rendered)


