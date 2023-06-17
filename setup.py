from setuptools import setup

setup(
    name='serial_monitor',
    version='0.1.0',
    py_modules=['main'],
    install_requires=[
        'Click',
        'pySerial'
    ],
    entry_points={
        'console_scripts': [
            'serial-monitor = main:start_serial',
        ],
    },
)