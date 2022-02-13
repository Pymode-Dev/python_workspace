import pprint

def character_counts(test):
    counts = {}
    
    for i in test:
        counts.setdefault(i, 0)
        counts[i] += 1
    pprint.pprint(counts)


message = 'hey whats up, i hope you are fine'
character_counts(message)
