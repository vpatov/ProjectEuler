from distutils.core import setup

setup(
    name='projecteuler',
    version='0.1.0',
    author='Vasia Patov',
    author_email='vasiapatov@gmail.com',
    packages=['projecteuler', 'projecteuler.utils'],
    install_requires=[
      'bitstring',
      'colorama'
    ],
    include_package_data=True
)
