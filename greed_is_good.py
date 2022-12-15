def score(dice):
    trip_scores = {0:0, 1:800, 2 : 200, 3 : 300, 4 : 400, 5 : 400, 6 : 600, 7:0}
    sing_scores = {0: 0, 1: 100, 2: 0, 3: 0, 4: 0, 5: 50, 6: 0, 7:0}
    final_score = 0
    dice.append(7)
    sorted_dice = sorted(dice)
    counter = 0
    for row, i in enumerate(sorted_dice):
        print(f'counter {counter}')
        if i == sorted_dice[row-1]:
            counter += 1
        if i != sorted_dice[row-1]:
            counter = 0
        if counter == 2:
            final_score += trip_scores[i]
            counter = -1
        else:
            final_score += sing_scores[i]
    return final_score
//
    sum = 0
    counter = [0,0,0,0,0,0]
    points = [1000, 200, 300, 400, 500, 600]
    extra = [100,0,0,0,50,0]
    for die in dice: 
    counter[die-1] += 1

    for (i, count) in enumerate(counter):
    sum += (points[i] if count >= 3 else 0) + extra[i] * (count%3)

    return sum
//
    return dice.count(1)//3 * 1000 + dice.count(1)%3 * 100 \
            + dice.count(2)//3 * 200 \
            + dice.count(3)//3 * 300 \
            + dice.count(4)//3 * 400 \
            + dice.count(5)//3 * 500 + dice.count(5)%3 * 50 \
            + dice.count(6)//3 * 600 \


print(score([1, 1, 2, 2, 3]))