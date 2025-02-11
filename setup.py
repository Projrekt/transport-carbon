from __future__ import absolute_import
from distutils.core import setup
setup(name='transport-carbon',
      version='0.0.4',
      description='Python Transport GHG Emissions',
      long_description=open('README.rst').read(),
      author='Jamie Bull',
      author_email='jamie.bull@oco-carbon.com',
      classifiers=['Development Status :: 2 - Pre-Alpha',
                   'Intended Audience :: Developers',
                   'Intended Audience :: Science/Research',
                   'License :: OSI Approved :: MIT License',
                   'Natural Language :: English',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python :: 2.7',
                   'Topic :: Database :: Front-Ends'],
      url='https://github.com/jamiebull1/transport-carbon',
      download_url='http://windows.github.com/',
      packages=['transport_carbon'],
      package_data={'transport_carbon': ['db/*.db']},
      requires=['geopy', 'pandas', 'pygeocoder']
      )