from setuptools import setup, find_packages

setup(
    name='helga-haskell',
    use_hg_version=True,
    author="Cary M. Robbins",
    author_email="carymrobbins@gmail.com",
    url="",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        # 'helga',
        # 'tryhaskell',
    ],
    entry_points=dict(
        helga_plugins=[
            'haskell = helga_haskell:haskell',
        ],
    ),
)
