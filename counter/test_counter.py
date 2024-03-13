"""Write a unit test to verify that Counter is a singleton.

   Also verify that all instances share the same count
   and that the count is not reset to 0 when you invoke 
   count = Counter() 
   after the first time.

   You can use pytest or unittest.
"""
from counter import Counter
import unittest

class CounterTest(unittest.TestCase):

   def test_create_one_object(self):
      """Test for creating one counter object"""
      c1 = Counter()
      self.assertEqual(0, c1.count)

   def test_counter_is_singleton(self):
      """Test for counter is a singleton when two objects not occur at the same time"""
      c1 = Counter()
      self.assertEqual(0, c1.count)
      c1.increment()
      self.assertEqual(1, c1.count)
      c2 = Counter()
      self.assertEqual(0, c2.count)
      self.assertTrue(c1 == c2)
   
   def test_counter_is_singleton2(self):
      """Test for counter is a singleton when two objects occur at the same time"""
      c1 = Counter()
      c2 = Counter()
      c1.increment()
      self.assertEqual(1, c2.count)
      self.assertTrue(c1 == c2)

if __name__ == '__main__':
    unittest.main(verbosity = 2)
