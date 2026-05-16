from laba8 import get_chain

def run_extra():
    #список слів для прикладу
    my_words = ["t", "at", "cat", "cats", "car", "crats", "bat", "bats"]
    
    #фільтруєм тільки ті де більше 2 букв
    #бо короткі слова то не цікаво
    filtered = [w for w in my_words if len(w) > 2]
    
    #рахуєм ланцюжок тільки для них
    res = get_chain(filtered)
    
    print(f"# фільтровані слова: {filtered}")
    print(f"# макс ланцюжок без коротких слів: {res}")

if __name__ == "__main__":
    run_extra()
