
# Select the images from the dockers is based
FROM python:3.9-buster

#Create a File where the app it's going to run
RUN mkdir /home/family_app_1

#Stablish the Workdir
WORKDIR /home/family_app_1

# Copy <origin folder> to <origind destino>>
COPY . /home/family_app_1

# Install Pip & Enable an venv envairoment
RUN python3.9 -m pip install --upgrade pip 
RUN python3.9 -m venv /opt/venv

# Activate envairoment & Install dependencies:
RUN . /opt/venv/bin/activate 
#RUN cd Family_Project
RUN pip3 install -r requirements.txt

#Established a work directory
WORKDIR /home/family_app_1/Family_Project
#RUN cd Family_Project
#RUN cd /home/family_app_1/Family_Project

CMD [ "python3.9", "manage.py", "runserver", "0.0.0.0:8000" ]

EXPOSE 8000
