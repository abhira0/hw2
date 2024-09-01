# hw2
Second SE homework on Debugging

---
### Steps
1. Running autopep8 on all files
    ```bash
    autopep8 -i src/*
    ```
2. Running pylint
   ```bash
   pylint src/* >> src/post_traces/pylint.txt # first time
   pylint src/* # iteratively
   ```
3. Running pyright
   ```bash
   pyright src/* >> src/post_traces/pyright.txt # first time
   pyright src/* # iteratively
   ```