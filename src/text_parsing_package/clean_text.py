"""
A module cleans a string of text and parses it into a list of individual words
"""

def clean_text(text, pref_case="lower", rm_all_punc=True, punctuation=None) -> list:
    """
    Cleans a string of text according to function arguments

    Parameters
    ----------
    text : str
        Any string of words, with or without punctuation.
    pref_case : str, default="lower"
        The case to convert the string to - possible values are "upper", 
        "lower", "asis"
    rm_all_punc : bool, default=True
        Indicates whether all punctuation should be removed from the string
    punctuation : list or None, default=None
        If rm_all_punc is false, a list of specific punctuation to remove can be provided here to only remove certain punctuation marks
        
    Returns
    -------
    string
       A cleaned string without whitespace other than spaces, coverted to a specific case if relevant and with punctuation removed as specified

    Examples
    --------
    >>> clean_text("Hello, it is so lovely to meet you today.")
    "hello it is so lovely to meet you today"

    >>> clean_text("Hello, it is so lovely to meet you today.", pref_case="upper", rm_all_punc=False, punctuation=[",", "!"])
    "HELLO IT IS SO LOVELY TO MEET YOU TODAY."

    """
    ...