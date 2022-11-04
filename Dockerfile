FROM ubuntu:latest
ENV DEBIAN_FRONTEND=noninteractive
ENV VIRTUAL_ENV=/opt/venv
RUN apt update && apt upgrade -y
RUN apt install -y build-essential python3-venv python3-dev git
COPY requirements.txt .
RUN git clone https://github.com/sparkfish/augraphy
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN pip install -r augraphy/requirements-dev.txt
RUN pip install -r requirements.txt
CMD uvicorn main:app --host=0.0.0.0 --workers=2
