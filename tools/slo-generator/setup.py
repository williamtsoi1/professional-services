# Copyright 2018 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#            http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='slo-generator',
      version='0.1.6',
      description='SLO generator',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='Google Inc.',
      author_email='brunoreboul@google.com,ocervello@google.com',
      packages=find_packages(exclude=['contrib', 'docs', 'tests']),
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Topic :: Software Development :: Build Tools',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
      ],
      keywords='slo sli generator gcp',
      install_requires=[
          'google-api-python-client', 'oauth2client', 'google-cloud-monitoring',
          'google-cloud-pubsub', 'google-cloud-bigquery',
          'prometheus-http-client', 'pyyaml', 'opencensus'
      ],
      entry_points={
          'console_scripts': ['slo-generator=slo_generator.cli:main',],
      },
      python_requires='>=3.0')
