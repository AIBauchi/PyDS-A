# Contributing guidelines

## Contributing to PyDS-A

Welcome to [AIBauchi/PyDS-A](https://github.com/AIBauchi/PyDS-A)! Before sending your pull requests, make sure that you __read the whole guidelines__. If you have any doubt on the contributing guide, please feel free to [state it clearly in an issue](https://github.com/AIBauchi/PyDS-A/issues/new) or ask the community in [AIBauchi](http://aibauchi.com.ng/).

## Contributing

### Contributor

We are very happy that you are considering implementing algorithms and data structures for others! This repository is referenced and used by learners from all over the globe. Being one of our contributors, you agree and confirm that:

- You did your work - no plagiarism allowed
  - Any plagiarized work will not be merged.
- Your work will be distributed under [MIT License](LICENSE.md) once your pull request is merged
- Your submitted work fulfils or mostly fulfils our styles and standards

__New implementation__ is welcome! For example, new solutions for a problem, different representations for a graph data structure or algorithm designs with different complexity but __identical implementation__ of an existing implementation is not allowed. Please check whether the solution is already implemented or not before submitting your pull request.

__Improving comments__ and __writing proper tests__ are also highly welcome.

### Contribution

We appreciate any contribution, from fixing a grammar mistake in a comment to implementing complex algorithms. Please read this section if you are contributing your work.

Your contribution will be tested by our [automated testing on GitHub Actions](https://github.com/AIBauchi/PyDS-A/actions) to save time and mental energy.  After you have submitted your pull request, you should see the GitHub Actions tests start to run at the bottom of your submission page.  If those tests fail, then click on the ___details___ button try to read through the GitHub Actions output to understand the failure.  If you do not understand, please leave a comment on your submission page and a community member will try to help.

If you are interested in resolving an [open issue](https://github.com/AIBauchi/PyDS-A/issues), simply make a pull request with your proposed fix. __We do not assign issues in this repo__ so please do not ask for permission to work on an issue.

Please help us keep our issue list small by adding `Fixes #{$ISSUE_NUMBER}` to the description of pull requests that resolve open issues.
For example, if your pull request fixes issue #10, then please add the following to its description:
```
Fixes #10
```

GitHub will use this tag to [auto-close the issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue) if and when the PR is merged.


## Getting Started

1. Fork the repository and clone it to your local machine.
2. Create a new branch for your contribution: `git checkout -b feature/your-feature-name`.
3. Make your changes and test them thoroughly.
4. Ensure your code follows our coding style and conventions.

   - Follow the PEP 8 style guide for Python code.
   - Keep your code clean, well-documented, and easy to understand.

5. If you are adding a new file or module, add a docstring explaining what the function or module does.
6. If you are editing an existing file, add your name to the author at the top, separated by a comma. *This applies only to people adding code or test cases.*
7. Commit your changes with clear and concise commit messages.
8. Push your changes to your fork: `git push origin feature/your-feature-name`.
9. Create a pull request (PR) to the `main` branch of this repository.

## Issues and Labels

We use GitHub issues to track tasks, enhancements, and bug reports. Feel free to pick up issues labeled with "hacktoberfest" if you're participating in Hacktoberfest.

## Communication

If you have questions or need assistance, join our community on [our Discord server](#) or open an issue.

## License

By contributing to this project, you agree that your contributions will be licensed under the [MIT License](LICENSE).

---

#### Coding Style

We want your work to be readable by others; therefore, we encourage you to note the following:

- Please write in Python 3.11+. For instance:  `print()` is a function in Python 3 so `print "Hello"` will *not* work but `print("Hello")` will.
- Please focus hard on the naming of functions, classes, and variables.  Help your reader by using __descriptive names__ that can help you to remove redundant comments.
  - Single letter variable names are *old school* so please avoid them unless their life only spans a few lines.
  - Expand acronyms because `gcd()` is hard to understand but `greatest_common_divisor()` is not.
  - Please follow the [Python Naming Conventions](https://pep8.org/#prescriptive-naming-conventions) so variable_names and function_names should be lower_case, CONSTANTS in UPPERCASE, ClassNames should be CamelCase, etc.

- We encourage the use of Python [f-strings](https://realpython.com/python-f-strings/#f-strings-a-new-and-improved-way-to-format-strings-in-python) where they make the code easier to read.

- Please consider running [__psf/black__](https://github.com/python/black) on your Python file(s) before submitting your pull request.  This is not yet a requirement but it does make your code more readable and automatically aligns it with much of [PEP 8](https://www.python.org/dev/peps/pep-0008/). There are other code formatters (autopep8, yapf) but the __black__ formatter is now hosted by the Python Software Foundation. To use it,

  ```bash
  python3 -m pip install black  # only required the first time
  black .
  ```

- All submissions will need to pass the test `ruff .` before they will be accepted so if possible, try this test locally on your Python file(s) before submitting your pull request.

  ```bash
  python3 -m pip install ruff  # only required the first time
  ruff .
  ```

- Original code submission require docstrings or comments to describe your work.

- More on docstrings and comments:

  If you used a Wikipedia article or some other source material to create your algorithm, please add the URL in a docstring or comment to help your reader.

  The following are considered to be bad and may be requested to be improved:

  ```python
  x = x + 2	# increased by 2
  ```

  This is too trivial. Comments are expected to be explanatory. For comments, you can write them above, on or below a line of code, as long as you are consistent within the same piece of code.

  We encourage you to put docstrings inside your functions but please pay attention to the indentation of docstrings. The following is a good example:

  ```python
  def sum_ab(a, b):
      """
      Return the sum of two integers a and b.
      """
      return a + b
  ```

- Write tests (especially [__doctests__](https://docs.python.org/3/library/doctest.html)) to illustrate and verify your work.  We highly encourage the use of _doctests on all functions_.

  ```python
  def sum_ab(a, b):
      """
      Return the sum of two integers a and b
      >>> sum_ab(2, 2)
      4
      >>> sum_ab(-2, 3)
      1
      >>> sum_ab(4.9, 5.1)
      10.0
      """
      return a + b
  ```

  These doctests will be run by pytest as part of our automated testing so please try to run your doctests locally and make sure that they are found and pass:

  ```bash
  python3 -m doctest -v my_submission.py
  ```

  The use of the Python builtin `input()` function is __not__ encouraged:

  ```python
  input('Enter your input:')
  # Or even worse...
  input = eval(input("Enter your input: "))
  ```

  However, if your code uses `input()` then we encourage you to gracefully deal with leading and trailing whitespace in user input by adding `.strip()` as in:

  ```python
  starting_value = int(input("Please enter a starting value: ").strip())
  ```

  The use of [Python type hints](https://docs.python.org/3/library/typing.html) is encouraged for function parameters and return values.  Our automated testing will run [mypy](http://mypy-lang.org) so run that locally before making your submission.

  ```python
  def sum_ab(a: int, b: int) -> int:
      return a + b
  ```

  Instructions on how to install mypy can be found [here](https://github.com/python/mypy). Please use the command `mypy --ignore-missing-imports .` to test all files or `mypy --ignore-missing-imports path/to/file.py` to test a specific file.

- [__List comprehensions and generators__](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions) are preferred over the use of `lambda`, `map`, `filter`, `reduce` but the important thing is to demonstrate the power of Python in code that is easy to read and maintain.

- Avoid importing external libraries for basic algorithms. Only use those libraries for complicated algorithms.
- If you need a third-party module that is not in the file __requirements.txt__, please add it to that file as part of your submission.

#### Other Requirements for Submissions
- If you are submitting code in the `data_structures/` directory, please also read [the dedicated Guideline](https://github.com/AIBauchi/PyDS-A/blob/main/pyds-a/data_structures/README.md) before contributing to our Project Euler library.
- The file extension for code files should be `.py`.
- Strictly use snake_case (underscore_separated) in your file_name, as it will be easy to parse in future using scripts.
- Please avoid creating new directories if at all possible. Try to fit your work into the existing directory structure.
- If possible, follow the standard *within* the folder you are submitting to.
- If you have modified/added code work, make sure the code compiles before submitting.
- If you have modified/added documentation work, ensure your language is concise and contains no grammar errors.
- Do not update the README.md or DIRECTORY.md file which will be periodically autogenerated by our GitHub Actions processes.
- Add a corresponding explanation to [Algorithms-Explanation](https://github.com/TheAlgorithms/Algorithms-Explanation) (Optional but recommended).
- All submissions will be tested with [__mypy__](http://www.mypy-lang.org) so we encourage you to add [__Python type hints__](https://docs.python.org/3/library/typing.html) where it makes sense to do so.

- Most importantly,
  - __Be consistent in the use of these guidelines when submitting.__
  - __Join__ us on [Discord](#) __now!__
  - Happy coding!

Writer [@Tinny-Robot](https://github.com/Tinny-Robot), Sep 2023.

By participating in this project, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md).

Thank you for considering contributing to PyDS-A! We welcome contributions from the community to help make this project better.