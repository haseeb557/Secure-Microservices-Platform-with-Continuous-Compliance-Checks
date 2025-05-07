import boto3

def detect_admin_iam_users():
    region = 'us-east-1'
    iam = boto3.client('iam')
    users = iam.list_users()

    for user in users['Users']:
        username = user['UserName']
        attached = iam.list_attached_user_policies(UserName=username)
        
        for policy in attached['AttachedPolicies']:
            if policy['PolicyName'] == 'AdministratorAccess':
                print(f"⚠️ User {username} has AdministratorAccess policy attached.")

        # Check for risky inline policies
        inline_policies = iam.list_user_policies(UserName=username)
        for policy_name in inline_policies['PolicyNames']:
            policy = iam.get_user_policy(UserName=username, PolicyName=policy_name)
            for stmt in policy['PolicyDocument']['Statement']:
                if stmt['Effect'] == 'Allow' and stmt['Action'] == '*':
                    print(f"⚠️ User {username} has an inline policy allowing all actions.")

if __name__ == "__main__":
    detect_admin_iam_users()
