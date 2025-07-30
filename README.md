# Daily news fetched from an API sent directly to the email
• This project fetches the latest news articles about a specific topic (e.g., "Tesla") using the NewsAPI and sends a daily email with the article titles, descriptions, and links. The script uses Python's requests library to retrieve news data and smtplib to securely send the email through Gmail's SMTP server. The email content is formatted in plain text with a single subject line and sent to a predefined recipient. This tool can be customized for any keyword or news topic, making it a useful automation for staying informed about subjects that matter to you.
<br><br>
• I also scheduled a task that sends an email with the current news everyday at 08:00 UTC using PythonAnywhere. What I did was the following:
<br><br>
<b>1. I loaded the scripts useful for fetching the information from the API and sending to the targeted email:</b>
<img width="1657" height="657" alt="1" src="https://github.com/user-attachments/assets/c3f5e5ef-bed9-4900-862e-83361c3c83a9" />
<br><b>2. I scheduled the task everyday @ 08:00 UTC:</b>
<img width="1537" height="312" alt="2" src="https://github.com/user-attachments/assets/41080e85-056e-495b-b8ef-dfe15eb18e0f" />
<br><b>3. And the mails that I receiva have the following format:</b>
<img width="1322" height="696" alt="3" src="https://github.com/user-attachments/assets/2a81ade5-a2ff-4729-b7f1-dfdf339126b2" />

