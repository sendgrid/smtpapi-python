import io
import os
from distutils.file_util import copy_file
from setuptools import setup, find_packages


dir_path = os.path.abspath(os.path.dirname(__file__))
readme = io.open(os.path.join(dir_path, 'README.rst'), encoding='utf-8').read()
version = io.open(
    os.path.join(dir_path, 'VERSION.txt'),
    encoding='utf-8',
).read().strip()
copy_file(os.path.join(dir_path, 'VERSION.txt'),
          os.path.join(dir_path, 'smtpapi', 'VERSION.txt'),
          verbose=0)
setup(
    name='smtpapi',
    version=version,
    author='Yamil Asusta, Kane Kim',
    author_email='yamil@sendgrid.com, kane.isturm@sendgrid.com',
    url='https://github.com/sendgrid/smtpapi-python/',
    packages=find_packages(exclude=["test"]),
    include_package_data=True,
    license='MIT License',
    description='Simple wrapper to use SendGrid SMTP API',
    long_description=readme,
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
