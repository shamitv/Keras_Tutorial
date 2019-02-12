# Keras_Tutorial
Tutorial that demonstrates how to 
   
   1. Generate a curve in Excel
   2. Read and visualize the curve in Jyputer 
  3. Build and train a model to Fit the curve with Keras
  4. Plot output of the model 

#Installation of Python Modules 

pip3 install plotly openpyxl sklearn pandas keras ipynb

# Define curve in Excel

Curve is defined as a formula, this formula is evaluated for values of x to get curve

![Excel Formula](images/excel_formula.png)

![Excel Plot](images/excel_plot.png)

# Read data from Excel

Notebook "showData.ipnyb" demostrates how to read data from Excel and 
plot it with Plotly.

![Load Data](images/loadData.png)
![Plot Data](images/plotData.png)

Zoom of plot to show test data (Test's color is kind of Orange)

![Plot Zoom](images/plotData_Zoom.png)

#Train and visualize results

"trainAndRunModel" notebook has code for defining and training a model in Keras 

Model definiton:
![Model Def](images/defineModel.png)

Training:

This code 

1. Prepares data in input/output format of Neural network
2. Trains the network
![Training](images/trainModel.png)

Predictions from the Model and Visualization :

![Predictions and Plot](images/predictAndPlot.png)