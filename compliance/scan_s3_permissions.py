import boto3

def scan_s3_permissions():
    s3 = boto3.client('s3')
    buckets = s3.list_buckets()

    for bucket in buckets['Buckets']:
        print(f"Checking bucket: {bucket['Name']}")  # Debug line
        acl = s3.get_bucket_acl(Bucket=bucket['Name'])
        for grant in acl['Grants']:
            if 'AllUsers' in grant.get('Grantee', {}).get('URI', ''):
                print(f"⚠️ Warning: S3 Bucket {bucket['Name']} has public access.")

if __name__ == "__main__":
    scan_s3_permissions()
