def linearCongruentialMethod(Xo, m, a, c,randomNums, noOfRandomNums):
    # seed state is initialized here
    randomNums[0] = Xo
 
    # Traverse to generate required
    # numbers of random numbers
    for i in range(1, noOfRandomNums):
         
        # linear congruential method
        randomNums[i] = ((randomNums[i - 1] * a) + c) % m

def additiveCongruentialMethod(Xo, m, c,
                               randomNums,
                               noOfRandomNums):
 
    # Initialize the seed state
    randomNums[0] = Xo
 
    # Traverse to generate required
    # numbers of random numbers
    for i in range(1, noOfRandomNums):
         
        # Follow the linear congruential method
        randomNums[i] = (randomNums[i - 1] + c) % m


if __name__ == '__main__':
    # Seed value
    Xo = 6
    # Modulus parameter
    m = 100
    # Multiplier term
    a = 5
    # Increment term
    c = 7
    noOfRandomNums = 10
    # To store random numbers
    randomNums = [0] * (noOfRandomNums)
    linearCongruentialMethod(Xo, m, a, c, randomNums, noOfRandomNums)
    # additiveCongruentialMethod(Xo, m, c, randomNums, noOfRandomNums)
 
    # Print the generated random numbers
    for i in randomNums:
        print(i, end = " ")