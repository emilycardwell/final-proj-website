from setuptools import find_packages
from setuptools import setup

with open("requirements.txt") as f:
    content = f.readlines()
requirements = [x.strip() for x in content if "git+" not in x]

setup(name='final-project-website',
      version="0.0.1",
      description="Streamlit website",
      license="MIT",
      author="Emily Cardwell",
      author_email="emily@emilycardwell.com",
      url="https://chord-predict.streamlit.app/",
      install_requires=requirements,
      packages=find_packages())
