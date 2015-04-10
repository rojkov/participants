import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "participants",
    version = "0.0.1",
    author = "Dmitry Rozhkov",
    author_email = "dmitry.rojkov@gmail.com",
    description = ("Participants."),
    license = "GPL",
    keywords = "workflow",
    url = "http://packages.python.org/an_example_pypi_project",
    packages = ['participants', 'participants.tasks'],
    install_requires = [
    ],
    long_description=read('README.rst'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: GPL License",
    ]
)
