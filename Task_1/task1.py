from collections import deque

def check_relation(net, first, second):
    search_queue = deque()
    graph_list = {}
    for relation in net:
        graph = {x: [y] for x, y in zip(relation, relation[::-1])}
        graph_list.update(graph)
    for relation in net:
        graph_list[relation[0]].append(relation[1])
        graph_list[relation[1]].append(relation[0])

    search_queue+=graph_list[first]
    searched = []
    while search_queue:
        name = search_queue.popleft()
        if name not in searched:
            if name is second:
                return True
            else:
                search_queue+=graph_list[name]
                searched.append(name)
    return False


if __name__ == '__main__':
    net = (
        ("Ваня", "Лёша"), ("Лёша", "Катя"),
        ("Ваня", "Катя"), ("Вова", "Катя"),
        ("Лёша", "Лена"), ("Оля", "Петя"),
        ("Стёпа", "Оля"), ("Оля", "Настя"),
        ("Настя", "Дима"), ("Дима", "Маша")
    )

    assert check_relation(net, "Петя", "Стёпа") is True
    assert check_relation(net, "Маша", "Петя") is True
    assert check_relation(net, "Ваня", "Дима") is False
    assert check_relation(net, "Лёша", "Настя") is False
    assert check_relation(net, "Стёпа", "Маша") is True
    assert check_relation(net, "Лена", "Маша") is False
    assert check_relation(net, "Вова", "Лена") is True