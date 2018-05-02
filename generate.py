#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

import os
import json

def main():
    """docstring for main"""
    radios = os.getenv('RADIO_LIST')

    if radios is None:
        radios = [
            'http://radiostreaming.ert.gr/ert-proto',
            'http://realfm.live24.gr/realfm',
            'http://netradio.live24.gr/kanali1peiraia',
            'http://diesi.live24.gr/diesi1013',
        ]
    else:
        radios = radios.split(' ')

    items = []
    for radio in radios:
        base = os.path.basename(radio)
        new = {
            'uid': radio,
            'arg': radio,
            'title': base,
            'match': ' '.join([base, base[1:]]),
        }
        icon = find_icon(base)
        if icon is not None:
            new['icon'] = icon
        items += [new]
    print(json.dumps({
        'items': items
    }, indent=4))



def find_icon(name):
    for ending in ['png', 'jpeg']:
        fyle = os.path.join('icons', '.'.join([name, ending]))
        if os.path.exists(fyle):
            return {
                'path': fyle
            }
    return None

if __name__ == '__main__':
    main()
