
# Text Indexer App

This Django project implements a RESTful API for analyzing text paragraphs. Users can input multiple paragraphs, and the API will store each paragraph along with word-to-paragraph mappings in a PostgreSQL database. The primary functionality is to search for a given word and retrieve the top 10 paragraphs where the word is present.


## Installation

Install my project with Docker.

You can install Docker to your machine using the link below.

#### Windows
https://docs.docker.com/desktop/install/windows-install/

#### Mac OS
https://docs.docker.com/desktop/install/mac-install/

Download and install git to clone the repo.

You can download git from the link : https://git-scm.com/book/en/v2/Getting-Started-Installing-Git

Clone the project to your machine using the command:
```bash
git clone https://github.com/krisk3/codemonk.git  
```


Open the terminal.

Open the project directory.

Run the command below to run the project.
```bash
docker-compose up
```

    
## Documentation
The [API Documentation](http://127.0.0.1:8000/api/docs/) can be accessed at: http://127.0.0.1:8000/api/docs/



## Steps

#### i) Create User
The API endpoint to create a new user is: http://127.0.0.1:8000/api/user/create/

#### ii) Generate Auth Token
The API endpoint to generate Token for Authentication: http://127.0.0.1:8000/api/user/token/

Keep a copy of the token to authenticate in step 3 and step 4.

#### iii) Add Text
The API endpoint to input textual data: http://127.0.0.1:8000/api/add-text/

Add token to headers to authenticate.

#### iv) Search
The API endpoint to search for paragraph by entering a word: http://127.0.0.1:8000/api/search-word/

Add token to headers to authenticate.






## Demo

- You can preview the demo working of the django project at: https://youtu.be/ytiX3hfYWOc

