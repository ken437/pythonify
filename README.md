# pythonify
IntelliJ plugin to automatically detect antipatterns in Python code and provide quick, one-click fixes for them.

# Setup
Remember to set the `PYTHONPATH` environment variable to include the base directory (`pythonify`) of this
repository after cloning.

# Antipatterns
## E1: Access from end of array without negative index
Antipattern example:
```
a = [1, 2, 3]
b = a[len(a) - 1]
```
Fix:
```
a = [1, 2, 3]
b = a[-1]
```

# Testing
To perform the unit tests, execute `python test/unit_tests/e1_test.py` from the base directory of the repository. Executing them from other directories should work as long as the path to the unit test file is updated.
