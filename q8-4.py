
def powerset(set):
    import itertools
    for n in xrange(len(set)):
        # Iterate over all possible set sizes
        for c in itertools.combinations(set, n):
            yield c

def test1():
    return list(powerset([1,2,3,4,5]))

def main():
    print test1()

if __name__ == "__main__":
    main()
