from setuptools import setup, find_packages

setup(
    name='imgconvert',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'pillow',  # ou outras dependências
    ],
    entry_points={
        'console_scripts': [
            'imgconvert=cli.cli_app:main',
        ],
    },
)
