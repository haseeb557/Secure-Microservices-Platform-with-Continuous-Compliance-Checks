import boto3

def check_open_ports():
    region = 'us-east-1'
    client = boto3.client('ec2')
    security_groups = client.describe_security_groups()

    for sg in security_groups['SecurityGroups']:
        for permission in sg.get('IpPermissions', []):
            if permission['IpProtocol'] == 'tcp' and permission['FromPort'] in [22, 80]:
                print(f"Warning: Security Group {sg['GroupName']} has port {permission['FromPort']} open.")

if __name__ == "__main__":
    check_open_ports()
