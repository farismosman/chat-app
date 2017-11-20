from setuptools import setup

setup(
    name='timesmedia',
    packages=['src'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask-sqlalchemy',
        'alembic',
        'psycopg2'
    ],
)
