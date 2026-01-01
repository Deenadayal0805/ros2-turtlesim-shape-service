from setuptools import find_packages, setup

package_name = 'py_srvcli'

setup(
    name=package_name,
    version='0.0.2',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='deenadayal',
    maintainer_email='sdeenadayal2006@gmail.com',
    description='TurtleSim based interactive shape designer!!',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [

        'draw_shape_server = py_srvcli.draw_shape_server:main',
        'draw_shape_client = py_srvcli.draw_shape_client:main',

        ],
    },
)