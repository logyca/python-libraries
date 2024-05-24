# Checksum – File Integrity Verification

Like azcopy, Microsoft's client for uploading large files to Blob, the md5 hash must be computed locally and uploaded to the blob properties along with the file, the blob service will commit this at the end of the process, returning an error if presents inconsistency in value.

## Calculates the MD5 hash of the file content and saves it as the Content-MD5 property of the blob:


```console
azcopy --put-md5 #
```

References:

    - https://learn.microsoft.com/en-us/azure/storage/common/storage-ref-azcopy-copy

# Test upload

bandwith movistar: upload/download: 300 mbps

## Test 1, function: container_blob_upload_staging_blocks_commit

    file: 20240126084440-backup-gs1codes1.dump
    size: 2.03 GB
    parameters: 
        - self.__chunk_size_bytes=4*1024*1024 # Defaults 4 MiB
    Elapsed time: 00:05:22
    Formats that failed (InvalidBlobOrBlock):
        - Formats: mp4, backup
    Output:
        Upload process: file_to_upload[20240126084440-backup-gs1codes1.dump], Chunks[42/522], Percentage[8.05%]
        Upload process: file_to_upload[20240126084440-backup-gs1codes1.dump], Chunks[43/522], Percentage[8.24%]
        Upload process: file_to_upload[20240126084440-backup-gs1codes1.dump], Chunks[44/522], Percentage[8.43%]
        Upload process: file_to_upload[20240126084440-backup-gs1codes1.dump], Chunks[45/522], Percentage[8.62%]
        Upload process: file_to_upload[20240126084440-backup-gs1codes1.dump], Chunks[46/522], Percentage[8.81%]
        Upload process: file_to_upload[20240126084440-backup-gs1codes1.dump], Chunks[47/522], Percentage[9.00%]
        ...
        ...
        ...
        Upload process: file_to_upload[20240126084440-backup-gs1codes1.dump], Chunks[517/522], Percentage[99.04%]
        Upload process: file_to_upload[20240126084440-backup-gs1codes1.dump], Chunks[518/522], Percentage[99.23%]
        Upload process: file_to_upload[20240126084440-backup-gs1codes1.dump], Chunks[519/522], Percentage[99.43%]
        Upload process: file_to_upload[20240126084440-backup-gs1codes1.dump], Chunks[520/522], Percentage[99.62%]
        Upload process: file_to_upload[20240126084440-backup-gs1codes1.dump], Chunks[521/522], Percentage[99.81%]
        Upload process: file_to_upload[20240126084440-backup-gs1codes1.dump], Chunks[522/522], Percentage[100.00%]

## Test 2, function: container_blob_upload_data_transfer_options
    file: 20240126084440-backup-gs1codes1.dump
    size: 2.03 GB        
    parameters:
        - self.__chunk_size_bytes=4*1024*1024 # 4 MiB
        - self.__max_single_put_size=8*1024*1024 # 8 MiB.
        - max_concurrency=1
    Elapsed time: 00:11:19
    Unsupported formats: ---
    Output: Not available

## Test 3, function: container_blob_upload_data_transfer_options
    file: 20240126084440-backup-gs1codes1.dump
    size: 2.03 GB        
    parameters:
        - self.__chunk_size_bytes=4*1024*1024 # 4 MiB
        - self.__max_single_put_size=8*1024*1024 # 8 MiB.
        - max_concurrency=2
    Elapsed time: 00:03:50
    Unsupported formats: ---
    Output: Not available

## Test 3, function: container_blob_upload_data_transfer_options
    file: 20240126084440-backup-gs1codes1.dump
    size: 2.03 GB        
    parameters:
        - self.__chunk_size_bytes=4*1024*1024 # 4 MiB
        - self.__max_single_put_size=8*1024*1024 # 8 MiB.
        - max_concurrency=3
    Elapsed time: 00:03:38
    Unsupported formats: ---
    Output: Not available

