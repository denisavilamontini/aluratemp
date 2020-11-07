from setuptools import setup

setup(
	name = 'conversor_temp',
	version = '1.0.0',
	description = 'Um simples conversor de temperatura (Celsius - Fahrenheit)',
	long_description = 'Um simples conversor de temperatura, com funcoes para conversao de Celsius para Fahrenheit e vice-versa, usado para um post no Blog da Alura',
	url = 'https://github.com/yanorestes/aluratemp',
	author = 'Denis Avila Montini',
	author_email = 'denisavilamontini@yahoo.com.br',
	license = 'MIT',
	classifiers = [
		'Development Status :: 5 - Production/Stable',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Natural Language :: Portuguese (Brazilian)',
		'Operating System :: OS Independent',
		'Topic :: Software Development :: Internationalization',
		'Topic :: Scientific/Engineering :: Physics'
	],
	keywords = 'conversor temperatura',
	project_urls = {
		'Código fonte': 'https://github.com/denisavilamontini/conversor_temp',
		'Download': 'https://github.com/denisavilamontini/conversor_temp/archive/1.0.0.zip'
	},
	packages = ['conversor_temp']
)