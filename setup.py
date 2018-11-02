import os
import re
from setuptools import setup

# def readme():
#     with open('README.rst') as f:
#         return f.read()

def get_version(*file_paths):
    """Retrieves the version from django_task/__init__.py"""
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    version_file = open(filename).read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')

version = get_version("toggl_projects", "__init__.py")
readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(name='toggl_projects',
      version=version,
      description='Script to download a projects summary from Toggl in CSV format',
      long_description=readme + '\n\n' + history,
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.6',
          'Topic :: Database :: Database Engines/Servers',
          'Topic :: Internet',
      ],
      keywords='toggl',
      url='https://github.com/morlandi/toggl_projects',
      author='Mario Orlandi',
      author_email='morlandi@brainstorm.it',
      license='MIT',
      scripts=['bin/toggl_projects'],
      packages=['toggl_projects'],
      # install_requires=[
      #     'TogglPy',
      # ],
      dependency_links=[
          #'https://github.com/morlandi/TogglPy.git',
          'https://github.com/morlandi/toggl_projects/archive/master.zip',
      ],
      include_package_data=False,
      zip_safe=False)
