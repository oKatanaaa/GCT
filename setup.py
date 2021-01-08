from setuptools import setup
import setuptools

setup(
    name='GCT',
    packages=setuptools.find_packages(),
    version='1.4.1',
    description='Short tools for fast idea checking.',
    long_description='...',
    author='Kilbas Igor',
    author_email='whitemarsstudios@gmail.com',
    url='https://github.com/oKatanaaa/GCT.git',
    include_package_data=True,  # This will include all files in MANIFEST.in in the package when installing.
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ], install_requires=[]
)
