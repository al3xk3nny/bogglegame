# Challenge
# Output should be ["H", "HE", "HEL", "HELL", "HELLO"]


def get_stems(word):
    
    stems = []
    
    # stems.append(word[:1])
    # stems.append(word[:2])
    # stems.append(word[:3])
    # stems.append(word[:4])
    # stems.append(word[:5])
    
    
    for i in range(1, len(word)):
        stems.append(word[:i])
    
    print(stems)


get_stems("HELLO")
