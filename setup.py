from setuptools import setup

setup(
    name='timesmedia',
    packages=['src', 'src.models', 'src.views'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask-sqlalchemy',
        'alembic',
        'psycopg2',
        'flask-migrate',
        'flask-script',
        'flask-bcrypt',
        'pyjwt'
    ],
)
