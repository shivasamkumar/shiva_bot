# Life Expectancy Analysis: Socioeconomic and Health Factors

## Introduction
This project analyzes life-expectancy data from 193 countries over a 15-year period to uncover the socioeconomic and health-related factors that most strongly influence lifespan. By examining variables such as alcohol consumption, health expenditure, disease prevalence (e.g., Hepatitis B immunization rate, HIV prevalence), GDP per capita, and mortality rates, the study seeks to identify and quantify key predictors of life expectancy. A suite of visualization and statistical tools—including correlation analysis, ANOVA, LASSO regression for feature selection, and both multiple and polynomial regression models evaluated via Akaike Information Criterion (AIC)—is applied to filter out noise, mitigate overfitting, and select the optimal predictive model. The insights generated can inform public-health policies and interventions aimed at improving population health and longevity. 

## Data & Methodology
- **Data Sources & Variables**  
  Life-expectancy and associated socioeconomic/health indicators were sourced for 193 countries, covering metrics such as per-capita alcohol consumption, government and private health expenditure, Hepatitis B immunization coverage, HIV prevalence, GDP per capita, and infant mortality rates. 
- **Data Cleaning & Preprocessing**  
  Handled missing values via exploratory missing-data visualization and appropriate imputation or record removal. Standardized and scaled continuous variables where necessary.  
- **Exploratory Analysis**  
  - **Missing-Values Visualization**: Generated plots to map the distribution and patterns of missing data.  
  - **Correlation Heat Map**: Computed pairwise Pearson correlations to identify multicollinearity and preliminary associations.  
- **Statistical Testing & Feature Selection**  
  - **Correlation Analysis**: Quantified linear relationships between predictors and life expectancy.  
  - **ANOVA**: Tested for significant group differences (e.g., by region or income level).  
  - **LASSO Regression**: Applied penalized regression to shrink less informative coefficients to zero, isolating the most impactful variables.  
- **Modeling & Evaluation**  
  - **Multiple Linear Regression**: Built a baseline predictive model incorporating selected features.  
  - **Polynomial Regression**: Tested non-linear transformations to capture curvature in relationships.  
  - **Model Selection via AIC**: Compared candidate models on the basis of goodness-of-fit penalized by complexity, selecting the model with the lowest AIC.

## Challenges Faced
- **Missing Data & Imputation**  
  Uneven reporting across countries and years required careful handling of missing values to avoid biasing results.  
- **Multicollinearity**  
  Strong correlations among economic and health variables (e.g., GDP vs. health expenditure) necessitated dimension reduction via LASSO to ensure model stability.  
- **Model Overfitting**  
  Balancing model complexity (polynomial terms) against overfitting risk required rigorous cross-validation and AIC-based selection.  
- **Heterogeneous Data Scales**  
  Variables measured on vastly different scales (e.g., percentage rates vs. monetary values) had to be standardized to enable fair coefficient estimation.  

## Results
- **Key Predictors Identified**  
  LASSO regression highlighted health expenditure, Hepatitis B immunization rate, GDP per capita, and alcohol consumption as the strongest predictors of life expectancy.  
- **Optimal Model Performance**  
  The final multiple regression model—selected via the lowest AIC—explained a substantial portion of variance in life expectancy (adjusted R² > 0.75) and satisfied diagnostic checks (normal residuals, homoscedasticity).  
- **Insightful Visualizations**  
  - **Heat Map**: Revealed clear clusters of correlated predictors, guiding feature selection.  
  - **Residual Diagnostics**: Confirmed model assumptions and identified no major outliers.  
- **Policy Implications**  
  Quantitative evidence from the regression coefficients suggests that incremental increases in health spending and immunization coverage could yield measurable gains in average lifespan across diverse national contexts.  

