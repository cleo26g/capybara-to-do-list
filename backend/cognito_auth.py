from functools import wraps
from boilerplate_responses import request_not_authorized_response


def get_user_sub(event):
    return event['requestContext']['authorizer']['jwt']['claims']['sub']


def parsed_groups(groups: str) -> list:
    parsed_groups = groups[1:-1].split(' ')
    return parsed_groups


def authorize_request_undecorated(event, required_groups: list):
    try:
        claims = event['requestContext']['authorizer']['jwt']['claims']
        groups_present = parsed_groups(claims['cognito:groups'])
        if set(required_groups).issubset(groups_present):
            return True
    except KeyError:
        return False
    return False


def authorize_request(required_groups: list):
    def groups_required(func):
        @wraps(func)
        def wrapper(event, context):
            try:
                claims = event['requestContext']['authorizer']['jwt']['claims']
                groups_present = parsed_groups(claims['cognito:groups'])
                if not set(required_groups).issubset(groups_present):
                    print('Required group not present')
                    return request_not_authorized_response()
            except KeyError:
                return request_not_authorized_response()
            return func(event, context)
        return wrapper
    return groups_required
