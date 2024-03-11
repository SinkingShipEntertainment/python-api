name = "sg_api"

version = "3.4.2"

authors = [
    "Shotgrid"
]

description = \
    """
    Shotgrid API
    """

with scope("config") as c:
    import os
    c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_EXT"]

requires = [
]

private_build_requires = [
]

variants = [
]

build_command = "rez python {root}/rez_build.py"

uuid = "repository.python-api"

def commands():
    env.REZ_SG_API_ROOT = "{root}"
    env.PYTHONPATH.append("{root}")
