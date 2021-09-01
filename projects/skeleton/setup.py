try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description' : 'My Project',
	'author': 'Reagan',
	'url': 'URL to get it at.',
	'download_url': 'where to download it.',
	'author_email': 'caseyreagan@163.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['NAME'],
	'scripts': [],
	'name': 'Projectname'
}

setup(**config)