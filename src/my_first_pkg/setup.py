from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'my_first_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),    ],
    py_modules=[
        'my_first_pkg.publisher',
        'my_first_pkg.subscriber',
        'my_first_pkg.counter',
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='tejas',
    maintainer_email='tejas@todo.todo',
    description='My first package for ROS2',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'publisher = my_first_pkg.publisher:main',
            'subscriber = my_first_pkg.subscriber:main',
            'counter = my_first_pkg.counter:main',
        ],
    },
)
