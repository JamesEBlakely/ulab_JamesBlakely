{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "3223c450-d9ba-466d-86eb-4cb294dd8f22",
   "metadata": {},
   "source": [
    "# Curve Fitting with SciPy (and Astropy... with time permitting) \n",
    "Today we will explore curve fitting with SciPy and Astropy! Curve fitting is the process of finding a mathematical function in an analytic form that best fits our set of data. We will mainly be working with SciPy today, so here is a bit of background. SciPy is a scientific computation library that uses NumPy underneath. Lots of useful functions for optimization, statistics and signal processing. Like Numpy and Astropy, SciPy is open source and can be used freely! Fun Fact: SciPy was created by NumPy's creator Travis Olliphant. "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0c9d1581-80fa-4c06-a66f-1a93fe2234bc",
   "metadata": {},
   "source": [
    "## Starting With Fitting Polynomials With NumPy\n",
    "\n",
    "When our data doesn't follow a straight line, the next best fit is a curve. The simplest way to fit a curve is with a polynomial (typically quadratics or cubics). Generally we want at least one data point more than orders of our polynomial but its better to have many many more data points than order of your polynomial fit. Its better to aim for double the data points for your order. Let's start by fitting data with polynomials via NumPy.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2cfc8252-b05a-4bcf-a507-811590c85aca",
   "metadata": {},
   "source": [
    "### Import Necessary Packages"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6eea0379-94e8-42e1-b3df-ef7b5c5c7021",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4037f8f1-8e3a-4eec-93d0-5fb028449619",
   "metadata": {},
   "source": [
    "### Generate some random data\n",
    "It doesn't really matter how this is being done. We are just playing around with fake data :)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "88ca5e9f-d3b0-48d4-9bb8-079e0dee0a3e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create the fake distribution of data\n",
    "m = 3.5 # Setting initial parameters for our \"fake\" data\n",
    "n = -2.8\n",
    "o = 0.5\n",
    "\n",
    "np.random.seed(0) # By setting this value to 0, we specify what \"random\" numbers we want numpy to give us\n",
    "x = np.linspace(0, 10, 50) # Setting a range of values for our distribution\n",
    "y = m * x**2 - n * x + o + np.random.normal(0, 7, 50) # Creating a polynomial distribution with error"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0d3cc779-561f-4b91-a53f-cb74f3a0475d",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Plot the fake data"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d3b942a5-4754-4c88-8e98-62167dcc0712",
   "metadata": {},
   "source": [
    "### Fit data with NumPy\n",
    "\n",
    "Given the name ``np.polyfit`` we are looking to fit a polynomial function of the form:\n",
    "\n",
    "$$y = ax^2 + bx^2 + c$$\n",
    "\n",
    "Therefore we are looking for 3 constants to satisfy our equation:\n",
    "* a = quadratic term\n",
    "* b = linear term\n",
    "* c = constant term"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "070b9ab0-aa69-4545-b90f-ec8ee6be1404",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Fit a polynomial using numpy's polyfit"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "70c716f2-b50a-4854-912a-f01af4bbafea",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Print out the coefficients\n",
    "print(\"Coefficients of the quadratic polynomial:\")\n",
    "print(\"a = {:.2f}\")\n",
    "print(\"b = {:.2f}\")\n",
    "print(\"c = {:.2f}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "11d30974-169f-4f2a-9e95-faeeae23a1d6",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Print final equation\n",
    "print(\"y = {:.2f} x^2 + {:.2f}x + {:.2f}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "56670190-5f06-4dab-96de-e32e4dfd674c",
   "metadata": {},
   "source": [
    "## Question\n",
    "\n",
    "How well do these parameters match up with the ones we assigned at the beginning? \n",
    "\n",
    "Let's see how our model looks against our data."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6c25b230-a443-418f-bf28-4b6e17bf68ff",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Plot random data and NumPy's fit"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9952d06a-dd09-4b90-bfd9-cb147815e7e4",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Check how good of a fit\n",
    "print(\"Chi-squared value:\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9db3844d-a780-4856-bd14-020652e0555e",
   "metadata": {},
   "source": [
    "### Yikes! \n",
    "That's not to good of a chi-squared value. But that's not necessarily our model's fault. What happens if we make our distribution less noisy? (i.e. have less error) What happens to our model's parameters?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3cfe5748-c28d-4f3e-b1fd-b4a5598f4af6",
   "metadata": {},
   "outputs": [],
   "source": [
    "# New distribution\n",
    "y = 3.5 * x**2 - 2.8 * x + 0.5 + 0.2 * np.random.normal(0, 1, 50) # Creating a polynomial distribution with error"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "65d39c48-8f44-420c-9ad9-9ea45c84a0de",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Define the Model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c0233536-81cc-40de-b23b-f27c94a3d715",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Plot new distribution with model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9f013b34-73ff-4a28-9f36-669119f91b25",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Print coefficients and chi-squared\n",
    "print(\"Coefficients of the quadratic polynomial:\")\n",
    "print(\"a = {:.2f}\")\n",
    "print(\"b = {:.2f}\")\n",
    "print(\"c = {:.2f}\")\n",
    "print(\"Chi-squared value:\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e248feb5-8380-40e0-ac45-f3668829c776",
   "metadata": {},
   "source": [
    "## SciPy Linear Fitting\n",
    "\n",
    "By using SciPy we can fit our data with more than just polynomials. But Scipy fitting is more complicated than NumPy's so let's take a step back and first only consider a linear fit."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3a137702-9a39-411e-b858-0d3bab03be3b",
   "metadata": {},
   "source": [
    "### Import Necessary Packages"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9a0ac108-6f86-4813-91b1-6fd434183686",
   "metadata": {},
   "outputs": [],
   "source": [
    "from scipy.optimize import curve_fit"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f6147164-dce7-4e6a-b50e-ac5e5bc20d15",
   "metadata": {},
   "source": [
    "### Generate some random data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "53903cd6-f508-4fc4-9d88-788e0084fe2d",
   "metadata": {},
   "outputs": [],
   "source": [
    "# How the fake data isn't too imporant, but we are doing it again :)\n",
    "m = 0.5\n",
    "b = 3         # Arbitrary parameters for data generation\n",
    "sigma = 1     # Noise\n",
    "n = 20        # Number of points to generate\n",
    "xdata = np.arange(0, n, 1)\n",
    "ydata = m * xdata + b + sigma * np.random.standard_normal(size=n) # Generate y values according to the random model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "851501bc-9747-498c-9285-3802781d6855",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Plot the fake data"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8e70f612-9980-4ffc-91a0-f9ed996a3c1b",
   "metadata": {},
   "source": [
    "### Fit data with Scipy\n",
    "\n",
    "Now lets fit a linear model to our data, which will take the following form:\n",
    "\n",
    "$$y = mx + b $$"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "164196d7-1bfb-4654-ae1e-0532b372698f",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Define model equation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "80603f74-6609-48c8-babe-8b2331f12a99",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Guess parameters"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "09d9dadc-473f-4af0-be83-3ea4ac15ee9a",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Use curve_fit"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ad716077-03b0-45e6-b020-9222953c1ffa",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Print parameters with error"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "839c33b4-68b4-4b5d-9b6a-d01a0fc35643",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Print final equation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9bcc6eb3-77ea-475e-a586-11a7668cf849",
   "metadata": {},
   "outputs": [],
   "source": [
    "# We need to define new arrays of x to plot the fit line\n",
    "x = np.linspace(xdata.min(), xdata.max(), 100)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f584c066-5d7a-4f3d-907c-f1bd03e4e8ec",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Use the outputted parameters from curve_fit and the model equation to create an array of y values "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cf2e4733-56eb-46ff-8a37-2e667a2808f0",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Plot the data and model"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7d3f5938-8df7-43e9-a988-6318792be8bf",
   "metadata": {},
   "source": [
    "## Scipy Curve Fitting\n",
    "\n",
    "Let's explore further the capabilities of SciPy."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b3b72b8f-d8c3-44d2-8f8e-1640bb57124e",
   "metadata": {},
   "source": [
    "### Generate some random data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "23f9e9a0-f137-4fdc-8530-14cf9c968d68",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Now we are going to generate some fake data for a Gaussian distribution\n",
    "x = np.linspace(-5, 5, 100)\n",
    "y = 3 * np.exp(-(x - 1.5)**2 / 2) + np.random.normal(0, 0.2, 100)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cb974547-0ce4-4edf-aa0e-2d41418338c8",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Plot the fake data"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "610016ff-dde6-4eec-bf80-4ec9f4701180",
   "metadata": {},
   "source": [
    "### Fit data with SciPy\n",
    "\n",
    "Now lets move on to more complicated Gaussian function of the form:\n",
    "\n",
    "$$y = ae^{-\\frac{1}{2}\\left(\\frac{x - \\mu}{\\sigma} \\right)^2 } $$"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "aca6d423-8dbc-4bd4-a82b-4b6800c37a68",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Define our model\n",
    "def gaussian(x, amplitude, mean, stddev):\n",
    "    return amplitude * np.exp(-(x - mean)**2 / (2 * stddev**2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e476ae97-efa1-4bb0-9a09-8fce0e7affbf",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Parameters"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "52d5ca93-0bee-4825-8bdf-bb4efa138f03",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Curve_fit"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5582db5c-c5af-4d11-b0c0-956592d93b7d",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Define model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a10b76f3-766c-4604-a790-2099d8095295",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Plot"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d61e5a2d-7af2-4cbe-9567-2eee09548de2",
   "metadata": {},
   "source": [
    "## AstroPy Modelling\n",
    "\n",
    "AstroPy also has lots of capabilities for modelling. Here is an example below:"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6d50dce2-fe4a-435a-9c7d-20891be90787",
   "metadata": {},
   "source": [
    "### Import Necessary Package"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "79c0f6ad-38c3-4eb8-9e09-57bc8a1c7b31",
   "metadata": {},
   "outputs": [],
   "source": [
    "from astropy.modeling import models, fitting"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3bb27c8a-a3d1-4969-9e94-3cad5d621395",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Generate data\n",
    "x = np.linspace(-5, 5, 100)\n",
    "y = 2.0 / ((x - 1.5) ** 2 + 0.5 ** 2)  # Sharper peaked Gaussian (Lorentzian) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "82889f7a-402b-4560-9f1a-a6f28a0fb1d3",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Add noise\n",
    "np.random.seed(0)\n",
    "y += np.random.normal(0.0, 0.1, x.shape)  # Reduced standard deviation of noise"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9ec4f9e7-9970-4781-befc-8985da523fb5",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Define a Lorentzian model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "30c90c4b-376b-4266-8655-374f7e558722",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Define a fitter"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c81efea2-36d0-47e7-aff2-31e2f68d4ec9",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Fit the model to data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "76485d35-8312-4a3e-bab5-ca6b28f5ea79",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Plotting"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "62c3f7ce-c9d2-4ae8-93fe-bbd5cb1ad9e8",
   "metadata": {},
   "source": [
    "## Extra SciPy Stuff"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7e573c29-0b30-4406-89bc-d58fd173eb51",
   "metadata": {},
   "source": [
    "### Import Necessary Packages"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "df6289fe-b51a-4c9a-b5e3-e7ef28da7623",
   "metadata": {},
   "outputs": [],
   "source": [
    "from scipy.optimize import root\n",
    "from scipy.optimize import fsolve"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b7755593-6771-4048-85a1-3147ada3577f",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Find the roots with root function"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ecf2750c-02ca-44e5-991f-18aabbe7dd56",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Find the roots with fsolve function"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}