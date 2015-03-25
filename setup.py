import os.path
from setuptools import setup
import merkle_tree

LONG_DESCRIPTION = ""
if os.path.exists("README.md"):
    LONG_DESCRIPTION = open("README.md", "r").read()

setup(
   name = 'MerkleTree',
   version = merkle_tree.__version__,
   description='CLI to calculate Merkle Tree based on botocore implementation.',
   long_description=LONG_DESCRIPTION,
   py_modules=['merkle_tree'],
   author='George Yoshida',
   url='https://github.com/quiver/merkle_tree',
   install_requires=[
     'botocore',
     'Click',
   ],
   license=open("LICENSE").read(),
   classifiers=(
       'Development Status :: 3 - Alpha',
       'Intended Audience :: Developers',
       'Intended Audience :: System Administrators',
       'Natural Language :: English',
       'License :: OSI Approved :: Apache Software License',
       'Programming Language :: Python',
       'Programming Language :: Python :: 2.6',
       'Programming Language :: Python :: 2.7',
       'Programming Language :: Python :: 3',
       'Programming Language :: Python :: 3.3',
   ),
   entry_points='''
       [console_scripts]
       merkle=merkle_tree:cli
   '''
)
