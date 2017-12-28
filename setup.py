from setuptools import setup

#converts markdown to reStructured
try:
    import pypandoc
except ImportError:
    print("Install pypandoc to generate the field long_description")
    pypandoc = None
if pypandoc:
    long_description = "\n\n".join([
        pypandoc.convert('README.md', 'rst', format='markdown'),
    ])
else:
    long_description = "[pypandoc missing]"

setup(name='jsonconfigreader',
      version='1.1.6',
      description='Python JSON configuration reader and parser',
      long_description=long_description,
      author='Andrei Surzhan',
      author_email='surzhan.a.y@gmail.com',
      url='https://github.com/AndreySurzhan/jsonconfigreader',
      packages=['jsonconfigreader'],
      install_requires=[
          'pypandoc'
      ],
      classifiers=[
          'Topic :: Utilities',
          'Intended Audience :: Developers',
          'Intended Audience :: Other Audience',
          'Operating System :: Microsoft :: Windows :: Windows 10',
          'Operating System :: MacOS',
          'Operating System :: Unix',
          'Programming Language :: Python'
          ]
      )
