# Import statements - Configure these to your needs
import json
import os
import time
# Import Selenium to help with web scraping
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Import urllib3 for REST API calls as needed
import urllib3
from datetime import datetime
# Import boto3 to work with AWS
import boto3
import logging
import botocore
# The statement below is imported to set our Chromedriver configuration
from tempfile import mkdtemp
# Import SMTP to send an email, instead of using AWS SES API which doesn't currently appear to work inside a lambda function
from email.utils import formataddr
from smtplib import SMTP_SSL, SMTPException
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#Below is our default Lambda function
def lambda_handler(event, context):
    """Sample pure Lambda function below, for reference only
    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format
        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format
    context: object, required
        Lambda Context runtime methods and attributes
        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html
    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict
        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    #Call function to scrape website
    webScrapingResults = scrapeWebsite(targetWebsite)

    #Set your own function here to parse your web scraping results to an HTML format
    emailHTML = buildHTML_Email(webScrapingResults)

    # Structure Email to send here
    senderEmail = "Replace this text with your sending email address"
    recipientEmail = {"ToAddresses": "Replace this text with your receiving email address"}
    emailSubject = "Weekend Update - Email Subject Line Here"
    emailTxt = "Replace this text here with the plantext version of your email"
    emailHTML = htmlCompiledFormat
    # === Code below to send an email using SMTP instead of the AWS SES API ===
    testEmailSend = sendEmail(emailTxt, emailHTML)

    return {
        "statusCode": 200,
    }

# Function to send an email via SMTP
def sendEmail(emailText, emailHTML):
    # Replace sender@example.com with your "From" address.
    # This address must be verified.
    SENDER = "sender@example.com"
    SENDERNAME = "sender_Name"

    # Replace recipient@example.com with a "To" address. If your account
    # is still in the sandbox, this address must be verified.
    RECIPIENT = "recipient@example.com"

    # Replace smtp_username with your Amazon SES SMTP user name.
    USERNAME_SMTP = "Replace smtp_username with your Amazon SES SMTP user name."

    # Replace smtp_password with your Amazon SES SMTP password.
    PASSWORD_SMTP = "Replace smtp_password with your Amazon SES SMTP password."

    # (Optional) the name of a configuration set to use for this message.
    # If you comment out this line, you also need to remove or comment out
    # the "X-SES-CONFIGURATION-SET:" header below.
    # CONFIGURATION_SET = "ConfigSet"

    # If you're using Amazon SES in an AWS Region other than US West (Oregon),
    # replace email-smtp.us-west-2.amazonaws.com with the Amazon SES SMTP
    # endpoint in the appropriate region.
    HOST = "email-smtp.us-west-2.amazonaws.com"
    # Email ports are typically 25, 465, 587, or 2525
    PORT = 587

    # The subject line of the email.
    SUBJECT = 'Weekend Update'

    # The email body for recipients with non-HTML email clients.
    BODY_TEXT = ("Amazon SES Test - SSL\r\n"
                 "This email was sent through the Amazon SES SMTP "
                 "Interface using the Python smtplib package." +
                 emailText)

    # The HTML body of the email.
    BODY_HTML = emailHTML

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = SUBJECT
    msg['From'] = formataddr((SENDERNAME, SENDER))
    msg['To'] = RECIPIENT
    # Comment or delete the next line if you are not using a configuration set
    # msg.add_header('X-SES-CONFIGURATION-SET',CONFIGURATION_SET)

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(BODY_TEXT, 'plain')
    part2 = MIMEText(BODY_HTML, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)

    # Try to send the message.
    try:
        with SMTP_SSL(HOST, PORT) as server:
            server.login(USERNAME_SMTP, PASSWORD_SMTP)
            server.sendmail(SENDER, RECIPIENT, msg.as_string())
            server.close()
            print("Email sent!")

    except SMTPException as e:
        print("Error: ", e)

# Function to scrape website
def scrapeWebsite(targetWebsite):

    # Using the reference settings from the repo linked below
    # https://github.com/umihico/docker-selenium-lambda/blob/main/main.py

    options = webdriver.ChromeOptions()
    options.binary_location = '/opt/chrome/chrome'
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1280x1696")
    options.add_argument("--single-process")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-dev-tools")
    options.add_argument("--no-zygote")
    options.add_argument(f"--user-data-dir={mkdtemp()}")
    options.add_argument(f"--data-path={mkdtemp()}")
    options.add_argument(f"--disk-cache-dir={mkdtemp()}")
    options.add_argument("--remote-debugging-port=9222")
    driver = webdriver.Chrome("/opt/chromedriver", options=options)

    # Basic debug function to check that Selenium is working
    driver.get("https://www.python.org")
    debugMessage = "Selenium is working: " + (driver.title)
    print(debugMessage)

# Function to build our HTML email
def buildHTML_Email(webScrapingResults):
    emailHeader = '<!DOCTYPE html>\
                    <html lang="en">\
                    <head>\
                        <meta charset="UTF-8">\
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">\
                        <title>Weekend Update</title>\
                        <style>\
                        u + .body .gmail-blend-screen { background:#000; mix-blend-mode:screen; }\
                        u + .body .gmail-blend-difference { background:#000; mix-blend-mode:difference; }\
                        table tr:nth-child(odd){ background-color: #cccccc; color: #000000; }\
                        table tr:nth-child(even){ background-color: #eeeeee; color: #000000; }\
                        .table_DescriptionColumn { text-align:left; }\
                        .table_NoLineBreak { white-space:nowrap; }\
                        .WeekendUpdateTitle { color: #303030; font-family: Arial, Helvetica, sans-serif; }\
                        </style>\
                    </head>'

    emailBody_Start = '<body class="body">\
                        <div style="background:#ebebeb; background-image:linear-gradient(#ebebeb,#ebebeb); color:#000000;">\
                            <div class="gmail-blend-screen">\
                                <div class="gmail-blend-difference">\
                                    <!-- Content starts here -->\
                                    <h3 class="WeekendUpdateTitle"> Weekend Update for: ' + datetime.today().strftime("%B %d, %Y") + '</h3>'


    emailBody_End = '<!-- Content ends here -->\
                    </div>\
                    </div>\
                    </div>'

    emailSectionDivider = '<br><br><br>'

    htmlOutput = emailHeader + emailBody_Start + webScrapingResults + emailBody_End

    return htmlOutput