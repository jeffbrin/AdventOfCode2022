class Monkey:
    def __init__(self, items: list, operation: str, test: str, targetIfTrue: int, targetIfFalse: int) -> None:
        self.items = items
        self.operation = operation
        self.test = test
        self.targetIfTrue = targetIfTrue
        self.targetIfFalse = targetIfFalse
        self.inspections = 0

    def set_reduce(self, num: int) -> None:
        self.reduce_number = num

    def inspectAndThrow(self) -> tuple:
        '''Returns a tuple. The first element if the item, the second is the target.
        (ITEM, TARGET)'''
        if len(self.items) == 0:
            return

        # Perform the operation on the first item and return it with the target so it can be thrown
        item = self.items[0]
        item =  eval(self.operation.replace("old", str(item)))

        # Relax
        item = item % self.reduce_number

        # Test and get target
        test_result = item % self.test == 0
        target = self.targetIfTrue if test_result else self.targetIfFalse

        # Remove from the list
        self.items.pop(0)

        self.inspections += 1
        return (item, target)

    def catch(self, item) -> None:
        self.items.append(item)

    def __str__(self) -> str:
        return f'Items: {self.items}\nOperation: {self.operation}\nTest: {self.test}\nTrue: {self.targetIfTrue}\nFalse: {self.targetIfFalse}\nInspections: {self.inspections}'

def monkey_from_data(data: dict) -> Monkey:
   return Monkey(
                data['items'],
                data['operation'],
                data['test'],
                data['true'],
                data['false']
            )

# Read file and make monkeys
monkeys = {}
with open("input.txt") as file:
    line = file.readline()
    monkey_data = {}
    while line != "":
        if "Monkey" in line:
            monkey_data['num'] = int(line.split()[1].split(":")[0])
        elif "Starting items" in line:
            monkey_data['items'] = [int(x) for x in line.split(":")[1].split(",")]
        elif "Operation" in line:
            monkey_data['operation'] = line.split("=")[1].split("\n")[0]
        elif "Test" in line:
            monkey_data['test'] = int(line.split()[-1])
        elif "true" in line:
            monkey_data['true'] = int(line.split()[-1])
        elif "false" in line:
            monkey_data['false'] = int(line.split()[-1])

        # If this is a separation between two monkeys,
        # Make a monkey with the info we built
        elif line == "\n":
            monkeys[monkey_data['num']] = monkey_from_data(monkey_data)
            monkey_data = {}
    
        line = file.readline()

# Add the last monkey
monkeys[monkey_data['num']] = monkey_from_data(monkey_data)

# Set the reduce number
reduce_num = 1
for x in map(lambda key: monkeys[key].test, monkeys): reduce_num *= x

for m in monkeys:
    monkeys[m].set_reduce(reduce_num)

ROUNDS = 10000
for round in range(ROUNDS):
    for no in monkeys:
        monkey: Monkey = monkeys[no]

        while len(monkey.items) != 0:
            (item, target) = monkey.inspectAndThrow()
            monkeys[target].catch(item)

# # Sort by inspections
monkeys = [monkeys[m] for m in monkeys]
monkeys = sorted(monkeys, key=lambda x: x.inspections, reverse=True)

print(monkeys[0].inspections * monkeys[1].inspections)