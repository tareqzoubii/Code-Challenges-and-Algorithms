from challenge02 import repeated_word
import pytest
# Write your test here

def test1_repeated_word():
    expected = "ASAC"
    actual = repeated_word("ASAC is a department at LTUC. ASAC teaches programming in LTUC.")
    assert actual == expected

def test2_repeated_word():
    expected = "No Repetition"
    actual = repeated_word("I am learning programming at ASAC.")
    assert actual == expected

def test3_repeated_word():
    expected = "No Repetition"
    actual = repeated_word("Today me and my friends will play football")
    assert actual == expected
