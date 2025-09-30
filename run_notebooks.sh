#!/bin/bash
# Execute notebooks sequentially using nbconvert (requires nbconvert)
jupyter nbconvert --to notebook --execute Churn_EDA_Preparation.ipynb --inplace
jupyter nbconvert --to notebook --execute Churn_Modeling.ipynb --inplace
echo "Notebooks executed."
