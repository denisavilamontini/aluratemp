import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aluratemp",
    version="0.0.1",
    author="Denis Avila Montini",
    author_email="denisavilamontini@yahoo.com.br",
    keywords='Pacote',
    description="Este é um conjunto elementar de funções para a conversção de temperatura (Celsius - Fahrenheit)",
    long_description=long_description,
    long_description_content_type="Conversor básico de temperatura, contendo funções",
    url="https://github.com/denisavilamontini/aluratemp",
    license='MIT License',
    packages=['aluratemp'],
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Portuguese (Brazilian)',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Internationalization',
        'Topic :: Scientific/Engineering :: Physics'
    ],
    python_requires='>=3.6',
)