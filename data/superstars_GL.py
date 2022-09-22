# Find the problem statement by clicking "Instructions" on the right panel >>>

def findSuperstar(oracle):
    """
    This method returns:
    - a list of superstars if any
    - an empty list otherwise
    """
    
    print(f"The village counts {oracle.size} inhabitants.")
    #print(f"You can ask the oracle whether #1 knows #3: {oracle.knows(1, 3)}.")
    
    #
    # Your code goes here
    #
    candidats = list(range(1, oracle.size + 1))
    ignored_by = {}
    know = {}
    
    for k in candidats:
        ignored_by[k] = []
        know[k] = []
        
    while len(candidats) > 1:
        ind = len(candidats) // 2
        for k in range(ind):
            c1 = candidats[2*k]
            c2 = candidats[2*k+1]
            if oracle.knows(c1, c2):
                candidats.remove(c1)
                know[c2].append(c1)
            else:
                candidats.remove(c2)
                ignored_by[c1].append(c2)
    
    if candidats == []:
        return []
    
    candidat = candidats[0]
    
    # test de validité 1 : le candidat ne connait personne
    for perso in list(range(1, oracle.size + 1)):
        if perso == candidat:
            continue
        if perso in ignored_by[candidat]:
            continue
        if oracle.knows(candidat, perso):
            return []
              
    # test de validité 2 : tout le monde connait le candidat
    for perso in list(range(1, oracle.size + 1)):
        if perso == candidat:
            continue
        if perso in know[candidat]:
            continue
        if not oracle.knows(perso, candidat):
            return []
     
    
    return [candidat]


class Inhabitant:
    '''
    DO NOT MODIFY
    '''
    id: int = 0
    friends = []

    def __init__(self, id: int, friends) -> None:
        self.id = id
        self.friends = friends

    def __str__(self):
        return f"{self.id} --> {self.friends}"


class Oracle:
    '''
    DO NOT MODIFY
    '''

    village = []
    size: int = 0
    price: int = 0

    def __init__(self, village) -> None:
        self.village = village
        self.size = len(village)-1
        self.price = 0

    def knows(self, x: int, y: int) -> bool:
        self.price += 1
        return y in self.village[x].friends

    def __str__(self):
        result = ""
        for person in self.village:
            if person is not None:
                result += person.__str__()
                result += "\n"
        return result


def get_oracle_test_with_superstar():
    """
    This method returns an oracle representing a village of 3 people in which:
    - 1 does not know anybody
    - 2 knows 1 and 3
    - 3 knows 1
    Hence, 1 is a superstar.
    """
    return Oracle([
        None,
        Inhabitant(1, [0]),
        Inhabitant(2, [1, 3]),
        Inhabitant(3, [1]),
    ])

def get_oracle_test_without_any_superstar():
    """
    This method returns an oracle representing a village of 3 people in which:
    - 1 knows 3
    - 2 knows 1 and 3
    - 3 knows 1
    Hence, there isn't any superstar.
    """
    return Oracle([
        None,
        Inhabitant(1, [3]),
        Inhabitant(2, [1, 3]),
        Inhabitant(3, [1]),
    ])

if __name__ == '__main__':
    '''
    you can modify the following in order to test your code
    '''
    oracle = get_oracle_test_with_superstar()
    print(oracle)
    superstars = findSuperstar(oracle)
    print(f"superstars = {superstars}")
    print(f"result found asking {oracle.price} questions")
    print("---")
    oracle = get_oracle_test_without_any_superstar()
    print(oracle)
    superstars = findSuperstar(oracle)
    print(f"superstars = {superstars}")
    print(f"result found asking {oracle.price} questions")