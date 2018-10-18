# Citibike review of Junjie Tsai(jc9033)
## Author: Shijia Gu(sj5718)


## A. Verify that their Null and Alternative hypotheses are formulated correctly
      Junjie formulated reasonable null and alternative hypotheses. He includes both a written hypothesis and formulas. Also, he states a significance level of 0.05.

      However, he had a typo in writing the formula of the alternative hypothesis, which should be H1 instead of H0 again. 
## B. Verify that the data supports the project (the data has the appropriate features to answer the question, and if the data was properly pre-processed to extract the needed values)
      Junjie properly extracts the necessary data which is tripduration. 
     
      However, based on his hypothesis, date is not necessarily related because he did not aim to examine the differences among every day in a week. Furthermore, in his hypothesis, he defined short trips that took less than 10 minutes and long trips that took more than 10 minutes, but citibikes.csv measures time in seconds and he redefine short trips that took less than 600 seconds and long trips that took more than 600 seconds, whish is a little confusing.
## C. Choose an appropriate test to test _H0_, given the type of data and the question asked
      I will choose Z-test, given junjie wants to compare the proportions of short trips and long trips from the same population. Also， the null hypothesis can be approximated by a normal distribution because of the central limit theorem. Thus, Z test can test the difference between means of these two samples.

## D. Suggest variations on the question
      Junjie need to provide a mathematical definition of short and long trips and drop the data:date he does not need.
      He just look at the data in January. Maybe he can dig more during warmer days. 

