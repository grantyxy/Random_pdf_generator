import setuptools

i = 3
setuptools.setup(name='random-pdf-generator',
                 version='0.2',
                 description='A PDF generator with random content',
                 url='https://github.com/grantyxy/Random-PDF-Generator',
                 author='Xingyou Yu',
                 author_email='grantyxy@outlook.com',
                 license='GPL-3.0',
                 install_requires=['fpdf'],
                 zip_safe=False)
