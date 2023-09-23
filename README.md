## High-Frequency Trading Liquidity Research

This a **High-Frequency Trading Liquidity Research Project** written by **Sid Bhatia** *('24 BSQF, '25 MSML + MSFE)*, **Sid Peri** *('24 BSQF, '25 MSFE)*, and **Sam Friedman** *('25 BSQF)* on *05/25/2023*.

Please reach out with any questions via [LinkedIn](https://www.linkedin.com/in/siddharthbhatia555/) or email: [sbhatia2@stevens.edu](mailto:sbhatia2@stevens.edu)/[siddharth.bhatia789@gmail.com](mailto:siddharth.bhatia789@gmail.com).

### Project Description

Closely intertwined with the financial markets, liquidity stands as a critical factor of paramount importance. The scarcity of liquidity during trading hours can substantially escalate transaction costs, thereby exerting an adverse impact on the overall stability of the market. Drawing upon existing models, numerous liquidity measures have been derived from diverse market characteristics such as tightness, depth, resiliency, and trading dynamics. In our previous research, we diligently explored measures based on trades and the limit order book, efficiently clustering appropriate liquidity  metrics, and effectively identifying extreme tail events.

Building upon our previous efforts, this proposed research endeavors to advance further by developing a robust framework to analyze liquidity using High-Frequency Trading (HFT) data. The core objective of this study is to unravel invaluable insights and knowledge across various domains, encompassing the recognition and regulation of liquidity risk, the formulation of statistical machine learning models grounded in liquidity analysis, and the provision of alternative inputs for the thorough examination of financial networks.

### Track 1:

Use limit order book datasets to construct predictive models for the price movement. We will use high-frequency data provided by Refinitiv Tick History Dataset.

- Conduct a thorough literature review.
- Process large datasets (TAQ and LOB).
- Calculate liquidity measures.
- Construct predictive models (statistical and/or machine learning).

### Methodology and Data

The goal of this project is to use the TAQ data to calculate liquidity measures and use these liquidity measures in a predictive model for price movements. The main dependent variable we are looking to predict is calculated from the Trade price in the TAQ data. 

We will take a daily subset from 11:00 AM to 4:00 PM of data from the TAQ data. From this subset, we will further reduce our sample data to be 1 minute frequency data, giving us approximately 300 data points per day for each ticker (approximately because some minutes may not have data). 

For each minute of data, we take the first trade and all quotes occurring for that minute. After reducing the sample data from TAQ to this set time window, we will calculate specific liquidity measures using metrics from TAQ occurring within the minute.

These liquidity measures will serve as independent variables in our predictive model. The main dependent variable for the predictive model will be the price movement of the TAQ prices, calculated as the 1 minute return from the trade prices for the first trade occurring in one minute to the first trade occurring in the next minute. 

We will approach the predictive model as a classification problem. Rather than performing a regression to predict the actual return, we define a categorical variable of the return direction. This variable will take 2 possible values: Up, denoting an upward price movement, and Down denoting a downward price movement.

Once we obtain our final dataset of the Direction variable and the liquidity measures as independent variables, we will create three different classification models: Logistic Regression (LR), SVM (Support Vector Machine), and Random Forest Classifier (RF). 

We will first fit the models on all our independent variables, and then through a process of subset selection, we will determine the ideal combination of liquidity measures that minimizes the classification errors of our models. 

We will utilize a 70%-15%-15% split for training, validation, and testing data. By choosing different classification models, we can compare each of their results and determine the best model for our applications. 

The end goal will be to create a model that uses liquidity measures to accurately predict return direction on the TAQ data. 

Ideally, we would like to find a consistent subset of liquidity metrics that have high explanatory power for all models on our data. From the sample data, we will be creating our model for March 14, 2022 for CVX.

### Model Background and Implementation

We first filtered the TAQ data to only include rows with a timestamp between 11:00 AM and 4:00 PM. We then further subset this data to include entries
in 1 minute intervals. 

For each 1 minute interval, obtain all the trade data and all quotes for that minute and do this for each subsequent minute for the entire time frame. To represent the quoted bid and ask prices and sizes for each minute, average the quote data over each minute. 

We then calculated the values for the following set of liquidity metrics, which are the independent variables for our model:
- Turnover
- Market Depth
- Log Depth
- Dollar Depth
- Spread
- Relative Spread (Mid)
- Relative Spread (Last)
- Relative Spread (Log)
- Effective Spread
- Relative Effective Spread (Last)
- Quote Slope
- Log Quote Slope
- Adjusted Log Quote Slope
- Composite Liquidity
- Liquidity Ratio 1 (Amivest)
- Flow Ratio
- Order Ratio
- Illiquidity (Amihud)

The formulas for these metrics are included in the Appendix. 

For the purposes of this model being predictive in nature, we lag the direction variable by one minute. This means that for a specific minute timestamp, we have all the liquidity metrics calculated based on that minute of TAQ data and the direction from the return in the next minute. This way, we are using liquidity metrics in the current minute to predict market direction in the next minute, which was our goal.

For implementing the models, we first created baseline models for our LR, SVM, and RF by using all the features present (all liquidity metrics calculated). 

This baseline model serves as a benchmark for us to understand how accurate we are when using every possible liquidity metric as a predictor. 

We next went through a series of 2 different types of subset selection to try and determine if there are ideal liquidity ratios for predicting price movements.

The first method was implemented to maximize training accuracy:

We conducted an iterative process of forward subset selection to select the combination of features that maximized training accuracy. We then used these features that maximized train accuracy as the “ideal combination” and fit our model on the test set using this combination to determine if this set works well on unseen data.

The last method of subset selection was a check of Feature Importance on the SVM and Random Forest models:

For both these models, we can determine the fitted feature importance from the trained data. For the Random Forest, a metric known as the MDI or mean-decrease impurity is used. This metric in a tree-based model is calculated as the number of splits using that specific feature proportional to the total number of splits made for the tree. Therefore, a higher result would indicate more splits based on the feature, which shows that the feature has much more correlation and importance with the final result.

The SVM feature importance is based on the magnitude of the feature coefficients from the fitted model, with higher coefficients indicating more important features. 

From doing this Feature Importance Analysis, we look to gauge if any specific features show consistent importance across models, indicating that they could have high predictive power for return direction.

### Results

The following results (see code) show the confusion matrix and accuracy for our 3 models with the baseline features, subset selection features, and Feature Importance selected features. 

For the confusion matrix, the top-left square represents the accurate Up predictions, and the bottom-right square represents the accurate Down predictions. The top-right and bottom-left represent misclassifications on the test set. The accuracy is represented as the percentage of correct classifications of market direction. We also present the feature importance coefficients for the RF and SVM models as well as graphs showing the feature importance visually.

Some takeaways from these results are the high accuracy of the baseline models relative to the tuned models with a subset of liquidity metrics. In a way, this shows that perhaps all the liquidity metrics were relevant and that it is difficult to predict return direction with a limited set of liquidity metrics. 

From the feature importance, we see some interesting results. The metrics: Liquidity Ratio, Flow Ratio, and Turnover all appeared to be consistently important for all models. These metrics had the largest feature importance which would indicate they were most influential in the predictions.

### Conclusion

Through our research we have presented an advanced framework for liquidity analysis, highlighting the crucial role of liquidity in the financial markets and its potential to influence transaction costs and market stability. We have expanded our knowledge related to identifying and regulating liquidity risk and statistical model formulation grounded in liquidity analysis.

The research conducted has been able to identify crucial liquidity metrics from a variety of methods, such as using machine learning algorithms such as Logistic Regression, Support Vector Machine, and Random Forest. For our goal of predicting return direction at minute intervals, we observed that using a large set of liquidity metrics proves to be more effective than subsetting based on accuracy metrics.

In some way, this could be due to the nature of predicting at very small intervals, which could require more inputs for accurate predictions. When evaluating features individually through the feature importance of our SVM and RF models, Liquidity Ratio, Flow Ratio, and Turnover appeared as the most significant features. In addition, Random Forest was the method that had the best results in terms of the highest accuracy.

This suggests that changes in these measures can lead to significant alterations in the prediction outcomes, implicating their importance as a determinant of liquidity. The next step for this project would be to apply these liquidity metrics to different stock data to see if consistent results are achieved in terms of accuracy and feature importance.

### References:

- "A Study on Brexit: Correlations and Tail Events Distribution of Liquidity Measures", M. Kong, A. Salighehdar and D. Bozdog, Journal of Management Science and Business Intelligence (JMSBI), Vol. 3, No. 1, July 2018.
- "Detection of Rare Events in Multidimensional Financial Datasets with Zonoid Depth Functions", P. Golbayani and D. Bozdog, IEEE Symposium Series on Computational Intelligence (SSCI), pg. 1-6, 2017.
- "Liquidity Risk and Asset Movement Evidence from Brexit", D. Mago, A. Salighehdar, M. Parekh, D. Bozdog, and I. Florescu, IEEE Symposium Series on Computational Intelligence (SSCI), pg. 1-8, 2017.
- "Cluster Analysis of Liquidity Measures in A Stock Market Using High-Frequency Data", A. Salighehdar, Y. Liu, D. Bozdog, and I. Florescu, Journal of Management Science and Business Intelligence, Vol. 2, No. 2, August 2017.
- "Rare Events Analysis Using Multidimensional Liquidity Measures in Financial Markets", Margarita Zaika, MS Thesis, Stevens Institute of Technology, 2021
- "An Event Study of Brexit on Distribution Characteristics of Liquidity Measures", M. Kong, MS Thesis, Stevens Institute of Technology, 2017
