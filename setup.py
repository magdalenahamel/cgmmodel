from setuptools import setup
#from Cython.Build import cythonize

setup(
    name="cgmmodel",
    version="0.1",
    description="Python software for modeling and synthetic spectra from an idealized CGM model",
    author="M. Hamel",
    author_email="magdalena.hamel@gmail.com",
    url="https://github.com/magdalenahamel/cgmmodel",
    packages=['cgmspec'],
    install_requires=[
        'astropy',
        'scipy',
        'matplotlib',
        'numpy'
          ])
