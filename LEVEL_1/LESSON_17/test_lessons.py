import unittest

from LESSON_17 import lesson_6_1
from LESSON_17 import lesson_7_2
from LESSON_17 import lesson_11_2
from LESSON_17 import lesson_16_2


class AllTests(unittest.TestCase):

    def test_dict(self):
        self.assertEqual(lesson_6_1.new_dict(('Bitcoin', 'Ether', 'Ripple', 'Litecoin'), ('BTC', 'ETH', 'XRP', 'LTC')),
                         {'Bitcoin': 'BTC', 'Ether': 'ETH', 'Ripple': 'XRP', 'Litecoin': 'LTC'})

    def test_cel_calc(self):
        self.assertEqual(lesson_7_2.cels(0), 'Температура по Кельвину: 273.15 Температура по Фарренгейту: 32.0')

    def test_kel_calc(self):
        self.assertEqual(lesson_7_2.kelv(0), 'Tемпература по Цельсию: -273.15 Температура по Фарренгейту: -459.67')

    def test_far_calc(self):
        self.assertEqual(lesson_7_2.farren(0), 'Температура по Кельвину: 255.37 Tемпература по Цельсию: -17.78')

    def test_email(self):
        self.assertEqual(lesson_11_2.hide_email('somebody_email@gmail.com'), 'somebody_em***@**il@gmail.com')

    def test_tel_numb(self):
        self.assertEqual(lesson_16_2.check_tel_num('063-999-99-99'), '(+38) 063 999-99-99')
        self.assertEqual(lesson_16_2.check_tel_num('063 999-99-99'), '(+38) 063 999-99-99')
        self.assertEqual(lesson_16_2.check_tel_num('063-99999-99'), '(+38) 063 999-99-99')
        self.assertEqual(lesson_16_2.check_tel_num('+3806399999-99'), '(+38) 063 999-99-99')
        self.assertEqual(lesson_16_2.check_tel_num('380639999999'), '(+38) 063 999-99-99')


if __name__ == '__main__':
    unittest.main()