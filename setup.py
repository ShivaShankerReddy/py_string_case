from distutils.core import setup
import os


rootdir = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
with open(os.path.join(rootdir, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


# setup(
#     name='py_string_case',
#     version='1.0.0',
#     py_modules=[
#         'py_string_case'
#     ],
#     url='https://github.com/ShivaShankerReddy/py_string_case',
#     license='MIT',
#     author='Shiva',
#     author_email='shivashanker.chagamreddy@gmail.com',
#     description='String case converter..',
#     long_description=open('./README.rst').read()
# )


setup(
    name="py_string_case",
    version="0.0.1",
    author="shiva",
    author_email="shivashanker.chagamreddy@gmail.com",
    description="String case converter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ShivaShankerReddy/py_string_case",
    # packages=['main'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    scripts= ['src/main.py'],
    python_requires='>=3.0',
)
