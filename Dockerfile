FROM python:3.7.1

RUN mkdir /hyaml

WORKDIR /hyaml

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

RUN pip install pipenv

RUN pipenv install --dev

COPY hydra hydra
COPY tests tests

CMD pipenv run python -m xmlrunner tests/test_* && tar cvzf tests_output.tar.gz *.xml
