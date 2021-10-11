import unittest
import os
import sys
import pathlib
from dev.E1 import detect_e1
from dev.utils.base_directory import base_directory

"""
Tests the ability to detect and fix the E1 (accessing from end of list without negative
index) antipattern.
"""
class TestE1(unittest.TestCase):

    """
    Get the contents of a Python example file (assumed to be in the E1 directory)
    @param filename: (str) name of the example file
    """
    def _get_contents(self, filename):
        noap_filepath = os.path.join(base_directory, "test", "example_python_files", "E1", filename)
        with open(noap_filepath, "r") as python_file:
            file_contents = python_file.read()
            return file_contents
    """
    Test that if there is an antipattern in a comment but not in the code it doesn't report
    anything
    """
    def test_antipatternincomment(self):
            file_contents = self._get_contents("incomment.py")
            self.assertFalse(detect_e1.has_e1(file_contents=file_contents))

    """
    Test that if there is an antipattern in a triple-quoted string but not in the code it
    doesn't report anything
    """
    def test_antipatternintriplestring(self):
            file_contents = self._get_contents("intriplestring.py")
            self.assertFalse(detect_e1.has_e1(file_contents=file_contents))

    """
    Test that if there is no antipattern at all in the Python file
    the code doesn't report one.
    """
    def test_noantipattern1(self):
            file_contents = self._get_contents("noantipattern1.py")
            self.assertFalse(detect_e1.has_e1(file_contents=file_contents))

    """
    Test that an antipattern is detected if present
    """
    def test_antipattern1(self):
            file_contents = self._get_contents("antipattern1.py")
            self.assertTrue(detect_e1.has_e1(file_contents=file_contents))

    """
    Test that an antipattern is detected if present
    """
    def test_antipattern2(self):
            file_contents = self._get_contents("antipattern2.py")
            self.assertTrue(detect_e1.has_e1(file_contents=file_contents))
    
    """
    Test that it can also tell if 2 is subtracted from the len() call
    """
    def test_antipatternminustwo(self):
            file_contents = self._get_contents("antipatternminustwo.py")
            self.assertTrue(detect_e1.has_e1(file_contents=file_contents))

    """
    Test that it can deal with weird whitespace involved with the antipattern
    """
    def test_weirdwhitespace(self):
            file_contents = self._get_contents("weirdwhitespace.py")
            self.assertTrue(detect_e1.has_e1(file_contents=file_contents))

if __name__ == "__main__":
    unittest.main()
