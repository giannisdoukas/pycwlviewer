import codecs
import os.path

from setuptools import setup

name = 'pycwlviewer'


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


with open(os.sep.join([os.path.abspath(os.path.dirname(__file__)), "README.md"]), "r") as fh:
    long_description = fh.read()

setup(
    name=name,
    version=get_version(f"{name}/__init__.py"),
    packages=['pycwlviewer'],
    package_dir={'pycwlviewer': 'pycwlviewer'},
    package_data={'': ['pycwlviewer/queries/*']},
    include_package_data=True,
    author='Yannis Doukas',
    author_email='giannisdoukas2311@gmail.com',
    description='Visualise CWL Workflows',
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Astronomy',
        'Topic :: Scientific/Engineering :: Atmospheric Science',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Medical Science Apps.'
    ],
    entry_points={
        'console_scripts': [
            'cwl-view=pycwlviewer.cwlviewer:main_view',
            'cwl-dot=pycwlviewer.cwlviewer:main_dot',
        ],
    },
    install_requires=[
        'cwltool>=3.0.20200530110633',
        'rdflib>=4.2.2',
        'pygraphviz>=1.5',
    ],
)
