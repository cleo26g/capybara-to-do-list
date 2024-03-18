import boto3


client = boto3.client('cognito-idp')


def handler(event, context):
    print(event)
    user_pool_id = event['userPoolId']
    user_email = event['request']['userAttributes']['email']
    client.admin_add_user_to_group(
        UserPoolId=user_pool_id,
        Username=user_email,
        GroupName='user'
    )
    print(f'User {user_email} added to group "user"')
    return event
