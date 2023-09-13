import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setuptools.setup(
    name='chatGPT-api',
    version='0.0.123',
    author='Ahmed badr',
    author_email='ahmed.k.badr.97@gmail.com',
    description='chat gpt api',
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
    url='https://github.com/Andalusia-Data-Science-Team/chatGPT-api',
    license='MIT',
    packages=['chatGPT_api'],
    package_dir={
        'chatGPT_api': 'src/chatGPT_api'},
    install_requires=['openai'],
)
