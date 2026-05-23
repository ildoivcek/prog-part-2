class TrieNode:
    def __init__(self):
        #кожен вузол має словничок для своїх нащадків
        self.children = {}
        #і маленький прапорець, щоб знати чи закінчується тут слово
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        #створюємо порожній корінець нашого дерева
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        #починаємо мандрівку з самого верху
        node = self.root
        for char in word:
            #якщо такої букви ще немає серед діток, швиденько її додаємо
            if char not in node.children:
                node.children[char] = TrieNode()
            #стрибаємо на рівень нижче по цій букві
            node = node.children[char]
        #слово закінчилось, ставимо позначку, що тут фінал
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        #знову стартуємо від кореня
        node = self.root
        for char in word:
            #якщо раптом потрібної букви немає — такого слова точно не існує
            if char not in node.children:
                return False
            #йдемо далі по знайденому шляху
            node = node.children[char]
        #перевіряємо, чи ми дійшли до кінця саме слова, а не просто якогось шматка
        return node.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        #тут логіка майже як у пошуку всього слова
        node = self.root
        for char in prefix:
            #якщо шлях обірвався, значить такого префікса нема
            if char not in node.children:
                return False
            #спускаємось глибше
            node = node.children[char]
        #якщо ми успішно пройшли всі букви префікса, значить він є в дереві
        return True

def build_trie(patterns: list[str]) -> Trie:
    #створюємо новісіньке дерево
    trie = Trie()
    #просто перебираємо всі слова зі списку і закидаємо їх у наше дерево
    for word in patterns:
        trie.insert(word)
    #віддаємо готову структуру
    return trie
