import setuptools

_requires = [
    'setuptools-scm',
    'raspi_system',

    # Node Id
    'netifaces',

    # System
    'ifcfg',
]

setuptools.setup(
    name='ebs-linuxnode-sysinfo',
    url='https://github.com/ebs-universe/ebs-linuxnode-sysinfo',

    author='Chintalagiri Shashank',
    author_email='shashank.chintalagiri@gmail.com',

    description='System Information Providers for EBS IOT Applications',
    long_description='',

    packages=setuptools.find_packages(),
    install_requires=_requires,

    setup_requires=['setuptools_scm'],
    use_scm_version=True,

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Operating System :: POSIX :: Linux',
    ],
)