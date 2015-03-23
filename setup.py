from setuptools import setup
import merkle_tree

setup(
   name = 'MerkleTree',
   version = merkle_tree.__version__,
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
