<p align="center">
  <a href="https://logyca.com/"><img src="https://logyca.com/sites/default/files/logyca.png" alt="Logyca"></a>
</p>
<p align="center">
    <em>LOGYCA public libraries</em>
</p>

<p align="center">
<a href="https://pypi.org/project/logyca-azure-storage-blob" target="_blank">
    <img src="https://img.shields.io/pypi/v/logyca-azure-storage-blob?color=orange&label=PyPI%20Package" alt="Package version">
</a>
<a href="(https://www.python.org" target="_blank">
    <img src="https://img.shields.io/badge/Python-%5B%3E%3D3.8%2C%3C%3D3.11%5D-orange" alt="Python">
</a>
</p>


---

# About us

* <a href="http://logyca.com" target="_blank">LOGYCA Company</a>
* <a href="https://www.youtube.com/channel/UCzcJtxfScoAtwFbxaLNnEtA" target="_blank">LOGYCA Youtube Channel</a>
* <a href="https://www.linkedin.com/company/logyca" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Linkedin"></a>
* <a href="https://twitter.com/LOGYCA_Org" target="_blank"><img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white" alt="Twitter"></a>
* <a href="https://www.facebook.com/OrganizacionLOGYCA/" target="_blank"><img src="https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white" alt="Facebook"></a>

---

# LOGYCA public libraries: To interact with the blob container files in your Azure Storage account.

[Source code](https://github.com/logyca/python-libraries/tree/main/logyca-azure-storage-blob)
| [Package (PyPI)](https://pypi.org/project/logyca-azure-storage-blob/)
| [Samples](https://github.com/logyca/python-libraries/tree/main/logyca-azure-storage-blob/samples)

---

To install the libraries

```Python
# Check SQLAlchemy dependency that is installed
pip install logyca_azure_storage_blob
```


# How azcopy performs file consistency validation

Like azcopy, Microsoft's client for uploading large files to Blob, the md5 hash must be computed locally and uploaded to the blob properties along with the file, the blob service will commit this at the end of the process, returning an error if presents inconsistency in value.

## Calculates the MD5 hash of the file content and saves it as the Content-MD5 property of the blob:


```console
azcopy --put-md5 #
```

References:

    - https://learn.microsoft.com/en-us/azure/storage/common/storage-ref-azcopy-copy

This library uses the concepts of the azcopy client for its implementation.

---

# Test upload

bandwith movistar: upload/download: 300 mbps

## Test 1, function: container_blob_upload_staging_blocks_commit with console output

    file: 20240126084440-backup.dump
    size: 2.03 GB
    parameters: 
        - self.__chunk_size_bytes=4*1024*1024 # Defaults 4 MiB
    Elapsed time: 00:05:22
    Output:
        Upload process: file_to_upload[20240126084440-backup.dump], Chunks[42/522], Percentage[8.05%]
        Upload process: file_to_upload[20240126084440-backup.dump], Chunks[43/522], Percentage[8.24%]
        Upload process: file_to_upload[20240126084440-backup.dump], Chunks[44/522], Percentage[8.43%]
        Upload process: file_to_upload[20240126084440-backup.dump], Chunks[45/522], Percentage[8.62%]
        Upload process: file_to_upload[20240126084440-backup.dump], Chunks[46/522], Percentage[8.81%]
        Upload process: file_to_upload[20240126084440-backup.dump], Chunks[47/522], Percentage[9.00%]
        ...
        ...
        ...
        Upload process: file_to_upload[20240126084440-backup.dump], Chunks[517/522], Percentage[99.04%]
        Upload process: file_to_upload[20240126084440-backup.dump], Chunks[518/522], Percentage[99.23%]
        Upload process: file_to_upload[20240126084440-backup.dump], Chunks[519/522], Percentage[99.43%]
        Upload process: file_to_upload[20240126084440-backup.dump], Chunks[520/522], Percentage[99.62%]
        Upload process: file_to_upload[20240126084440-backup.dump], Chunks[521/522], Percentage[99.81%]
        Upload process: file_to_upload[20240126084440-backup.dump], Chunks[522/522], Percentage[100.00%]

## Test 2, function: container_blob_upload_data_transfer_options no console output
    file: 20240126084440-backup.dump
    size: 2.03 GB        
    parameters:
        - self.__chunk_size_bytes=4*1024*1024 # 4 MiB
        - self.__max_single_put_size=8*1024*1024 # 8 MiB.
        - max_concurrency=1
    Elapsed time: 00:11:19
    Unsupported formats: ---
    Output: Not available

## Test 3, function: container_blob_upload_data_transfer_options no console output
    file: 20240126084440-backup.dump
    size: 2.03 GB        
    parameters:
        - self.__chunk_size_bytes=4*1024*1024 # 4 MiB
        - self.__max_single_put_size=8*1024*1024 # 8 MiB.
        - max_concurrency=2
    Elapsed time: 00:03:50
    Unsupported formats: ---
    Output: Not available

## Test 4, function: container_blob_upload_data_transfer_options no console output
    file: 20240126084440-backup.dump
    size: 2.03 GB        
    parameters:
        - self.__chunk_size_bytes=4*1024*1024 # 4 MiB
        - self.__max_single_put_size=8*1024*1024 # 8 MiB.
        - max_concurrency=3
    Elapsed time: 00:03:38
    Unsupported formats: ---
    Output: Not available

---

# Semantic Versioning

logyca_azure_storage_blob < MAJOR >.< MINOR >.< PATCH >

* **MAJOR**: version when you make incompatible API changes
* **MINOR**: version when you add functionality in a backwards compatible manner
* **PATCH**: version when you make backwards compatible bug fixes

## Definitions for releasing versions
* https://peps.python.org/pep-0440/

    - X.YaN (Alpha release): Identify and fix early-stage bugs. Not suitable for production use.
    - X.YbN (Beta release): Stabilize and refine features. Address reported bugs. Prepare for official release.
    - X.YrcN (Release candidate): Final version before official release. Assumes all major features are complete and stable. Recommended for testing in non-critical environments.
    - X.Y (Final release/Stable/Production): Completed, stable version ready for use in production. Full release for public use.

---

# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Types of changes

- Added for new features.
- Changed for changes in existing functionality.
- Deprecated for soon-to-be removed features.
- Removed for now removed features.
- Fixed for any bug fixes.
- Security in case of vulnerabilities.

## [0.0.1rc1] - 2024-05-24
### Added
- First tests using pypi.org in develop environment.

## [0.1.0] - 2024-05-24
### Added
- Completion of testing and launch into production.

## [0.1.2] - 2024-07-18
### Changed
- Two filter sa container blob list are added. modified hours ago to return modified blobs after x hours and include_subfolders to return only blobs from the received folder list.

