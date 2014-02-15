# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    name='django-pushy-articulator',
    version='0.0.1',
    author=u'Matthew D. Howell',
    author_email='matthewdhowell@gmail.com',
    packages=['pushy_articulator'],
    url='http://github.com/misterinterrupt/pushy-articulator',
    license='BSD licence, see LICENCE.txt',
    description='Create and edit articles and publish them ' + \
                'to Blogger, facebook, & Twitter'
    long_description=open('README').read(),
    zip_safe=False,
)
