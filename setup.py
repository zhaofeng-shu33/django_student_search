from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="django-student-search",
    version="0.1",
    author="zhaofeng-shu33",
    description="search student information",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitee.com/freewind201301/student_search",
    author_email="616545598@qq.com",
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
    ],
)
