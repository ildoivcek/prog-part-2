import unittest
from laba7 import get_max_flow
from laba7_dod import find_critical_roads

class LabTest(unittest.TestCase):
    def test_logic(self):
        # проста ситуація: ферма - вузька дорога - магазин
        fermy = ["f1"]
        magazy = ["s1"]
        dorogy = [("f1", "x1", 10), ("x1", "s1", 4)]
        
        flow, graf, s_in, _ = get_max_flow(fermy, magazy, dorogy)
        critical = find_critical_roads(dorogy, graf, s_in)
        
        # потік має бути 4
        self.assertEqual(flow, 4)
        # критична дорога має бути x1-s1
        self.assertEqual(critical[0][0], "x1")
        self.assertEqual(critical[0][1], "s1")

if __name__ == "__main__":
    unittest.main()
