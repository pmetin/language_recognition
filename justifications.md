# Justifications

## Git

I tried to commit regularly, so as to have an appropriate, concise message for each one of my commits. I created and merged a second branch with no particular issue (except one related to AI, see AI section).

## Tests

I tried to test very basic features, like the presence of accurate statistics in `compute_stats()`. I also tested edge cases, like inputs that don't include letters in the language detection workflow, as well as the case where `compute_stats` gets an empty input, which would result in an impossible division by 0. I also tested what happens with `visualize_stats` if it processes an empty dictionary, and decided to have the function raise an error so as not to break the workflow.

## Documentation and type hints

I decided to include small docstrings to explain tests as well.

I did not include much documentation in `web_app.py` because it doesn't do much except display the results of the various function; although I did comment the file. I also did not include `web_app.py` in the Github Actions pdoc generation because it was both a little unnecessary and somehow broken.

## License

I chose the Apache 2.0 License because it is both very widely used and very permissive while maintaining original copyright.

## AI

I used ChatGPT for several parts of the projects :

* Feature suggestions (which statistics to include, relevant tests)
* Code generation (using matplotlib, including data on Streamlit using DataFrames, Counter, Try/Except)
* General code structure (tests, Type hints)
* Git guidelines (Setting up Github Actions, managing branches)

A concrete example: I asked ChatGPT to generate a few relevant tests for my functions and it suggested I test the empty input case that would result in a division by 0 (in `compute_stats.py`).

In all of these areas I asked several questions, got explanations and examples, but in most cases I adapted/rewrote the code so that it would fit my ideas and so that I would understand what's going on. For example, ChatGPT suggested tests that were actually testing the `lang_detect` library, not the functions that I had wrote. I adapted some of them to fit my functions. Another example: I asked for help to switch easily between two already existing branches, and got this reply:
```bash
git switch -c newbranch
```
Obviously this suggestion is not appropriate as the branch already exists, and '-c' is used to create a new branch and switch to it immediately.
