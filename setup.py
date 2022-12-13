from setuptools import setup, find_packages


setup(
    
    name='tempesta_excel',
    version='1',
    license='MIT',
    author="Jose Tempesta",
    author_email='zetempesta@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/gmyrianthous/example-publish-pypi',
    keywords='example project',
    install_requires=[
          'scikit-learn',
      ],

)