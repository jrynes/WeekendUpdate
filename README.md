# Weekend Update
Example repo to demonstrate how [AWS Lambda](https://aws.amazon.com/lambda/) and [AWS Simple Email Service (SES)](https://aws.amazon.com/ses/) can be used to scrape web information, and compile and send an HTML-formatted email

****

## Technologies Used in This Demo

|                      Technology Used                      |     Badge     | Purpose                                                                                                                                                                                                  |
|:---------------------------------------------------------:|:-------------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|    [Amazon Web Service (AWS)](https://aws.amazon.com/)    |      ![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)    | Used to run [AWS Lambda](https://aws.amazon.com/lambda/) to execute our serverless function, and [AWS Simple Email Service (SES)](https://aws.amazon.com/ses/) to send an email from our Lambda function |
|             [Docker](https://www.docker.com/)             |       ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)   | Containerization platform used with AWS to simplify debugging, versioning issues, and deploying a Python script that uses Selenium and Chrome                                                            |
|             [Python](https://www.python.org/)             |       ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)    | Primary programming language used in this example                                                                                                                                                        |
| [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) |       ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)    | Secondary programming language used with CSS to format the email update                                                                                                                                  |
|  [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)  |       ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)    | Secondary programming language used with HTML to format the email update                                                                                                                                 |
|           [Selenium](https://www.selenium.dev/)           |       ![Selenium](https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white)    | Used with Python to automate web browsing and scraping                                                                                                                                                   |
|        [Google Chrome](https://www.selenium.dev/)         |       ![Google Chrome](https://img.shields.io/badge/Google%20Chrome-4285F4?style=for-the-badge&logo=GoogleChrome&logoColor=white)    | Web browser used with Selenium in a headless state to automate web browsing                                                                                                                              |
|            [Gmail](https://gmail.google.com/)             |       ![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)    | Email client used to send mail with AWS Simple Email Service (SES) - While Gmail is used for this example, other email clients can be used                                                               |

## Function Diagram

![Function Diagram](Resources/Diagrams-01.jpg)










