import boto3
import os

aws_access_key_id = "tu_clave"
aws_secret_access_key = "tu_clave"
region_name = "us-east-1"
bucket_name = "s3-cloud-final-2025-upeu"
archivo_local = os.path.join(os.path.dirname(__file__), "..", "aws_proyecto", "archivo.txt")

nombre = "Hola Mark Pino"

s3 = boto3.client(
    's3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name
)

try:
    s3.download_file(bucket_name, "archivo.txt", archivo_local)
    print("📥 Se descargó archivo.txt existente desde S3.")
except Exception as e:
    print("⚠️ No se encontró archivo.txt en S3, se creará uno nuevo.")

with open(archivo_local, "a") as f:
    f.write(f"{nombre}\n")

print(f"✍️ Se añadió: {nombre}")

try:
    s3.upload_file(archivo_local, bucket_name, "archivo.txt")
    print(f"🚀 Archivo actualizado subido a S3 → {bucket_name}/archivo.txt")
except Exception as e:
    print("❌ Error al subir el archivo:", str(e))
