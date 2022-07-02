from typing import final
import boto3
from botocore.exceptions import ClientError

# Replace sender@example.com with your "From" address.
# This address must be verified with Amazon SES.
SENDER = "Harikrishnan <harikrish.narasiman@gmail.com>"

# Replace recipient@example.com with a "To" address. If your account 
# is still in the sandbox, this address must be verified.
RECIPIENT = ["neuropac.hari@gmail.com","manjula.isha1@gmail.com"]

# Specify a configuration set. If you do not want to use a configuration
# set, comment the following variable, and the 
# ConfigurationSetName=CONFIGURATION_SET argument below.
# CONFIGURATION_SET = "ConfigSet"

# If necessary, replace us-west-2 with the AWS Region you're using for Amazon SES.
AWS_REGION = "us-east-1"

# The subject line for the email.
SUBJECT = "What to cook for Next Week?"

# The email body for recipients with non-HTML email clients.
BODY_TEXT = ("What to cook for Next Week?\r\n"
             "by FoodPlanner"
            )
            
# The HTML body of the email.  
      

# The character encoding for the email.
CHARSET = "UTF-8"

# Create a new SES resource and specify a region.
client = boto3.client('ses',region_name=AWS_REGION)


def send_email(final_schedule):
# Try to send the email.
    schedule_paragraph = ""
    for day in final_schedule:
        schedule_paragraph += f"""
        <b>{day}</b><br>\n
        Main Dish: {final_schedule[day]['mainDish']}<br> \n
        Side Dish: {final_schedule[day]['sideDish']}<br>\n
        Ingredients Needed: {final_schedule[day]['ingredientsNeeded']}<br> \n
        \n\n<br><br>
        """
    print(schedule_paragraph)
    BODY_HTML = f"""<html>
<head></head>
<body>
  <h1>What to Cook This Week?</h1>
  <p>
    {schedule_paragraph}
  </p>
</body>
</html>
            """    
    try:
        #Provide the contents of the email.
        response = client.send_email(
            Destination={
                'ToAddresses':
                    RECIPIENT,
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': CHARSET,
                        'Data': BODY_HTML,
                    },
                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER,
            # If you are not using a configuration set, comment or delete the
            # following line
            # ConfigurationSetName=CONFIGURATION_SET,
        )
    # Display an error if something goes wrong.	
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])