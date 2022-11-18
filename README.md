## Starting Machine Learning Project 

## Software and Account Requirement 
1. [GitHub Account](https://github.com)
2. [Heroku Account](https://dashboard.heroku.com/login) 
3. [Vs Code](https://code.visualstudio.com/downloads) 
4. [Git CLI](https://git-scm.com/downloads)

create conda environment 
```

conda create -p venv python==3.8 -y
```

conda activate venv/ 
```
pip install -r requirements.txt
```
to add files to git 
```
git add.
```
or
```
git add filename 
```

> Note to ignore file and folder you should include those file to .gitignore file

to check git status 
```
git status 
```

to check all the versions maintained by git
```
git log
```
To create version/commit all changes by git 
```
git commit -m "message"
```
To send version/changes to github
```
git push origin main 
```
to check remote url 
```
git remote -v
```
TO setup CI/CD pipeline in heroku  we need 3 Information 

1. HEROKU_EMAIL = abdulahad2045@gmail.com
2. HEROKU_API_KEY = 4deb4643-7a68-4b30-bfac-07a209823c54
3. HEROKU_APP_NAME=new-ml-app-1

BUILD DOCKER IMAGE 
```
docker build -t <image-name>:<tagname> .
```
> Note :Image name for docker must be in lower case 

To list docker image 
```
docker images 
```
run docker images 
```
docker run -p 5000:5000 -e PORT = 5000 8cab0a520587
```



 




