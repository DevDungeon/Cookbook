# setup.py
# https://docs.python.org/3/distutils/setupscript.html
import os
from setuptools import setup
from sys import platform

requirements = [
    'docopt',
    'discord.py==0.16.12'
]

if platform == "win32":
    requirements.append('windows-curses')

setup(
    name = "an_example_pypi_project",
    version = "0.0.4",
    author = "Someone",
    author_email = "example@gmail.com",
    description = ("An demonstration of how to create, document, and publish "
                   "to the cheese shop a5 pypi.org."),
    license = "MIT",
    keywords = "example documentation tutorial",
    url = "http://packages.python.org/an_example_pypi_project",

    # Individual Python modules (.py files)
    py_modules=['mymodule'],
    # Directories (package)
    packages=[
        'mypackage',
        'tests'
    ],
    long_description_content_type='text/markdown',
    long_description=open('README.md').read(),
    entry_points={
        'console_scripts': [
            'foo = my_package.some_module:main_func',
            'bar = other_module:some_func',
        ],
        'gui_scripts': [
            'baz = my_package_gui:start_func',
        ]
    },
    package_data={  # Other misc files that should be installed
        'mypackage': [ 
            'data/defaults.xml',  # Relative to setup.py dir
            'data/*.dat',
        ],
    },
    python_requires='<3.7',  # Optional
    install_requires=requirements,
    platforms='any',
    classifiers=[  
        # Options at https://pypi.org/classifiers/
        'Development Status :: 1 - Planning',
        'Development Status :: 2 - Pre-Alpha',
        'Development Status :: 3 - Alpha'
        'Development Status :: 4 - Beta',
        'Development Status :: 5 - Production/Stable',
        'Development Status :: 6 - Mature',
        'Development Status :: 7 - Inactive',
        'Environment :: Console :: Curses',
        'Environment :: Win32 (MS Windows)',
        'Environment :: Web Environment',
        'Operating System :: MacOS',
        'Environment :: X11 Applications',
        'Environment :: X11 Applications :: GTK',
        'Environment :: X11 Applications :: Gnome',
        'Environment :: X11 Applications :: KDE',
        'Environment :: X11 Applications :: Qt',
        'Framework :: Django :: 4.0',
        'Framework :: Flask',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: Android',
        'Operating System :: iOS',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Utilities',
        'Topic :: Software Development',
        'Topic :: Security',
    ],
)