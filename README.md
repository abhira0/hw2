# hw2
Second SE homework on Debugging

---

![badge_pylint](https://img.shields.io/badge/pylint-10.00-brightgreen.svg)
![badge_pyright](https://img.shields.io/badge/pyright-passing-brightgreen.svg)
![badge_total_tests](https://img.shields.io/badge/tests-7-brightgreen.svg)
![badge_code_coverage](https://img.shields.io/badge/coverage-100%25-brightgreen.svg)
![badge_pytest_status](https://img.shields.io/badge/PyTest-passing-brightgreen.svg)

---
### Steps
1. Install python requirements
   ```bash
   pip install -r requirements.txt
   ```
2. Running autopep8 on all files
    ```bash
    autopep8 -i src/*
    ```
3. Running pylint
   ```bash
   pylint src/* >> src/post_traces/pylint.txt # first time
   pylint src/* # iteratively
   ```
4. Running pyright
   ```bash
   pyright src/* >> src/post_traces/pyright.txt # first time
   pyright src/* # iteratively
   ```
5. Running pytest
   ```bash
   pytest
   ```