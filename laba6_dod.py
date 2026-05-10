from laba6 import find_unreachable_cities

def find_critical_pipeline(cities, storages, pipelines):
    
    #шукає пошкодження якої труби призведе до найбільшої втрати газу в містах
    
    max_lost_cities = -1
    critical_pipe = None

    #рахуємо скільки міст не мають газу зараз
    initial_unreachable = find_unreachable_cities(cities, storages, pipelines)
    initial_count = sum(len(cities_list) for _, cities_list in initial_unreachable)

    for i in range(len(pipelines)):
        #тимчасово видаляємо одну трубу
        test_pipes = pipelines[:i] + pipelines[i+1:]
        
        current_result = find_unreachable_cities(cities, storages, test_pipes)
        current_count = sum(len(cities_list) for _, cities_list in current_result)
        
        lost_due_to_break = current_count - initial_count
        
        if lost_due_to_break > max_lost_cities:
            max_lost_cities = lost_due_to_break
            critical_pipe = pipelines[i]

    return critical_pipe, max_lost_cities

if __name__ == "__main__":
    cities_list = ["Львів", "Стрий", "Київ"]
    storages_list = ["Сховище_А"]
    pipes = [["Сховище_А", "Львів"], ["Львів", "Стрий"], ["Сховище_А", "Київ"]]
    
    pipe, loss = find_critical_pipeline(cities_list, storages_list, pipes)
    print(f"Найкритичніша труба: {pipe} її пошкодження відключить ще {loss} міст(а).")
