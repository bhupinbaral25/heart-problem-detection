FROM public.ecr.aws/lambda/python:3.8

LABEL author = "apkotabikash194@gmail.com"
LABEL description = "This is a sample lambda function"
COPY requirement.txt requirements.txt
RUN python -m pip install -r requirements.txt
LABEL author = "sskotabikash194@gmail.com"
COPY . .
CMD ["app.handler"]