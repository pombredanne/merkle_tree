# merkle_tree

`merkle_tree` is a command line program to calculate Merkle Tree hashes.
Internally, this is a ultra-thin wrapper for botocore's Merkle Tree implementation.
[botocore](https://github.com/boto/botocore) (low-level interface to AWS) itself uses it for
[Glacier API]( http://docs.aws.amazon.com/amazonglacier/latest/dev/checksum-calculations.html).

CLI to calculate Merkle Tree

## Getting Started

1. Install merkle_tree

    $ sudo pip install merkle_tree

2. Calculate hash

chunk size is 1MB and sha256 hash function is used.

    $ merkle filename
    3aef1c637ae8997d84b98f835c193556bca3892e4a6ec1e84dd3e664ecf125e1

If you want a binary hash:

    $ merkle --output binary filename | hexdump
    0000000 ef3a 631c e87a 7d99 b984 838f 195c 5635
    0000010 a3bc 2e89 6e4a e8c1 d34d 64e6 f1ec e125
    0000020 000a
    0000021


## Multi-part upload an archive to AWS Glacier


1. Create an archive to upload

    $ dd if=/dev/urandom of=FILENAME  bs=1024 count=2560 # 2560 = 1024 * 2.5

2. Initiate multipart upload

    $ BLOCK_SIZE=1048576 # 1048576 = 1MB
    $ aws glacier initiate-multipart-upload --account-id - --vault-name $VAULT_NAME --part-size $BLOCK_SIZE

upload_id is returned.

3. split an archive into pieces

    $ split -b $BLOCK_SIZE -d FILENAME 
    $ ls -l
    total 5120
    -rw-rw-r-- 1 jsmith jsmith 2621440 Mar 27 00:52 FILENAME
    -rw-rw-r-- 1 jsmith jsmith 1048576 Mar 27 00:52 x00
    -rw-rw-r-- 1 jsmith jsmith 1048576 Mar 27 00:52 x01
    -rw-rw-r-- 1 jsmith jsmith  524288 Mar 27 00:52 x02

4. multipart upload to Glacier

    $ aws glacier upload-multipart-part --account-id - --vault-name $VAULT_NAME --upload-id $UPLOAD_ID --range 'bytes 0-1048575/*' --body x00
    $ aws glacier upload-multipart-part --account-id - --vault-name $VAULT_NAME --upload-id $UPLOAD_ID --range 'bytes 1048576-2097151/*' --body x01
    $ aws glacier upload-multipart-part --account-id - --vault-name $VAULT_NAME --upload-id $UPLOAD_ID --range 'bytes 2097152-2621439/*' --body x02

5. complete multipart upload

    $ CHECKSUM=`merkle $FILENAME`
    $ ARCHIVE_SIZE=`wc -c < FILENAME`
    $ aws glacier complete-multipart-upload --account-id - --vault-name $VAULT_NAME --upload-id $UPLOAD_ID --archive-size $ARCHIVE_SIZE --checksum $CHECKSUM

