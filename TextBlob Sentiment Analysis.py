# -*- coding: utf-8 -*-
"""TextBlob Sentiment Analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dUrL1Hzrls--4nUmOpvhkCPDkYe0L8Jj

**TextBlob Average Sentiment of Articles Relevant to Companies**

In this assignment, you will use TextBlob (a natural language processing package in Python) to gain an idea of the recent publicity of a firm. You will find twenty recent articles about a given company and calculate the average sentiment polarity and sentiment subjectivity. You will then compare your findings to fluctuations in the stock price over your researched time period to form a conclusion about the correlation between sentiment scores and stock price.

*Each text and code block in this Jupyter Notebook environment is interactive and can be edited by double clicking on the desired cell. Once a code block is selected, click on the play button in the left margin of the block to run the code. Alternatively, you can press (Ctrl+Enter)/(Cmd+Enter).*

*This notebook is structed so that informational text blocks are placed ABOVE the code block which accompanies it. Read the text blocks to understand each subsequent code block, then run the code.*

In the first code block below, you will import the required packages and functions for this natural-language processing assignment.
"""

from textblob import TextBlob
import nltk
nltk.download('punkt')

"""In the set of code below, you will initalize two empty lists to store the polarity scores and subjectivity scores from the *sentiment* function of TextBlob. Keeping the numerical values in lists ensures that the average score can be calculated simply later on."""

plist = list()
slist = list()

"""In the code below, you initialize a variable 'a1' to reference the text of the first article. Copy and paste your entire article contents (including the title) into a text file (.txt). Remove all empty lines and ensure that the words are formatted as one large paragraph in the text editor."""

a1 = TextBlob("Apple Watch Hasn’t Crushed the Swiss. Not Yet. When Apple’s chief executive, Timothy D. Cook, announced the Apple Watch in September 2014, the Swiss watch industry shuddered. The company’s arrival in the watch market carried an echo of the quartz revolution that devastated mechanical watchmaking in the 1970s, and some experts wondered whether the Apple Watch would cause a similar upheaval. Five years on, the Apple Watch and those from competitors like Samsung and Huawei have not had the crushing effect some Swiss brands had feared. But, as the category continues to grow, some experts say the worst may be yet to come. “We believe,” Mr. Cook said during the 2014 introduction, that the Apple Watch “will redefine what people expect from its category.” Which category was that? Well, Apple clearly sees itself as a watchmaker. And it has described the Apple Watch as “the No. 1 watch in the world,” comparing sales — although never providing actual numbers — to those of the traditional industry giants Rolex, Omega and Cartier. It might be an accurate assessment. The research firm Strategy Analytics has calculated that 22.5 million Apple Watches were shipped in 2018, while the Federation of the Swiss Watch Industry said the industry exported 23.7 million watches in the same period. Reports now suggest that 2019 will be the first year Apple outsells the entire Swiss watch industry by volume. And while sales in the traditional Swiss sector also have been growing, there are indications that the smartwatch expansion has come at the expense of its lower-price timepieces. The federation’s 2018 data shows a 5 percent decline in watches with export prices of less than 500 Swiss francs ( $511), so its growth is being achieved by a reliance on high-end timepieces. A New Category One thing Apple’s success produced was an entirely new category in Swiss watchmaking: the luxury smartwatch. A few high-profile brands, including Louis Vuitton, TAG Heuer and Montblanc, introduced smartwatches of their own. Others, like Frédérique Constant, produced hybrids: smartwatches that connect to smartphones but have analog displays like traditional watches. After an initial sales rush, signs are that the market for luxury smartwatches has been stagnating. (The picture isn’t entirely clear, however, as the manufacturers release so little data.) The Digital Luxury Group, a research and marketing company in Geneva that measures what it calls global “interest” by tallying internet searches, said the public’s curiosity about luxury smartwatches grew from 2015 to 2017, but has plateaued and, in some cases, declined. For example, according to its research, there were 60,500 Google searches for the TAG Heuer Connected Modular in April, compared with more than 350,000 in December 2015, the month after the watch was introduced. And some of TAG Heuer’s competitors can only dream of those numbers. Since their 2017 introductions, neither Louis Vuitton’s Tambour nor Montblanc’s Summit luxury smartwatches have exceeded 50,000 Google searches a month, the group’s information showed. And in April, there were just 1,300 searches for the Louis Vuitton watch. (The group said it had no evidence of how the data equated to sales.) However, Benedicte Soteras, Digital Luxury Group’s head of search, noted that interest in traditional mechanical watches had remained high since 2015. “It’s like the e-book and print,” she said. “You will always find audiences for both types of product.” An analyst with Counterpoint Research, a Hong Kong-based analytics company, said his review of market data indicated that luxury smartwatch sales had been declining. When TAG Heuer introduced the Connected Modular range, supported by the might of its LVMH Moët Hennessy Louis Vuitton parent organization, “there seemed to be an upswell,” said Peter Richardson, a research director at Counterpoint. “They seemed to be doing reasonable volumes — over 1,000 per week. But it seems to have faded off.” Mr. Richardson said he did not have precise information about shipments of the TAG Heuer smartwatch, but he said the “indicative direction was negative from 2017,” based on research by the Swiss investment bank Vontobel (which calculated a decline of 2 percent in TAG Heuer revenues in 2018). Change of Heart This might explain why luxury watch brands appear to have cooled on smartwatches. For example, Gucci’s “smartband” collaboration with the recording artist and entrepreneur Will.i.am that was announced at Baselworld in 2015 has disappeared. And the only luxury smartwatch introduction at the major Swiss watch fairs this year was TAG Heuer’s Connected Modular Golf Edition, a line extension. Analysts agreed that mixing luxury and the rapid obsolescence of a smartwatch was a consumer turnoff. Mr. Richardson of Counterpoint Research compared luxury smartwatches to the smartphones made by Vertu, his former employer. “It was incongruous that you had this amazing handcrafted piece of art and engineering, but underneath was this very bog-standard smartphone,” he said of the failed phone brand. “And that’s the danger in the luxury smartwatch world.” (Louis Vuitton, TAG Heuer and Montblanc all use Google’s Wear OS, an operating system available in much cheaper watches, like Fossil’s $275 Sport smartwatch.) Nicolas Baretzki, Montblanc’s chief executive, disagreed. “This segment will become so big there’s no reason why people would only want to wear ugly things on their wrist,” he said. “There is a clear opportunity to build a luxury segment here.” The company introduced its second smartwatch, the Summit 2, last year. And, Mr. Baretzski said, Summit sales “nearly doubled” in 2018. Montblanc’s parent company, Richemont, also does not disclose sales by brand. Peter Stas, chief executive of Frédérique Constant and Alpina, Citizen-owned Swiss brands whose hybrid luxury smartwatches sell in the same range as the Apple Watch, went further in his market analysis. Brands that “stay with a 30-year-old quartz caliber, they’re waiting to die,” he said, referring to Swiss companies yet to adopt the new technology. “Smartwatches are going to take more and more share of the total watch market.” He said his companies, which sit in the so-called “affordable luxury” midmarket segment that has been eroded by smartwatches, have been propped up by their smartwatch sales, which account for 15 percent of Frédérique Constant’s revenues and 30 percent of Alpina’s. And Mr. Stas, who also heads the smartwatch technology company MMT that produces modules for Frédérique Constant and Alpina watches, said he believed that the development of health apps would prompt more and more consumers, particularly older people, to adopt smartwatches. “Health prediction functionality is still in the baby phase,” he said. “It will become better and better, and this is where smartwatches will be devastating for the industry. Health is worth more than prestige.” From Retail At least one watch retail group said luxury smartwatches have had little impact on its business. “By nature, they’re peripheral to the luxury market,” said Brian Duffy, chief executive of the Watches of Switzerland Group, which operates 125 stores in Britain and 21 in the United States, and which began trading on London’s FTSE 100 in May. The group recently commissioned a customer survey, Mr. Duffy said, that found only 1 percent of the respondents considered a smartwatch to be a replacement for a traditional watch. “Luxury things you want to have forever,” he said, but with a smartwatch, “you’re buying technology that has an expiration date on it.” However, he added, that the group had sold 1.2 million pounds (about $1.5 million) worth of TAG Heuer’s smartwatches in Britain and “could have sold more” of Hublot’s limited edition Big Bang Referee 2018 FIFA World Cup Russia smartwatch. Some analysts said smartwatches actually have had a positive impact on sales of traditional watches. “Smartwatches and smartwatch retailers not normally in the watch retail business are bringing additional consumers into wearing a time-telling device on their wrist,” said Reginald Brack of the NPD Group, an information service company. “And when people wear a time-telling device on their wrist, they want something that’s an expression of who they are. That’s very reassuring for the watch business.”")

