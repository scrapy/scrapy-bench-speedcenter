FROM scrapy-bench

COPY requirements.txt .
RUN python3.6 -m pip install -r requirements.txt

COPY . .
