Using Amazon Web Services command line interface
================================================

python3 -m pip install awscli
python3 -m awscli configure  # Get key from IAM

https://docs.aws.amazon.com/cli/latest/reference/

#copy my-file.txt to the to the "data" directory located in my-s3-bucket 
aws s3 cp my-file.txt s3://my-s3-bucket/data/
 
#copy all files in my-data-dir into the "data" directory located in my-s3-bucket 
aws s3 cp my-data-dir/ s3://my-s3-bucket/data/ --recursive