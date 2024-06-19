#!/usr/bin/python3

"""Script that uses a recursive function to query the Reddit API and return a
list containing the titles of all hot articles for a given subreddit. It
prints a sorted count of the number of times each word appears in the titles"""
import requests


def count_words(subreddit, word_list, found_list=[], next_page=None):
    """
    Prints counts of given words found in hot posts of a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): A list of words to search for in the titles.
        found_list (list, optional): A list to store the found words. Defaults
        to an empty list.
        next_page (str, optional): The "next_page" parameter for pagination.
        Defaults to None.
    """
    try:
        reply = requests.get(
            f"http://www.reddit.com/r/{subreddit}/hot.json?after={next_page}",
            headers={"user-agent": "nabuntu_bot-01"},
            timeout=60,
        )
    except requests.ConnectionError:
        print("Encountered a connection error. Please try again later.")
        return

    if next_page is None:
        word_list = [word.lower() for word in word_list]

    if reply.status_code != 200:
        return

    data = reply.json()["data"]
    next_page = data["after"]
    sends = data["children"]

    locate_matching_words(word_list, found_list, sends)

    if next_page is not None:
        count_words(subreddit, word_list, found_list, next_page)
    else:
        count_word = count_word_numbers(found_list)

        display_keywords_count(count_word)


def display_keywords_count(count_word):
    """
    Prints the keywords and their corresponding word counts in descending
    order.

    Args:
        word_count (dict): A dictionary containing keywords as keys and their
        respective word counts as values.
    """
    sort_word_count = sorted(
        count_word.items(), key=lambda item: item[1], reverse=True
    )

    for keyword, count in sort_word_count:
        print("{}: {}".format(keyword, count))


def count_word_numbers(list_found):
    """
    Counts the occurrences of each word in a given list.

    Args:
        found_list (list): A list of words.

    Returns:
        dict: A dictionary where the keys are the words and the values are the
        number of occurrences. The keys are all lowercase.
    """
    count_word = {}
    for word in list_found:
        if word.lower() in count_word:
            count_word[word.lower()] += 1
        else:
            count_word[word.lower()] = 1
    return count_word


def locate_matching_words(word_list, list_found, sends):
    """
    Finds and appends matching words from post titles to the found_list.

    Args:
        word_list (list): A list of words to search for in the titles.
        found_list (list): A list to store the found words.
        posts (list): A list of post objects containing title information.
    """
    for send in sends:
        title = send["data"]["title"].lower()
        for word in title.split():
            if word in word_list:
                list_found.append(word)
