from setuptools import setup

__version__ = '0.1'


setup(
    name='argue',
    version=__version__,
    url='https://gitlab.com/jrkerns/argue',
    keywords="""parameters functions bounds""",
    author='James Kerns',
    author_email='jkerns100@gmail.com',
    description='Set bounds and options for your functions and conditions for your methods',
    license='MIT',
    test_suite='tests.test_argue',
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3"]
)
