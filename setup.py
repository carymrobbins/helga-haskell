from setuptools import setup, find_packages

setup(
    name='helga-haskell',
    version='0.1.0',
    author="Cary M. Robbins",
    author_email="carymrobbins@gmail.com",
    url="https://github.com/carymrobbins/helga-haskell",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        'helga',
        'tryhaskell',
    ],
    entry_points=dict(
        helga_plugins=[
            'haskell = helga_haskell:haskell',
        ],
    ),
)
