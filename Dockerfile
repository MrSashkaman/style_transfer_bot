FROM python:3.9
COPY ./requirements.txt /code/requirements.txt

WORKDIR python/app

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY model.py ./
COPY main.py ./

RUN useradd -m -u 1000 user
USER user
ENV HOME=/home/user \
	PATH=/home/user/.local/bin:$PATH

WORKDIR $HOME/app
COPY --chown=user . $HOME/app

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "7860"]
