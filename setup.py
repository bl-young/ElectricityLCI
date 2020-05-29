from distutils.core import setup

setup(
    name='ElectricityLCI',
    version='1.0alpha',
    packages=['electricitylci'],
    package_data={'electricitylci': ["data/*.*", "output/*.*"]},
    url='https://github.com/USEPA/ElectricityLCI',
    license='CC0',
    author='Wesley Ingwersen',
    author_email='ingwersen.wesley@epa.gov',
    description='Create life cycle inventory data for regionalized electricity generation, mix of generation, mix of consumption, and distribution to the end-user in the United States.',
    install_requires=[
        'fedelemflowlist @ git+https://github.com/USEPA/Federal-LCA-Commons-Elementary-Flow-List@v1.0.2#egg=fedelemflowlist',
        'StEWI @ git+https://github.com/USEPA/standardizedinventories@v0.9.2#egg=StEWI',
        'numpy>=1.14',
        'pandas>=0.24',
        'olca-ipc>=0.0.6',
        'openpyxl>=2.5',
        'matplotlib>=2.2',
        'seaborn>=0.9',
        'sympy>=1.2',
        'xlrd>=1.1',
        'pyyaml>=5.1'
        ],
    long_description=open('README.md').read(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: IDE",
        "Intended Audience :: Science/Research",
        "License :: CC0",
        "Programming Language :: Python :: 3.x",
        "Topic :: Utilities",
    ]

)
