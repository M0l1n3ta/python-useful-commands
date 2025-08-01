
## install dependencies

```bash
pip3 install requests pytest pytest-html

```


## Generate Htmls report

```bash
pytest -q api-example_test.py  --self-contained-html --html=./reports/report.html

```