class TrieNode:
    def __init__(self):
        #словник
        self.children = {}
        #кінець слова
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        #створюємо порожній корінь
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        #йдемо з самого верху
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        #ставимо галочку що тут кінець
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        #шукаємо точний збіг слова
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        #а тут просто чи є взагалі схожий префікс
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

if __name__ == '__main__':
    #дерево
    trie = Trie()

    #ввести дані. split() щоб розбити 
    virus_pattern = input("введи днк вірусу: ").strip().split()
    dna_text = input("введи загальну днк: ").strip()

    #закидаємо ВСІ введені віруси у дерево через цикл
    for v in virus_pattern:
        trie.insert(v)
    
    #визначаємо розмір нашої рамки віконця (беремо довжину першого вірусу зі списку)
    window_size = len(virus_pattern[0])
    virus_count = 0 #лічильник, скільки разів зловили того віруса

    print("\n--- починаємо перевіряти ---")
    
    #соваємо наше віконце по тексту днк
    for i in range(len(dna_text) - window_size + 1):
        #відрізаємо шматок днк, який зараз у віконці
        substring = dna_text[i : i + window_size]
        
        #питаємо дерево чи є такий шматок
        result = trie.search(substring)
        
        #газ
        if result:
            print(f"крок {i}: {substring} ➔ ОПА, ЗНАЙШЛИ! ")
            virus_count += 1 # плюсуємо знахідку
        else:
            print(f"крок {i}: {substring} ➔ чисто")
            
    #підсумки
    if virus_count > 0:
        #рахуємо скільки букв днк вражено вірусом
        infected_length = virus_count * window_size
        percent = (infected_length / len(dna_text)) * 100
        
        #щоб не було більше 100%, якщо віруси накладаються один на одного
        if percent > 100:
            percent = 100
            
        print(f"\n вірус є це жесть! знайдено {virus_count} раз(и)!")
        print(f" рівень зараження: {percent:.1f}%")
    else:
        print("\n ти здоровий як кобила")
