# set base image (host OS)
FROM python:3.8

# set env variable
ENV API_KEY "AAAAAAAA-BBBB-CCCC-DDDD-EEEEEEEEEEEE"
ENV stocks "PTON,PLTR,PUBM,UPST,DASH"

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY src .

# command to run on container start
CMD [ "sh", "-c", "python ./bot.py ${API_KEY} ${stocks}" ]