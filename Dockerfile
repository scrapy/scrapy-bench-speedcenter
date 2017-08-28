FROM scrapy-bench

WORKDIR /speedcenter

RUN python2.7 -m pip install uWSGI==2.0.15 --user

COPY requirements.txt .
RUN python2.7 -m pip install -r requirements.txt --user

COPY . .

RUN cd center && \
    python2.7 manage.py collectstatic --noinput

ENTRYPOINT ["bash", "entrypoint.sh"]
