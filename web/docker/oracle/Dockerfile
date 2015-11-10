FROM python:2.7
ADD . /code
WORKDIR /code
#Add oracle
#ENV LD_LIBRARY_PATH=$ORACLE_HOME/lib
RUN pip install -r requirements.txt
CMD python app.py
