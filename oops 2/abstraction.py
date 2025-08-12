# MARK: Q-1
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

from abc import ABC, abstractmethod


class CloudStorage(ABC):
    @abstractmethod
    def upload_file(self, file_path: str, destination: str) -> str:
        pass

    @abstractmethod
    def download_file(self, file_id: str, destination: str) -> bool:
        pass

    @abstractmethod
    def delete_file(self, file_id: str) -> bool:
        pass


class S3Storage(CloudStorage):
    def upload_file(self, file_path: str, destination: str) -> str:
        print(f"[S3] Uploading {file_path} to bucket '{destination}'...")
        return "S3_123"

    def download_file(self, file_id: str, destination: str) -> bool:
        print(f"[S3] Downloading {file_id} to '{destination}'...")
        return True

    def delete_file(self, file_id: str) -> bool:
        print(f"[S3] Deleting file with ID {file_id} from Amazon S3...")
        return True


class GCPStorage(CloudStorage):
    def upload_file(self, file_path: str, destination: str) -> str:
        print(f"[GCP] Uploading {file_path} to bucket '{destination}'...")
        return "GCP_456"

    def download_file(self, file_id: str, destination: str) -> bool:
        print(f"[GCP] Downloading {file_id} to '{destination}'...")
        return True

    def delete_file(self, file_id: str) -> bool:
        print(f"[GCP] Deleting file with ID {file_id} from GCP Storage...")
        return True


class AzureStorage(CloudStorage):
    def upload_file(self, file_path: str, destination: str) -> str:
        print(f"[Azure] Uploading {file_path} to container '{destination}'...")
        return "AZURE_789"

    def download_file(self, file_id: str, destination: str) -> bool:
        print(f"[Azure] Downloading {file_id} to '{destination}'...")
        return True

    def delete_file(self, file_id: str) -> bool:
        print(
            f"[Azure] Deleting file with ID {file_id} from Azure Blob Storage...")
        return True
    
    def something(self):
        return True


class FileManager:
    def __init__(self, storage: CloudStorage):
        self.storage = storage

    def upload(self, file_path: str, destination: str) -> str:
        return self.storage.upload_file(file_path, destination)

    def download(self, file_id: str, destination: str) -> bool:
        return self.storage.download_file(file_id, destination)

    def delete(self, file_id: str) -> bool:
        return self.storage.delete_file(file_id)


providers = [S3Storage(), GCPStorage(), AzureStorage()]

for provider in providers:
    print("\n--- Using new provider ---")
    fm = FileManager(provider)
    file_id = fm.upload("report.pdf", "reports")
    fm.download(file_id, "downloads")
    fm.delete(file_id)


# MARK: Follow-up to Q-1

"""
Scenario — Multi-Provider Cloud Storage with Credentials & Provider Tools

We’re upgrading the system so that:

Shared state
    All cloud providers require:
    - provider_name (string)
    - region (string)
These should be stored in the abstract base class CloudStorage.

Provider-specific state
    Each concrete class should store its own credentials or settings:
     - S3Storage: access_key, secret_key
     - GCPStorage: service_account_json
     - AzureStorage: connection_string

Required abstract methods
    Same as before:
        upload_file(file_path: str, destination: str) -> str
        download_file(file_id: str, destination: str) -> bool
        delete_file(file_id: str) -> bool

Extra provider-only method (NOT in the abstract class)
 - S3Storage: list_bucket(bucket_name: str) — list files
 - GCPStorage: set_bucket_acl(bucket_name: str, acl: str) — change access control
 - AzureStorage: generate_sas_token(container_name: str) — generate temporary access token

FileManager class
 - Takes a CloudStorage instance in __init__
 - Uses only abstract methods for general operations.
 - If a provider-specific method exists, demonstrate how it could be accessed safely without breaking abstraction completely (hint: isinstance or duck typing).

Demo
 - Show how you can swap providers without changing FileManager code.
 - Also show how you can call a provider-only method only when the provider supports it.

Example expected flow:
    Using S3 in region ap-south-1
    [S3] Uploading invoice.pdf to 'invoices'
    [S3] Listing bucket contents for 'invoices'
    Using GCP in region us-central1
    [GCP] Uploading invoice.pdf to 'invoices'
    [GCP] Setting ACL 'public-read' on bucket 'invoices'
    Using Azure in region eastus
    [Azure] Uploading invoice.pdf to 'invoices'
    [Azure] Generating SAS token for container 'invoices'

What this tests:
 - Abstract base class with state (shared initialization).
 - Concrete class with extra state.
 - Mixing abstraction with provider-specific extensions.
 - Safe handling of extended behaviors.
 - OOP design trade-offs when you need to sometimes break strict abstraction for extra functionality.

If you solve this, you’ll be hitting:
 - Abstraction
 - Encapsulation (credentials hidden inside class)
 - Polymorphism (upload/download/delete interchangeable across providers)
 - Composition (FileManager has-a CloudStorage)
"""

