10, 2020-04-27
Aim: Python class and other packages: argparse, pandas, seaborn, matplotlib
In this last day tutorial, we are going to build a small software that can take arguments from command line, process data with object oriented programming, and output summary and figures.
Here are the steps:
1, Use argparse package to process arguments from command line
    Set -i (or --input) and -o (or --output)
2, Write functions in a separate script, including reading inputs and constructing objects.
    Construct a Gene object to store original data and average expression, fold changes between KD to WT
3, Output a table containing summary:
    For each gene, calculate average expression in KD and WT, then calculate a fold change
4, Also output a heatmap representing the summarized data table

Some notes:
1, You can set if the argument is required using ¡®required=True¡¯, and you can set default values etc.
2, When writing functions in another file, Example.py, use import Example as xxx to impiety
3, To create pandas DataFrame from lists, use list(zip(column1, column2)), to convert, then run pd.DataFrame, since pandas treats each list as a row if you run pd.DataFrame([column1, column2])
4, Use matplotlib and seaborn to plot and save the figure.
    Day10_ClassAndPackages.py -h
    Day10_ClassAndPackages.py -i GeneExp_Significant.csv -o Result
