**Author**: Thomas Isola (ti582) <br/>
**Assignment**: Perform a review of Shijia Gu's (sg5718) Assignment 2/HW4

## A. Verify that their Null and Alternative hypotheses are formulated correctly
*Praise*: Shijia formulated coherent and reasonable Null and Alternative hypotheses. Her method of including a proportion test in her hypotheses is very good, which was recommended in class as a better way of comparison. She includes both a written and formulaic version of her hypotheses, both of which make sense and agree with each other. She chooses a confidence level of 0.05 and states that at the beginning, which is good.

*Improvements*: Shijia does not connect her idea to her hypotheses. Her idea is that customers are less likely to choose biking for commuting compared to subscribers, but her hypotheses talk about biking on the weekends. As a person who bikes and commutes to work myself, I understand that she is trying to make the connection that people who bike more during the week are more likely to be commuting to work compared to people who bike on the weekend, which is more likely to be biking for pleasure. I would recommend that she explain this connection (weekday biking with commuting) more thoroughly in her idea and hypothesis statements. Additionally, she does not define what she means by customer. As a citibike user, I can assume that she means someone who only uses citibike on an occasional basis. It would add more clarity if she defined what a customer is. 

## B. Verify that the data supports the project (the data has the appropriate features to answer the question, and if the data was properly pre-processed to extract the needed values)
*Praise*: Shijia properly pre-processes (extracts) the necessary data (usertype and date), which, in my opinion, are sufficient to answer the question. She adds useful plots that support the ability to answer the question.

## C. Choose an appropriate test to test _H0_, given the type of data and the question asked
For this question, I suggest using the Chi-Square test of independence. This test is typically used to compare two unpaired groups (in this case customers and subscribers) who come from the same population, to determine if there is a significant difference between the two groups. In this case, it is determining whether there is a significant difference in the proportion of customers and the proportion of subscribers using Citibike on the weekends.

## D. Suggest variations on the question
I have a hard time coming up with a variation on the question because I think it is well formulated. However, if I had to come up with a variation, I would suggest the following:

*Idea*: The ratio of Citibike type riders during weekday peak hours is likely to be comprised of more subscriber type riders than customer type riders. 

*Null Hypothesis variation*: The proportion of customer type Citibike riders is greater or equal to the proportion of subscriber type Citibike riders during peak weekday hours (7am-10am and 4pm-7pm)

*Formula*: C_weekday,peakhour - S_weekday,peakhour >= 0 <br/>
Where C = customer proportion and S = subscriber proportion


