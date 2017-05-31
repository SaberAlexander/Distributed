FROM python:2.7

MAINTAINER Saber_Alexander

# Copy the current directory contents into the container at /code
ADD . /JD_comments

# Set the working directory to /code
WORKDIR /JD_comments

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Define environment variable
ENV PATH /usr/local/bin:$PATH

CMD /usr/local/bin/scrapy crawl comments