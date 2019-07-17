# Neptune
Neptune is an education project where I will try to build a containerized nano-service that productizes a machine learning model. The project will include the following:

1. [x] A standardized conda environment 
1. [x] A machine learning training workbook that makes proper use of sklearn's pipeline and gridsearch tools.
2. [x] A serialized machine learning model stored on S3
3. [x] A very simple Flask app that will function as REST API.
4. [ ] The app will be containerized using Docker
5. [ ] The app will be deployed on an AWS EC2 instance

## The conda environment
[conda](https://docs.conda.io/projects/conda/en/latest/user-guide/overview.html) is both a package manager and a virtual environment manager. 

The virtual environment functionality solves for critical dependencies between packages and package versions. For example a machine learning model created by one version of sklearn might not run when loading it into a different version of sklearn.

The other advantage of using conda as an environment manager is that we can install a complete suite of tools (e.g. spyder and jupyter notebooks) with which to develop our project, knowing that each tool will be accessing the same environment. In short, so long as the program works in our defined project environment, we can be confident that it will work on another machine so long as we replicate our environment. 

See the documentation for [managing conda environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#).

### Creating the neptune environment
The neptune environment is already defined in the environment.yml file. To clone the environment on your machine, run the following code:

```
$ conda env create -f environment.yml
```

Once the neptune environment exists you can activate it by running `$ conda activate neptune`

