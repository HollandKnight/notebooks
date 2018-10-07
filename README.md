# HK Lawyer Notebook

**A Jupyter notebook designed for lawyers.**

![alt text](https://github.com/jndewey/dashboard/blob/master/dashboard/Screenshot_2018-10-06%20%20lawyer_notebook-0(5).png)

![alt text](https://github.com/jndewey/dashboard/blob/master/dashboard/Screenshot_2018-10-06%20%20lawyer_notebook-0(6).png)

![alt text](https://github.com/jndewey/dashboard/blob/master/dashboard/Screenshot_2018-10-06%20%20lawyer_notebook-0(6).png)


## Try it live

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/oschuett/appmode/master?urlpath=%2Fapps%2Fexample_app.ipynb)


## Description

To Do
## Deployment

1. Install [Docker](https://docs.docker.com/engine/installation/).
2. git clone this repository
3. `docker build --tag appmode_dev ./`
4. `docker run --init -ti -p8888:8888 appmode_dev`
5. Browse to `http://localhost:8888/apps/lawyer_notebook.ipynb`
