from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='python-bits-and-peace',
      version='0.0.1',
      description='This repository brings together useful Python bits often used in any Project for peace of mind.',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
      ],
      keywords='structure template',
      url='https://github.com/tkivisik/python-bits-and-peace',
      author='Taavi Kivisik',
      license='MIT',
      packages=['python-bits-and-peace'],
      test_suite='nose.collector',
      tests_require=['nose', 'nose-cover3'],
      zip_safe=False)
