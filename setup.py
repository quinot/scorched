import os
from setuptools import setup, find_packages

version = '0.1'

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()


setup(name='elainepy',
      version=version,
      description="",
      long_description=README + '\n\n' + CHANGES,
      classifiers=[],
      keywords='solr tow sunburnt offspring',
      author='(Josip Delic) Lugensa GmbH',
      author_email='info@lugensa.com',
      url='http://www.lugensa.com',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          "setuptools",
          "requests",
          "nose",
          "coverage",
          "pytz",
      ],
      setup_requires=["setuptools_git"],
      )
