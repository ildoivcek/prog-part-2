import unittest
from laba9.lab9 import Trie, build_trie

class TestTrie(unittest.TestCase):
    def setUp(self):
        #ця штука запускається перед кожним тестом, щоб у нас завжди було чисте дерево
        self.trie = Trie()

    def test_insert_and_search(self):
        #додаємо слово і перевіряємо, чи воно дійсно там з'явилося
        self.trie.insert("python")
        self.assertTrue(self.trie.search("python"))
        #а от шматочок слова не повинен рахуватись як повноцінне слово
        self.assertFalse(self.trie.search("pytho"))
        #ну і зовсім лівого слова там теж не має бути
        self.assertFalse(self.trie.search("java"))

    def test_starts_with(self):
        #закидаємо кілька слів
        self.trie.insert("banana")
        self.trie.insert("bandana")
        
        #префікс "ban" точно є
        self.assertTrue(self.trie.starts_with("ban"))
        #префікс "band" теж є (від bandana)
        self.assertTrue(self.trie.starts_with("band"))
        #а от чогось на "cat" ми не додавали
        self.assertFalse(self.trie.starts_with("cat"))

    def test_build_trie_function(self):
        #перевіряємо саме ту функцію яку просили створити в завданні
        words_list = ["apple", "app", "application"]
        #згодовуємо їй список і отримуємо об'єкт дерева
        my_trie = build_trie(words_list)

        #перевіряємо, чи все правильно побудувалось
        self.assertTrue(my_trie.search("apple"))
        self.assertTrue(my_trie.search("app"))
        self.assertTrue(my_trie.starts_with("appli"))
        self.assertFalse(my_trie.search("appl"))

if __name__ == '__main__':
    #запускаємо всю цю красу
    unittest.main()
