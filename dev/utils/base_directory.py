# Provides a variable containing the path of this repository's base directory

import pathlib

base_directory = pathlib.Path(__file__).parent.parent.parent.resolve()  # Must be updated if this file changes places
