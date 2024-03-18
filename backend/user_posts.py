import boto3
import uuid
from cognito_auth import (
    authorize_request,
    authorize_request_undecorated,
    get_user_sub
)
from boilerplate_responses import (
    request_not_authorized_response, success_response
)
import os
import json

dynamodb = boto3.resource('dynamodb')

TABLE_NAME = os.environ['DYNAMODB_TABLE']
table = dynamodb.Table(TABLE_NAME)


# Alternatively, you can use the decorator:
# @authorize_request(['user'])
def create(event, context):
    print(event)
    if not authorize_request_undecorated(event, ['user']):
        return request_not_authorized_response()
    post_data = json.loads(event['body'])
    post_id = str(uuid.uuid4())
    item = {
        'pk': f'USER#{get_user_sub(event)}',
        'sk': f'POST#{post_id}',
        'postData': post_data,
        'userId': get_user_sub(event),
        'postId': post_id,
    }
    table.put_item(
        Item=item
    )
    return success_response(item)


@authorize_request(['user'])
def get_all(event, context):
    try:
        # Scan ddb table for all items
        items = table.scan(
            FilterExpression='begins_with(sk, :sk)',
            ExpressionAttributeValues={
                ':sk': 'POST#'
            }
        )['Items']
        return success_response(items)
    except KeyError:
        return success_response({})


@authorize_request(['admin'])
def delete(event, context):
    # Load the id from the url path
    user_id = event['pathParameters']['userId']
    post_id = event['pathParameters']['postId']
    # Delete the item from the table
    table.delete_item(
        Key={
            'pk': f'USER#{user_id}',
            'sk': f'POST#{post_id}'
        }
    )
    return success_response({"message": "Post deleted successfully"})
