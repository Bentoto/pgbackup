

def local(infile, outfile):
    outfile.write(infile.read())
    outfile.close()
    infile.close()


def upload_to_s3(client, infile, bucket, name):
    client.upload_fileobj(infile, bucket, name)