# import smtplib
# from google.cloud import secretmanager

# def send_email(request):
#     # Access secrets from Google Secret Manager
#     client = secretmanager.SecretManagerServiceClient()
#     email_secret_name = "projects/midproject-438621/secrets/EMAIL_SECRET/versions/latest"
#     password_secret_name = "projects/midproject-438621/secrets/PASSWORD_SECRET/versions/latest"

#     email = client.access_secret_version(request={"name": email_secret_name}).payload.data.decode("UTF-8")
#     password = client.access_secret_version(request={"name": password_secret_name}).payload.data.decode("UTF-8")

#     # Set up email content
#     message = f'Subject: Task Added\n\nA new task has been added to your to-do list.'
#     to_email = 'asifjahish2022@gmail.com'  # Replace with your email

#     # Send the email using SMTP
#     with smtplib.SMTP('smtp.gmail.com', 587) as server:
#         server.starttls()
#         server.login(email, password)
#         server.sendmail(email, to_email, message)

#     return 'Email sent', 200



import smtplib
from google.cloud import secretmanager
from flask import jsonify

def send_email(request):
    # Access secrets from Google Secret Manager
    client = secretmanager.SecretManagerServiceClient()
    email_secret_name = "projects/midproject-438621/secrets/EMAIL_SECRET/versions/latest"
    password_secret_name = "projects/midproject-438621/secrets/PASSWORD_SECRET/versions/latest"

    email = client.access_secret_version(request={"name": email_secret_name}).payload.data.decode("UTF-8")
    password = client.access_secret_version(request={"name": password_secret_name}).payload.data.decode("UTF-8")

    # Get data from request
    request_json = request.get_json(silent=True)
    item_name = request_json.get('item_name', 'New Task')  # Default value if not provided
    item_description = request_json.get('item_description', 'No Description')  # Default value if not provided
    to_email = request_json.get('to_email', 'asifjahish2022@gmail.com')  # Replace with your email

    # Set up email content
    message = f'Subject: Task Added\n\nA new task has been added to your to-do list:\n\nName: {item_name}\nDescription: {item_description}'

    try:
        # Send the email using SMTP
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(email, password)
            server.sendmail(email, to_email, message)

        return jsonify({'status': 'success', 'message': 'Email sent'}), 200

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

