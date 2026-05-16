import sys
import os

def get_chain(words):
    #замість вбудованого сортування роблю bucket sort
    #створюємо 51 порожній список кошик для слів довжиною від 0 до 50
    buckets = [[] for _ in range(51)]
    
    #розкидаємо слова по кошиках відповідно до їхньої довжини
    for w in words:
        buckets[len(w)].append(w)
        
    #збираємо слова назад в один список спочатку короткі потім довгі
    sorted_words = []
    for bucket in buckets:
        for w in bucket:
            sorted_words.append(w)
            
    #далі йде наша стандартна логіка динаміки
    dp = {}
    ans = 0

    for w in sorted_words: #використовуємо наш відсортований список
        current_len = 1
        #перебираєм всі варіанти без однієї букви
        for i in range(len(w)):
            prev = w[:i] + w[i+1:]
            #якщо таке слово вже було, додаєм +1 до ланцюжка
            if prev in dp:
                if dp[prev] + 1 > current_len:
                    current_len = dp[prev] + 1
        
        dp[w] = current_len
        #оновлюєм загальний рекорд
        if current_len > ans:
            ans = current_len
            
    return ans

def solve():
    #якщо є файл читаєм, якщо нє — чекаєм вводу в консоль
    if os.path.exists('wchain.in'):
        with open('wchain.in', 'r') as f:
            data = f.read().split()
    else:
        #читаєм все зразу поки не ctrl+d
        data = sys.stdin.read().split()

    if not data:
        return

    n = int(data[0])
    words = data[1:n+1]

    result = get_chain(words)

    #виводим куди треба
    if os.path.exists('wchain.in'):
        with open('wchain.out', 'w') as f:
            f.write(str(result))
    else:
        print(result)

if __name__ == "__main__":
    solve()
