from setuptools import find_packages, setup

with open("./README.md", "r") as f:
    long_description = f.read()

with open("./requirements.txt", "r") as reqs:
    deps = reqs.read().splitlines()

with open("./VERSION.txt", "r") as ver:
    version = ver.read()

setup(
    name="spa",
    version=version,
    description="Using SIP Packet Analyser (SPA, Chat with PCAP/PCAPNG files locally, privately!",
    packages=find_packages(),
    package_dir={'spa' : '.'},
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/idkpmiller/sip-packet-analyser",
    author="Viswa Kumar",
    author_email="idkpmiller@gmail.com",
    license="MIT",
    scripts=['bin/spa', 'bin/spa_main.py', 'bin/spa_ollamaClient.py', 'bin/spa_packet.py', 'bin/spa_prompt.py', 'bin/spa_settings.py', 'bin/spa_home.py', 'bin/spa_init.py', 'bin/spa_agent.py'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    install_requires = deps,
    include_package_data=True,
    python_requires=">=3.11",
)   