from setuptools import setup, find_packages


version = '0.0.0'


setup(
    name="curry",
    version=version,
    packages=find_packages(exclude=('tests*',)),
    tests_require=['tox', 'pytest', 'mock', 'wrapt'],
    author="Ivan Malison",
    author_email="ivanmalison@gmail.com",
    license="MIT",
    keywords=["curry", "functional", "partial", "partialable",
              "functools", "decorator"],
    url="https://github.com/IvanMalison/dropbox_git_sync",
)
