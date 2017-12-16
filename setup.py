# coding=utf-8

import os

import versioneer
from pipenv.project import Project
from pipenv.utils import convert_deps_to_pip
from setuptools import setup

pfile = Project(chdir=False).parsed_pipfile
requirements = convert_deps_to_pip(pfile['packages'], r=False)
test_requirements = convert_deps_to_pip(pfile['dev-packages'], r=False)


def read_local_files(*file_paths: str) -> str:
    """
    Reads one or more text files and returns them joined together.

    A title is automatically created based on the file name.

    :param file_paths: list of files to aggregate

    """

    def _read_single_file(file_path):
        with open(file_path) as f:
            filename = os.path.splitext(file_path)[0]
            title = f'{filename}\n{"=" * len(filename)}'
            return '\n\n'.join((title, f.read()))

    return '\n' + '\n\n'.join(map(_read_single_file, file_paths))


entry_points = '''
[console_scripts]
epab=epab.cli:cli
'''

if __name__ == '__main__':
    setup(
        name='EPAB',
        author='132nd-etcher',
        zip_safe=False,
        author_email='epab@daribouca.net',
        platforms=['win32'],
        url=r'https://github.com/132nd-etcher/EPAB',
        download_url=r'https://github.com/132nd-etcher/EPAB/releases',
        description="I'll do you for that.",
        license='GPLv3',
        long_description=read_local_files('README.rst'),
        packages=['epab'],
        include_package_data=True,
        entry_points=entry_points,
        install_requires=requirements,
        tests_require=test_requirements,
        version=versioneer.get_version(),
        cmdclass=versioneer.get_cmdclass(),
        # setup_requires=setup_requires,
        # dependency_links=dependency_links,
        python_requires='>=3.6',
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Topic :: Utilities',
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
            'Environment :: Win32 (MS Windows)',
            'Natural Language :: English',
            'Operating System :: Microsoft :: Windows',
            'Operating System :: Microsoft :: Windows :: Windows 7',
            'Operating System :: Microsoft :: Windows :: Windows 8',
            'Operating System :: Microsoft :: Windows :: Windows 8.1',
            'Operating System :: Microsoft :: Windows :: Windows 10',
            'Programming Language :: Cython',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3 :: Only',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: Implementation',
            'Programming Language :: Python :: Implementation :: CPython',
            'Topic :: Games/Entertainment',
            'Topic :: Utilities',
        ],
    )
