# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 11:28:31 2019

@author: Jing
"""

import math

import matplotlib.pyplot as plt

from .Generaldistribution import Distribution

class Binomial(Distribution):
    
    """ Binomial distribution class for calculating and 
    visualizing a Binomial distribution.
    
    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats to be extracted from the data file
        p (float) representing the probability of an event occurring
        n (int) number of trials
            
    """
    def __init__(self, prob=0.5, size=20):
        
        self.n = size
        self.p = prob
        
        Distribution.__init__(self, self.calculate_mean(), self.calculate_stdev())
        
    def calculate_mean(self):
        
        """Function to calculate the mean from p and n
        
        Args: 
            None
        
        Returns: 
            float: mean of the data set
    
        """
        self.mean = 1.0 * self.n * self.p
        
        return self.mean
        
    def calculate_stdev(self):
        
        """Function to calculate the standard deviation from p and n.
        
        Args: 
            None
        
        Returns: 
            float: standard deviation of the data set
    
        """        
        self.stdev = math.sqrt(self.n * self.p * (1.0 - self.p))        
        
        return self.stdev
      
    def replace_stats_with_data(self):
        
        """Function to calculate p and n from the data set
        
        Args: 
            None
        
        Returns: 
            float: the p value
            float: the n value
    
        """   
        self.n = 1.0 * len(self.data)
        self.p = 1.0 * sum(self.data) / len(self.data)
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev()

        
        return self.p, self.n
    
    
    def plot_bar(self):
        
        """Function to output a histogram of the instance variable data using 
        matplotlib pyplot library.
        
        Args:
            None
            
        Returns:
            None
        """
        plt.bar(x = ['0', '1'], height = [(1 - self.p) * self.n, self.p * self.n])
        plt.title('Bar chart of the data')
        plt.xlabel('Outcome')
        plt.ylabel('Count')


    def pdf(self, k):
        """Probability density function calculator for the binomial distribution.
        
        Args:
            k (float): point for calculating the probability density function
            
        
        Returns:
            float: probability density function output
        """
        
        n = self.n
        p = self.p
        
        a = 1.0 * math.factorial(n) / (math.factorial(k) * math.factorial(n - k)) 
        b = p ** k * (1 - p) ** (n - k)
        
        pdf = a * b
                  
        return pdf
        
    
    def plot_bar_pdf(self):

        """Function to plot the pdf of the binomial distribution
        
        Args:
            None
        
        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot
            
        """
        x = []
        y = []
        
        for k in range(int(self.n) + 1):
            x.append(k)
            y.append(self.pdf(k))
            
        # make the plots
        plt.bar(x, y)
        plt.title('Distribution of the binomial distributed outcomes')
        plt.xlabel('Outcomes')
        plt.ylabel('Probability')
        
        plt.show()
        
        return x, y
    
    def __add__(self, other):
        
        """Function to add together two Binomial distributions with equal p
        
        Args:
            other (Binomial): Binomial instance
            
        Returns:
            Binomial: Binomial distribution
            
        """
        
        try:
            assert self.p == other.p, 'p values are not equal'
        except AssertionError as error:
            raise
            
        result = Binomial()
        result.p = self.p
        result.n = self.n + other.n
        result.calculate_mean()
        result.calculate_stdev()
            
        return result
    
    def __repr__(self):        
 
        """Function to output the characteristics of the Binomial instance
        
        Args:
            None
        
        Returns:
            string: characteristics of the Binomial object
        
        """
        return 'mean {}, standard deviation {}, p {}, n {}'.format(self.mean, self.stdev, \
                     self.p, self.n)
