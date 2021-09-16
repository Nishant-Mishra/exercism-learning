"""
You're a teaching assistant correcting student exams. Keeping track of results manually is getting both tedious
and mistake-prone. You decide to make things a little more interesting by putting together some functions to count
and calculate results for the class.
"""
from typing import List, Union


def round_scores(student_scores: List[float]) -> List[int]:
    """
    :param student_scores: List[float]: list of student exam scores as float or int.
    :return: List[int]: list of student scores *rounded* to nearest integer value.
    """
    return [round(score) for score in student_scores]


def count_failed_students(student_scores: List[int]) -> int:
    """
    :param student_scores: List[int]: list of integer student scores.
    :return: int: count of student scores at or below 40.
    """
    return sum(score <= 40 for score in student_scores)


def above_threshold(student_scores: List[int], threshold: int) -> List[int]:
    """
    :param student_scores: list of integer scores
    :param threshold :  integer
    :return: list of integer scores that are at or above the "best" threshold.
    """
    return list(filter(lambda score: score >= threshold, student_scores))


def letter_grades(highest: int) -> List[int]:
    """
    :param highest: integer of highest exam score.
    :return: list of integer score thresholds for each F-A letter grades.
    """
    return list(range(41, highest, (highest - 40) // 4))


def student_ranking(student_scores: List[int], student_names: List[str]) -> List[str]:
    """
     :param student_scores: list of scores in descending order.
     :param student_names: list of names in descending order by exam score.
     :return: list of strings in format ["<rank>. <student name>: <score>"].
     """
    return [f"{i + 1}. {name}: {score}" for i, (name, score) in enumerate(zip(student_names, student_scores))]


def perfect_score(student_info: List[List[Union[str, int]]]) -> Union[List[Union[str, int]], str]:
    """
    :param student_info: list of [<student name>, <score>] lists
    :return: First [<student name>, 100] found OR "No perfect score."
    """
    for elem in student_info:
        if elem[1] == 100:
            return elem

    return "No perfect score."
