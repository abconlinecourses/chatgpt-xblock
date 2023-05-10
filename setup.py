"""Setup for chatgptxblock XBlock."""


import os

from setuptools import setup


def package_data(pkg, roots):
    """Generic function to find package_data.

    All of the files under each of the `roots` will be declared as package
    data for package `pkg`.

    """
    data = []
    for root in roots:
        for dirname, _, files in os.walk(os.path.join(pkg, root)):
            for fname in files:
                data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}


setup(
    name='chatgpt-xblock',
    version='0.1',
    description='chatgpt XBlock',   # TODO: write a better description.
    license='AGPL-3.0',
    author='Isanka Wijerathne, abconlinecourses.com',
    author_email='isankadn@gmail.com',
    packages=[
        'chatgptxblock',
    ],
    install_requires=[
        'XBlock',
        'openai'
    ],
    entry_points={
        'xblock.v1': [
            'chatgptxblock = chatgptxblock:ChatgptXBlock',
        ]
    },
    package_data=package_data("chatgptxblock", ["static", "public"]),
)
