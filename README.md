# Spot Bias

**Project Title**<br>
spotBias-Identifying Political Bias in News Article.<br>

**Motivation**<br>
The major reason we chose this issue was to determine the political bias in a news story. Certain media sources have a tendency to produce articles that support a political party's point of view or propaganda. As a result, they approach news items with a predetermined agenda. Because the general public is frequently unaware of a Media Outlet's preferences, they tend to believe them and the ideas/incidents mentioned in their publications. We believe that it is critical for the general public to know the truth (before forming an opinion), without succumbing to the bias of media outlets or bloggers' published articles.<br>

**Build Status**<br>
We have deployed spotBias-Web Application in our local server- Ubuntu.<br>

**Screenshots**<br>
![welcome_p![about](https://user-images.githubusercontent.com/41499024/165491717-353f3bee-5c97-4043-b311-fc0a3265166c.PNG)
age](https://user-ima![fetch_news](https://user-images.githubusercontent.com/41499024/165491753-9d0e4fdb-2ccb-4c5c-82ce-aea7a6e4cbd7.PNG)
ges.githubusercontent.com/41499024/165491689-e38b4bba-60f6-4759-a5d3-409643bff6ec.PNG)

*Database*
![image](https://drive.google.com/file/d/1BTRpItfW41ke1I4Oxn9f-hskFMiZU_KS/view?usp=sharing)


**Framework**<br>
*Front End* HTML, CSS, Bootstrap <br>
*Back End* FLASK <br>
*News Catcher API* <br>
*Google News* 
Republic News:"https://news.google.com/search?for=republic+world+political+news+india&hl=en-IN&gl=IN&ceid=IN%3Aen"
NDTV News:https://news.google.com/search?for=ndtv+political+news+india&hl=en-IN&gl=IN&ceid=IN%3Aen"

<br>
*Database Connectivity* SQLite3 <br><br>

**Features**<br>
1. Fetch News: 4 different News Articles will be fetched and their headings will be displayed. Users can select from any of the 4 headings and the selected news article will be displayed.
2. Predict Biasness: Our web application will identify if the selected news article is biased towards any political party (BJP, Congress and AAP) or not.
3. Database Connectivity: In our database we'll save the selected news article, predicted biasness and what user think to which political party it's biased.<br><br>

**How it's implemented**<br>
1. The dataset was built using BeautifulSoup on News Catcher API and Google News.It currently consists of roughly 900 articles and respective annotations. The annotations represent the bias in the news articles. Link to the dataset:{https://docs.google.com/spreadsheets/d/17Kk9Rh93J4WtG3n_VBm1n8u7rpnklJ0h/edit?usp=sharing&ouid=103176303380619764050&rtpof=true&sd=true}{Dataset}.
2. We preprocessed the dataset using NLP techniques: Conversion into lower case, StopWords removal and lemmatization.
3. In the preprocessed dataset, we applied two methods: With feature selection and without feature selection, and fed it into different classifier algorithms. Out of which Random Forest OneVsAll gives us the best result.
4. We develop the application using these tech/framework NewsCatcherAPI, HTML,CSS, Bootstrap, FLASK, SQLite3.

