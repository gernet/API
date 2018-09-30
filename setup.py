from setuptools import setup, find_packages

setup(
    name ="APIfirebase",
    version ="1.0",
    packages= find_packages(),
    install_requires = ['requests','pandas','bs4','app','firebase_admin'],
    package_data={'realace2018-firebase-adminsdk-r7gk1-121be5edaf.json':'api/realace2018-firebase-adminsdk-r7gk1-121be5edaf.json'}
)
