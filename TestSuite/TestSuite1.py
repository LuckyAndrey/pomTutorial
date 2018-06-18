import unittest

from Tests import test_Switch_to_Alert

first = unittest.TestLoader().loadTestsFromModule(test_Switch_to_Alert)
second = unittest.TestLoader().loadTestsFromModule(test_Switch_to_Alert)




suite = unittest.TestSuite([first, second])

unittest.TextTestRunner(verbosity=2).run(suite)
