from setuptools import find_packages, setup
from typing import List

HYPEN = "-e ."

def get_requirement(file_path: str) -> List[str]:
    """
    Reads the requirements.txt file and returns a list of dependencies.
    """
    requirement = []
    with open(file_path, "r") as file_obj:
        requirement = file_obj.readlines()
        requirement = [req.strip() for req in requirement]  # Remove extra spaces and newlines
        if HYPEN in requirement:
            requirement.remove(HYPEN)  # Remove '-e .' if present
    return requirement

setup(
    name="ml_project",
    version="0.0.1",
    author="Aditya",
    author_email="adityaganeshpawar@gmail.com",
    packages=find_packages(),  # Fix here (was `package`)
    install_requires=get_requirement("requirement.txt")  # Ensure filename is correct
)
