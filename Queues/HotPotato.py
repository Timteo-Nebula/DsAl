"""
Backgrounds:
In this game children line up in a circle and
pass a potato from neighbor to neighbor as fast as they can.
At a certain point(e.g, potato has been passed 5 times) in the game,
the action is stopped and the child who has the item (the potato) is
removed from the circle. Play continues until only one child is left.

More detailed description can be found at this web page
'http://interactivepython.org/runestone/static/pythonds/BasicDS/SimulationHotPotato.html'

"""
from Queues.Queue import Queue


def hot_potato(children, trigger=7):
    count = 0
    q = Queue()
    for child in children:
        q.enqueue(child)

    while q.size() > 1:
        # each pass formed by  a pair of dequeue and enqueue operation.
        q.enqueue(q.dequeue())
        count += 1
        if count == trigger:
            count = 0
            q.dequeue()

    return q.dequeue()


if __name__ == "__main__":
    children = ["Bill", "David", "Susan", "Jane", "Kent", "Brad"]
    print("%s wins! " %
          hot_potato(children))

    joseph = list(range(40))
    print("You should choose the %dth location" %
          (hot_potato(joseph) + 1))
