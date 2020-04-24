from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='numpyencoder',
    version='0.2.0',
    author='Hunter M. Allen',
    author_email='allenhm@gmail.com',
    license='MIT',
    #packages=find_packages(),
    packages=['numpyencoder'],
    install_requires=['numpy>=1.14.3'],
    description='Python JSON encoder for handling Numpy data types.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/hmallen/numpyencoder',
    keywords=['numpy', 'json', 'encoder'],
    classifiers=(
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ),
)
