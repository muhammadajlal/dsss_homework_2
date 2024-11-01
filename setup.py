from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="math_quiz",  # Name of the package
    #version="0.1",
    description="A math quiz game",
    author="Muhammad Ajlal",
    author_email="ajlalruddy@gmail.com",
    packages=find_packages(),
    install_requires=requirements,  # Add the requirements file
    entry_points={
        'console_scripts': [
            'math_quiz=math_quiz.math_quiz:main',  # Command to run the game
        ],
    },
)
