# Spot Bias

**Project Title**<br>
spotBias-Identifying Political Bias in News Article.<br>

**Motivation**<br>
The major reason we chose this issue was to determine the political bias in a news story. Certain media sources have a tendency to produce articles that support a political party's point of view or propaganda. As a result, they approach news items with a predetermined agenda. Because the general public is frequently unaware of a Media Outlet's preferences, they tend to believe them and the ideas/incidents mentioned in their publications. We believe that it is critical for the general public to know the truth (before forming an opinion), without succumbing to the bias of media outlets or bloggers' published articles.<br>

**Build Status**<br>
We have deployed spotBias-Web Application in our local server- Ubuntu.<br>

**Screenshots**<br>
![image](https://user-images.githubusercontent.com/41499024/163366303-6940e8b7-b589-4cf6-983e-90aab2102cb2.png)
![image](https://user-images.githubusercontent.com/41499024/163365256-199c0f0f-97d4-4140-abb1-b9546c110dfa.png)


**Framework**<br>
*Front End* HTML, CSS, Bootstrap <br>
*Back End* FLASK <br>
*News Catcher API* <br>
*Google News* "https://news.google.com/search?for=republic+world+political+news+india&hl=en-IN&gl=IN&ceid=IN%3Aen"
<br>
*Database Connectivity* SQLite3 <br><br>

**Features**<br>
1. Fetch News: 4 different News Articles will be fetched and their headings will be displayed. Users can select from any of the 4 headings and the selected news article will be displayed.
2. Predict Biasness: Our web application will identify if the selected news article is biased towards any political party (BJP, Congress and AAP) or not.
3. Database Connectivity: In our database we'll save the selected news article, predicted biasness and what user think to which political party it's biased.
<br><br>
**How it's implemented**<br>
1. The dataset was built using BeautifulSoup on News Catcher API and Google News.It currently consists of roughly 900 articles and respective annotations. The annotations represent the bias in the news articles. Link to the dataset: \href{https://docs.google.com/spreadsheets/d/17Kk9Rh93J4WtG3n_VBm1n8u7rpnklJ0h/edit?usp=sharing&ouid=103176303380619764050&rtpof=true&sd=true}{Dataset}.


