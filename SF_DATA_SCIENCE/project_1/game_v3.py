import numpy as np

def random_predict(number:int=1) -> int:
    """Guess a number randomly

    Args:
        number (int, optional): Hidden number. Defaults to 1.

    Returns:
        int: Number of attempts
    """

    count = 0
    first = 0
    last = 101
    n = 1
    while number != n:
        count +=1
        n = (first + last)//2
        if number > n:
            first = n
        elif number < n:
            last = n
    return(count)

def score_game(random_predict) -> int:
    """For how many attempts on average out of 1000 approaches our algorithm guesses

    Args:
        random_predict ([type]): guess function

    Returns:
        int: average number of attempts
    """

    count_ls = [] # list to save the number of attempts
    np.random.seed(1) # fix seed for reproducibility
    random_array = np.random.randint(1, 101, size=(1000)) # made a list of numbers

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # find the average number of attempts

    print(f'Your algorithm guesses the number in {score} attempts on average')
    return(score)

# RUN

if __name__ == '__main__':
    score_game(random_predict)