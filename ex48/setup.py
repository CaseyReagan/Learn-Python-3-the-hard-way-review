try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description' : 'ex48',
	'author': 'Reagan',
	'url': 'URL to get it at.',
	'download_url': 'where to download it.',
	'author_email': 'caseyreagan@163.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['ex48'],
	'scripts': [],
	'name': 'Projectname'
}

setup(**config)