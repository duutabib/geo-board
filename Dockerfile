FROM ubuntu:20.04

USER root

RUN apt-get update

# Install required tools.
RUN apt-get install -y \
	gcc \
	make \
	flex \
	bison \
	byacc \
    python3 \
    pip \
	git

# Install python tools.
RUN pip install pandas 


# Clone repo & perform standardization
RUN git clone https://github.com/duutabib/geo-board.git && \
    cd geo-board/ && \
    python3 ./scripts/cleaner.py
    
WORKDIR /geo-board/