"""Similarly, the text file itself can be uploaded and initialized as shown below."""

from google.colab import files
files.upload()

a2=open("AAPL A1.txt", "r")
a2contents = a2.read()

article2 = TextBlob(a2contents)

"""In the set of code below, you will save the sentiment polarity and subjectivity into variables."""

a1p = a1.sentiment.polarity
a1s = a1.sentiment.subjectivity
print(a1p)
print(a1s)

"""In the set of code below, the *append* function is used to add values to a list-object. The "plist" stores values for sentiment polarity while "slist" stores those for sentiment subjectivity."""

plist.append(a1p)
slist.append(a1s)
print(plist)
print(slist)

"""Using this methodology above,  add the sentiment polarity/subjectivity scores for 20 articles into their resepctive lists. Print mean(plist) and mean(slist) to display the average sentiment polarity and subjectivity scores. Be sure to save these latter two values with a distinct reference variable. For the next part of this assignment, you will analyze the correlation between stock price for the dates of your article and the sentiment polarity/subjectivity scores. The code block below will provide a rough methodology to calculate a correlation coefficient using the numpy package and the *corrcoef* function. Note that the following code simply provides an example of the functions and methodology to achieve the objective. Your final lists will have 20 values each. Please remember to check the dates of your articles carefully and ensure you are retrieving the correct stock price to include as part of your data."""

import numpy as np
listpolarityscores = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]
listsubjectscores = [0.7, .6, .5, .4, .3, .2, .1]
liststockprice = [199.80, 199.74, 197.92, 201.55, 202.73, 204.41, 204.23]
stockpolaritycorr = np.corrcoef(liststockprice, listpolarityscores)
stocksubjectcorr = np.corrcoef(liststockprice, listsubjectscores)
print(stockpolaritycorr)
print(stocksubjectcorr)