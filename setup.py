from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='1.5',
    packages=find_packages(exclude=['test']),
    license='MIT',  
    description='A short description of myPackage',
    long_description=open('README.md').read(),
    author='Amobi Ndubuisi',
    author_email='amobi.mc@gmail.com',
    url='https://github.com/username/repository',
)

