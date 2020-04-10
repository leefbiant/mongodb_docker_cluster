FROM python
RUN mkdir /work
COPY requirements.txt /work
RUN pip install --no-cache-dir -r /work/requirements.txt
WORKDIR /work
CMD ["python","app.py"]
