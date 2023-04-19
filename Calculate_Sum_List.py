# Replace ___ with your code
import math


# create the Student class
class Student:
    # use the __init__() method to initialize the scores attribute
    def __init__(self, scores):
        self.scores = scores

        # create the get_scores_sum() method that returns the sum of scores items

    def get_scores_sum(self):
        score_list = math.fsum(self.scores)
        return score_list


# create the scores variable
scores = [55, 75, 80, 62, 77]

# create an object of Student by passing scores as an argument
s1 = Student(scores)

# call the get_scores_sum() method using the s1 object
total = int(s1.get_scores_sum())

# print total
print(total)
