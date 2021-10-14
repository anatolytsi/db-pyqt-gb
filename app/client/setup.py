from setuptools import setup, find_packages

setup(name="messenger_client",
      version="0.0.1",
      description="messenger_client",
      author="Anatolii Tsirkunenko",
      author_email="tsirkunenkoat@gmail.com",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )
