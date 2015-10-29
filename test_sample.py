from sample import add_and_one,double,say_hello,num_speak

# tests for add_and_one
def test_add_and_one_2_3():
    assert add_and_one(2,3) == 6

def test_add_and_one_0_2():
    assert add_and_one(0,2) == 3

def test_add_negatives():
    assert add_and_one(-1,-2) == -2

# tests for doubler
def test_double_0():
    assert double(0) == 0

def test_double_2():
    assert double(2) == 4

def test_double_negatives():
    assert double(-2) == -4

# tests for hello
def test_say_hello_name():
    assert say_hello("roy") == "hello roy"
 
def test_say_hello_number():
    assert say_hello(3) == "hello 3"
 
def rest_num_speak_42():
    assert num_speak(42) == "forty-two"

def rest_num_speak_0():
    assert num_speak(0) == "zero"
