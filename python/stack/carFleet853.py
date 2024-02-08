from matplotlib import pyplot

def carFleet(target: int, position: list[int], speed: list[int]) -> int:
    fleet = []
    pairs = [(p, s) for p, s in zip(position, speed)]

    for cars in sorted(pairs, reverse=True):
        fleet.append((target - cars[0]) / cars[1])
        print(fleet)
        if len(fleet) >= 2 and fleet[-1] <= fleet[-2]:
            fleet.pop()

    return len(fleet)

target = 12 
position = [10,8,0,5,3] 
speed = [2,4,1,1,3]

print(carFleet(target, position, speed)) # Expected output : 3