import math
import unittest

from encoder_rpm import calculate_rpm, rpm_to_rad_s, speed_status


class EncoderRpmTests(unittest.TestCase):
    def test_calculate_rpm(self):
        self.assertAlmostEqual(calculate_rpm(1000, 500, 2.0), 60.0)

    def test_zero_pulses_is_zero_rpm(self):
        self.assertEqual(calculate_rpm(0, 500, 1.0), 0.0)

    def test_rpm_to_rad_s(self):
        self.assertAlmostEqual(rpm_to_rad_s(60.0), 2.0 * math.pi)

    def test_speed_status(self):
        self.assertEqual(speed_status(1200.0, 1500.0), "OK")
        self.assertEqual(speed_status(1600.0, 1500.0), "OVER LIMIT")

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            calculate_rpm(-1, 500, 1.0)
        with self.assertRaises(ValueError):
            calculate_rpm(100, 0, 1.0)
        with self.assertRaises(ValueError):
            calculate_rpm(100, 500, 0.0)
        with self.assertRaises(ValueError):
            speed_status(100.0, 0.0)


if __name__ == "__main__":
    unittest.main()
