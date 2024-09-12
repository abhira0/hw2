# Homework 2
Second SE homework on Debugging

---
---

#### Quality
[![badge_pytest_status](https://img.shields.io/badge/PyTest-failing-red?logo=pytest&logoColor=white)](https://github.com/gitsetgopack/hw2/actions/runs/10821886315)
[![badge_code_coverage](https://img.shields.io/badge/coverage-0%25-red)](https://github.com/gitsetgopack/hw2/actions/runs/10821886315)
[![badge_total_tests](https://img.shields.io/badge/tests-0-blue?logo=pytest&logoColor=white&link=https%3A%2F%2Fgithub.com%2Fgitsetgopack%2Fhw2%2Ftree%2Fmain%2Ftests)](https://github.com/gitsetgopack/hw2/tree/main/tests)
[![badge_pylint](https://img.shields.io/badge/pylint-10.00-brightgreen)](https://github.com/gitsetgopack/hw2/actions/runs/10821886315)
[![badge_pyright](https://img.shields.io/badge/pyright-passing-brightgreen)](https://github.com/gitsetgopack/hw2/actions/runs/10821886315)

#### Standards
![autopep8](https://img.shields.io/badge/code%20style-autopep8-blue)
![license](https://img.shields.io/github/license/gitsetgopack/hw2)

#### Stats
![repo_size](https://img.shields.io/github/repo-size/gitsetgopack/hw2)
![pr_open](https://img.shields.io/github/issues-pr/gitsetgopack/hw2)
![pr_close](https://img.shields.io/github/issues-pr-closed/gitsetgopack/hw2)
![forks](https://img.shields.io/github/forks/gitsetgopack/hw2?style=flat)
![stars](https://img.shields.io/github/stars/gitsetgopack/hw2?style=flat)
![downloads](https://img.shields.io/github/downloads/gitsetgopack/hw2/total)

   
#### Tools & Technologies
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Python](https://img.shields.io/badge/python%203.13-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)



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
