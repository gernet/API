from setuptools import setup, find_packages

setup(
    name ="APIfirebase",
    version ="1.0",
    packages= find_packages(),
    install_requires = ['requests','pandas','bs4','app','firebase_admin'],
)
