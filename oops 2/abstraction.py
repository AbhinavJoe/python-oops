"""
Abstraction Challenge — Cloud Storage Service

Scenario:
You’re designing a system that can store and retrieve files from different cloud providers (AWS S3, Google Cloud Storage, Azure Blob Storage).

We don’t want the main application code to care which provider is being used — it should only depend on an abstract interface for storage.

Requirements:

- Create an abstract base class CloudStorage that defines:

- upload_file(file_path: str, destination: str) -> str

- download_file(file_id: str, destination: str) -> bool

- delete_file(file_id: str) -> bool

Implement three concrete classes:

- S3Storage

- GCPStorage

- AzureStorage

- Each class should simulate its own storage behavior (no need to actually connect to AWS/GCP/Azure — just print messages with unique formatting).

- Write a FileManager class that takes a CloudStorage instance in its constructor and uses it to perform file operations without knowing the actual type.

Demonstrate usage by:

- Switching between S3, GCP, and Azure at runtime.

- Calling the same FileManager methods and getting provider-specific outputs.

Example Output:

[S3] Uploading report.pdf to bucket 'reports'...
[S3] File uploaded successfully with ID: S3_123
[GCP] Uploading report.pdf to bucket 'reports'...
[GCP] File uploaded successfully with ID: GCP_456
[Azure] Uploading report.pdf to container 'reports'...
[Azure] File uploaded successfully with ID: AZURE_789


What this tests you on:

- Designing abstract base classes with method contracts.

- Making the main logic provider-agnostic.

- Understanding why abstraction is key for interchangeable implementations.

- Setting up for Dependency Inversion in the future.
"""
