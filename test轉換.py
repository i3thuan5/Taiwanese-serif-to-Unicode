from unittest.case import TestCase
from 轉換器 import 轉換


class test轉換(TestCase):
    
    def test鼻音符號(self):
        self.assertEqual(轉換('Chhi°'), 'Chhiⁿ')
        
    def test_oo(self):
        self.assertEqual(轉換('h³'), 'hō͘')
        
    def test囥佇正確碼位的字(self):
        self.assertEqual(轉換('Á'), 'Á')
        
    def test_combine(self):
        self.assertEqual(轉換('ýh'), 'u̍h')
        
    def test漢字袂動(self):
        print(轉換(self.text))
        self.assertEqual(轉換('t¡g 去'), 'tńg 去')