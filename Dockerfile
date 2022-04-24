FROM public.ecr.aws/lambda/python:3.8

RUN mkdir -p /app
COPY main.py /app/
COPY htmlDirectory/ /app/htmlDirectory/
COPY playerdata_df/ /app/playerdata_df/
COPY requirements.txt /app/

WORKDIR /app
RUN pip install -r /app/requirements.txt
EXPOSE 8080
CMD [ "main.py" ]
ENTRYPOINT [ "python" ]