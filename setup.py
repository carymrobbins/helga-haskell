from setuptools import setup, find_packages

setup(
    name='helga-haskell',
    version='0.1.1',
    author="Cary M. Robbins",
    description='Evaluate Haskell expressions using helga!',
    author_email="carymrobbins@gmail.com",
    url="https://github.com/carymrobbins/helga-haskell",
    packages=find_packages(),
    py_modules=['helga_haskell'],
    license='BSD3',
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        'tryhaskell',
    ],
    entry_points=dict(
        helga_plugins=[
            'haskell = helga_haskell:haskell',
        ],
    ),
)
