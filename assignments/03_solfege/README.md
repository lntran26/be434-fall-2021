# Solfege

For this exercise, we'll draw inspiration from the song "Do-Re-Mi" from _The Sound of Music_:

https://www.youtube.com/watch?v=drnBMAEA3AM

Your program will accept one or more positional arguments which may or may not name a syllable of [solfege](https://en.wikipedia.org/wiki/Solf%C3%A8ge).
If a given syllable is valid, you should print it followed by a comma and the the appropriate line from the following list:

* Do: A deer, a female deer
* Re: A drop of golden sun
* Mi: A name I call myself
* Fa: A long long way to run
* Sol: A needle pulling thread
* La: A note to follow sol
* Ti: A drink with jam and bread

For example, it should handle one day:

```
$ ./solfege.py Do
Do, A deer, a female deer
```

Or several:

```
$ ./solfege.py Do Mi Sol
Do, A deer, a female deer
Mi, A name I call myself
Sol, A needle pulling thread
```

If any argument does not name a day of the week, print 'I don't know "{note}"':

```
$ ./solfege.py Do Mi foo Sol
Do, A deer, a female deer
Mi, A name I call myself
I don't know "foo"
Sol, A needle pulling thread
```

If run with no arguments, it should print a short usage:

```
$ ./solfege.py
usage: solfege.py [-h] str [str ...]
solfege.py: error: the following arguments are required: str
```

And it should respond to `-h` or `--help` with a longer usage:

```
$ ./solfege.py -h
usage: solfege.py [-h] str [str ...]

Solfege

positional arguments:
  str         Solfege

optional arguments:
  -h, --help  show this help message and exit
```

Your program should pass all tests:

```
$ make test
pytest -xv --pylint --flake8 test.py
============================= test session starts ==============================
...
collected 14 items

test.py::PYLINT SKIPPED (file(s) previously passed pylint checks)        [  7%]
test.py::FLAKE8 SKIPPED (file(s) previously passed FLAKE8 checks)        [ 14%]
test.py::test_exists PASSED                                              [ 21%]
test.py::test_usage PASSED                                               [ 28%]
test.py::test_do PASSED                                                  [ 35%]
test.py::test_re PASSED                                                  [ 42%]
test.py::test_mi PASSED                                                  [ 50%]
test.py::test_fa PASSED                                                  [ 57%]
test.py::test_sol PASSED                                                 [ 64%]
test.py::test_la PASSED                                                  [ 71%]
test.py::test_ti PASSED                                                  [ 78%]
test.py::test_lower PASSED                                               [ 85%]
test.py::test_do_re PASSED                                               [ 92%]
test.py::test_mix PASSED                                                 [100%]

======================== 12 passed, 2 skipped in 0.42s =========================
```
