import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket = "s3-cloud-final-2025-upeu"
    key = "archivo.txt"

    response = s3.get_object(Bucket=bucket, Key=key)
    content = response['Body'].read().decode('utf-8')

    return {
        'statusCode': 200,
        'body': {
            'archivo_contenido': content
        }
    }
