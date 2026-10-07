### Company Bankruptcy Detection

This project was about predicting whether a company is likely to go bankrupt based on its financial information. I worked with around 6,800 company records and 95 financial features covering areas like profitability, liquidity, debt and financial stability.

I first cleaned and explored the data and then handled the class imbalance because bankrupt companies were much fewer than healthy companies. I used SMOTE on the training data to create synthetic samples for the minority class.

I then compared different machine learning models, including Logistic Regression, Decision Tree, Random Forest and XGBoost. I evaluated them using metrics such as precision, recall, F1-score and ROC-AUC rather than relying only on accuracy.

I also used feature importance and SHAP to understand which financial factors were influencing the predictions. Finally, I created a simple Streamlit interface where financial values can be entered and the model gives a bankruptcy prediction.

The main thing I learned from this project was that in a financial-risk problem, identifying the minority class correctly is more important than just achieving high overall accuracy.

