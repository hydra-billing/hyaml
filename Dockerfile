FROM python:3.7.1

RUN mkdir /hyaml

WORKDIR /hyaml

COPY setup.py setup.py
COPY README.md README.md

RUN pip install -e .[dev]

COPY hyaml hyaml
COPY tests tests

CMD pipenv run python -m xmlrunner tests/test_* && tar cvzf tests_output.tar.gz *.xml
