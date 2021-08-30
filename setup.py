import pathlib

from setuptools import setup

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(

    name='DigitalLogicAnalysis',

    version='0.0.0',

    description='Digital Logic Analysis tool.',

    long_description=long_description,

    long_description_content_type='text/markdown',

    url='https://github.com/DevinDeSilva/DigitalLogicAnalysis.git',

    author='DevinDeSilva',

    author_email='devin.18@cse.mrt.ac.lk',

    keywords='DigitalElectronics , LearningTools',

    packages=['DigitalLogicAnalysis'],

    python_requires='>=3.5, <4',

    install_requires=['numpy', 'pandas', 'matplotlib'],

    extras_require={
        'dev': ['check-manifest',
                'pytest>=3.7'],
        'test': ['coverage', 'unittest'],
    },

    # package_data={  # Optional
    #     'sample': ['package_data.dat'],
    # },

    # data_files=[('my_data', ['data/data_file'])],  # Optional

    # entry_points={  # Optional
    #     'console_scripts': [
    #         'hello=sample:main',
    #     ],
    # },

    project_urls={  # Optional
        'Bug Reports': 'https://github.com/DevinDeSilva/DigitalLogicAnalysis/issues',
        'Source': 'https://github.com/DevinDeSilva/DigitalLogicAnalysis/',
    },
)
