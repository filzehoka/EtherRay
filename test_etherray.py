# test_etherray.py
"""
Tests for EtherRay module.
"""

import unittest
from etherray import EtherRay

class TestEtherRay(unittest.TestCase):
    """Test cases for EtherRay class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = EtherRay()
        self.assertIsInstance(instance, EtherRay)
        
    def test_run_method(self):
        """Test the run method."""
        instance = EtherRay()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
