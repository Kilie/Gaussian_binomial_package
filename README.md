## Gaussian and Binomial Distributions 

This package can be used to calculate the mean, standard deviation, and probability density of Gaussian and binomial distributions. 

Additions of two Gaussian distributions or two binomial distributions, respectively, can be also conducted using this package. Note that when adding two binomial distributions, their probability will have to be equal. Otherwise, the code will raise an error. 

Finally, one can also visualize the probability density function of a given Gaussian distribution or binomial distribution using this package. 

This is a course project from the Data Scientist Nanodgree program from Udacity, as a practice for Object-Oriented Programming as well as making a package for publishing on PyPi. 

The package has been already published on PyPi. Therefore, it can be pip installed by using this command line pip install jx_distributions in your terminal if you want to try it out.  

## File Discription

There are 4 files in this folder, including:

> 1. Bionomialdistribution.py  which includes the code for calculating binomial distributions;

> 2. Gaussiandistribution.py which does the same thing for Gaussian distributions;

> 3. Generaldistribution.py which defines a class Distribution and read in the data;

> 4. README.md which includes important information about the package.

## Contributions

You are very welcome to contribute to this repository either by adding more functions to these two distributions or adding more distributions. Also, when you spot any problems with the code during using the package after pip installing it, please feel free to report it here. 

## About the Package

Note that beside the files in this repository, a few extra files are needed for successfully uploading this package to test.pypi.org and pypi.org. These files include a \__init__.py, a license.txt, a setup.cfg, and finally a setup.py. Except for the setup.py file, all the other files including the README.md file should be in one folder which is named as the package name. 

Once all the files are set up properly, they are ready to be uploaded to test PyPi and finally PyPi for other programmers to install for their own use.



