#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers='rodrigo21')
    add_depends(['libgio-2.0.so', 'libglib-2.0.so', 'libgobject-2.0.so'])
    add_provides(['libgssdp-1.2.so'])

def post_build():
    check_library_provides()
    aur_post_build()
