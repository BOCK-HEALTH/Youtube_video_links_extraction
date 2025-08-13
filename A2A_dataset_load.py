import boto3
          # ---------- CONFIG ----------
          MAIN_BUCKET = 'eira1-general-dataset'    
          SUB_BUCKET = 'eira1-a2a-ds'        
          PREFIX = 'audio/'
          REGION = 'ap-south-1'
          # ----------------------------

          def copy_updated_files():
              s3 = boto3.resource("s3", region_name=REGION)

              src_bucket = s3.Bucket(MAIN_BUCKET)
              dest_bucket = s3.Bucket(SUB_BUCKET)

              print(f"Starting copy from '{MAIN_BUCKET}' to '{SUB_BUCKET}'...")

              for obj in src_bucket.objects.filter(Prefix=PREFIX):
                  src_key = obj.key
                  copy_source = {'Bucket': MAIN_BUCKET, 'Key': src_key}

                  # Copy the file (will overwrite if exists)
                  dest_bucket.Object(src_key).copy(copy_source)
                  print(f"✅ Copied/Updated: {src_key}")

              print("🎯 Copy process completed.")

          if __name__ == "__main__":
              copy_updated_files()
