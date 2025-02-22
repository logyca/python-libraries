<p align="center">
  <a href="https://logyca.com/"><img src="https://logyca.com/sites/default/files/logyca.png" alt="Logyca"></a>
</p>
<p align="center">
    <em>LOGYCA public libraries</em>
</p>

<p align="center">
<a href="https://pypi.org/project/logyca-ai" target="_blank">
    <img src="https://img.shields.io/pypi/v/logyca-ai?color=orange&label=PyPI%20Package" alt="Package version">
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

# LOGYCA public libraries: To interact with ChatGPT and analyze documents, files and other functionality of the OpenAI library.

[Source code](https://github.com/logyca/python-libraries/tree/main/logyca-ai)
| [Package (PyPI)](https://pypi.org/project/logyca-ai/)
| [Samples](https://github.com/logyca/python-libraries/tree/main/logyca-ai/samples)


## To interact with the examples, keep the following in mind

FastAPI example. Through Swagger, you can:
- https://github.com/logyca/python-libraries/tree/main/logyca-ai/samples/fastapi_async
- Use the example endpoints to obtain the input schemas for the post method and interact with the available parameters.
- Endpoint publishing is asynchronous of openai SDK.
- The model currently used is ChatGPT-4o, no other models have been tested so far.
- Currently the formats supported to receive files and extract the text to interact with artificial intelligence are: txt, csv, pdf, images, Microsoft (docx, xlsx).

Script example. Through of code, you can:
- https://github.com/logyca/python-libraries/tree/main/logyca-ai/samples/script_app_sync
- Examples shared with the example written in FastAPI.
- The examples use synchronous functionality of openai SDK.
- The model used is ChatGPT-4o for testing.

## Environment variables documentation for example: fastapi_async

The examples are built in the Microsoft Azure OpenAI environment, and the variables to use are the following:

.env.sample
```console
# Environment variables documentation:

# API_KEY:
# The general API key used for authentication with services. This key is typically used for accessing cloud-based or other API-driven platforms. Replace '***' with the actual key.

# AZURE_OPENAI_DEPLOYMENT:
# The name or identifier of the OpenAI deployment within Azure. This defines the specific model version and configuration you are using in Azure OpenAI Service. Set this to the name of the deployed model, such as 'chatgpt3.5-turbo-1106'.

# AZURE_OPENAI_ENDPOINT:
# The base URL of the Azure OpenAI Service endpoint. This is the URL where API requests are sent, typically formatted like 'https://<your-endpoint>.openai.azure.com/'.

# AZURE_OPENAI_MODEL_NAME:
# The name of the specific OpenAI model being used in Azure, for example, 'gpt-35-turbo'. This identifies which model variant will be used for processing requests.

# AZURE_OPENAI_MODEL_VERSION:
# The version of the OpenAI model deployed in Azure. This typically reflects updates or optimizations to the model, such as '1106' to indicate a version from November 6th.

# OPENAI_API_KEY:
# The API key provided by OpenAI directly (not through Azure). This is used to authenticate and access OpenAI services outside of Azure.

# OPENAI_API_VERSION:
# The version of the OpenAI API being used. This specifies the version of the API and its capabilities, for example, '2023-03-15-preview'. It dictates the available features and request format.

API_KEY=***
AZURE_OPENAI_DEPLOYMENT=***
AZURE_OPENAI_ENDPOINT=***
AZURE_OPENAI_MODEL_NAME=***
AZURE_OPENAI_MODEL_VERSION=***
OPENAI_API_KEY=***
OPENAI_API_VERSION=***

# Example
# API_KEY=CUSTOM_ABC
# AZURE_OPENAI_DEPLOYMENT=chat4omni
# AZURE_OPENAI_ENDPOINT=azurenameforendpoint
# AZURE_OPENAI_MODEL_NAME=gpt-4o
# AZURE_OPENAI_MODEL_VERSION=2024-05-13
# OPENAI_API_KEY=AZURE_ABC
# OPENAI_API_VERSION=2024-07-01-preview
```
---

# OCR engine to extract images.

- Tesseract is an optical character recognition engine for various operating systems.
  It is free software, released under the Apache License. Originally developed by Hewlett-Packard as proprietary software in the 1980s,
  it was released as open source in 2005 and development was sponsored by Google in 2006

## Install

- (Source Code) https://tesseract-ocr.github.io/tessdoc/Downloads.html
- (Windows Binaries) https://github.com/UB-Mannheim/tesseract/wiki
- (Linux/Docker) apt-get -y install tesseract-ocr

# Example for simple conversation.

```json
{
  "system": "Voy a definirte tu personalidad, contexto y proposito.\nActua como un experto en venta de frutas.\nSe muy positivo.\nTrata a las personas de usted, nunca tutees sin importar como te escriban.",
  "messages": [
    {
      "additional_content": "",
      "type": "text",
      "user": "Dime 5 frutas amarillas"
    },
    {
      "assistant": "\n¡Claro! Aquí te van 5 frutas amarillas:\n\n1. Plátano\n2. Piña\n3. Mango\n4. Melón\n5. Papaya\n"
    },
    {
      "additional_content": "",
      "type": "text",
      "user": "Dame los nombres en ingles."
    }
  ]
}
```

---

# Example for image conversation.

## Using public published URL for image
```json
{
  "system": "Actua como una maquina lectora de imagenes.\nDevuelve la información sin lenguaje natural, sólo responde lo que se está solicitando.\nEl dispositivo que va a interactuar contigo es una api, y necesita la información sin markdown u otros caracteres especiales.",
  "messages": [
    {
      "additional_content": {
        "base64_content_or_url": "https://raw.githubusercontent.com/logyca/python-libraries/main/logyca-ai/logyca_ai/assets_for_examples/file_or_documents/image.png",
        "image_format": "image_url",
        "image_resolution": "auto"
      },
      "type": "image_url",
      "user": "Extrae el texto que recibas en la imagen y devuelvelo en formato json."
    }
  ]
}
```

## Using image content in base64
```json
{
  "system": "Actua como una maquina lectora de imagenes.\nDevuelve la información sin lenguaje natural, sólo responde lo que se está solicitando.\nEl dispositivo que va a interactuar contigo es una api, y necesita la información sin markdown u otros caracteres especiales.",
  "messages": [
    {
      "additional_content": {
        "base64_content_or_url": "<base64 image png content>",
        "image_format": "png",
        "image_resolution": "auto"
      },
      "type": "image_base64",
      "user": "Extrae el texto que recibas en la imagen y devuelvelo en formato json."
    }
  ]
}
```

---

# Example for pdf conversation.

## Using public published URL for pdf
```json
{
  "system": "No uses lenguaje natural para la respuesta.\nDame la información que puedas extraer de la imagen en formato JSON.\nSolo devuelve la información, no formatees con caracteres adicionales la respuesta.",
  "messages": [
    {
      "additional_content": {
        "base64_content_or_url": "https://raw.githubusercontent.com/logyca/python-libraries/main/logyca-ai/logyca_ai/assets_for_examples/file_or_documents/pdf.pdf",
        "pdf_format": "pdf_url"
      },
      "type": "pdf_url",
      "user": "Dame los siguientes datos: Expediente, radicación, Fecha, Numero de registro, Vigencia."
    }
  ]
}
```

## Using pdf content in base64
```json
{
  "system": "No uses lenguaje natural para la respuesta.\nDame la información que puedas extraer de la imagen en formato JSON.\nSolo devuelve la información, no formatees con caracteres adicionales la respuesta.",
  "messages": [
    {
      "additional_content": {
        "base64_content_or_url": "<base64 pdf content>",
        "pdf_format": "pdf"
      },
      "type": "pdf_base64",
      "user": "Dame los siguientes datos: Expediente, radicación, Fecha, Numero de registro, Vigencia."
    }
  ]
}
```

# Example for plain_text conversation.

## Using public published URL for plain_text
```json
{
  "system": "No uses lenguaje natural para la respuesta.\n                Dame la información que puedas extraer en formato JSON.\n                Solo devuelve la información, no formatees con caracteres adicionales la respuesta.\n                Te voy a enviar un texto que representa información en formato csv.",
  "messages": [
    {
      "additional_content": {
        "base64_content_or_url": "https://raw.githubusercontent.com/logyca/python-libraries/main/logyca-ai/logyca_ai/assets_for_examples/file_or_documents/plain_text.csv",
        "file_format": "plain_text_url"
      },
      "type": "plain_text_url",
      "user": "Dame los siguientes datos de la primera fila del documento: Expediente, radicación, Fecha, Numero de registro, Vigencia.\n                A partir de la fila 2 del documento, suma los valores de la columna Valores_A.\n                A partir de la fila 2 del documento, Suma los valores de la columna Valores_B."
    }
  ]
}
```

## Using plain_text content in base64
```json
{
  "system": "No uses lenguaje natural para la respuesta.\n                Dame la información que puedas extraer en formato JSON.\n                Solo devuelve la información, no formatees con caracteres adicionales la respuesta.\n                Te voy a enviar un texto que representa información en formato csv.",
  "messages": [
    {
      "additional_content": {
        "base64_content_or_url": "<base64 pdf content>",
        "file_format": "csv"
      },
      "type": "plain_text_base64",
      "user": "Dame los siguientes datos de la primera fila del documento: Expediente, radicación, Fecha, Numero de registro, Vigencia.\n                A partir de la fila 2 del documento, suma los valores de la columna Valores_A.\n                A partir de la fila 2 del documento, Suma los valores de la columna Valores_B."
    }
  ]
}
```

# Example for Microsoft files conversation (Word, Excel).

## Using public published URL for Excel file
```json
{
  "system": "No uses lenguaje natural para la respuesta.\n                Dame la información que puedas extraer de la imagen en formato JSON.\n                Solo devuelve la información, no formatees con caracteres adicionales la respuesta.",
  "messages": [
    {
      "additional_content": {
        "base64_content_or_url": "https://raw.githubusercontent.com/logyca/python-libraries/main/logyca-ai/logyca_ai/assets_for_examples/file_or_documents/ms_excel.xlsx",
        "file_format": "ms_url"
      },
      "type": "ms_url",
      "user": "Dame los siguientes datos: Expediente, radicación, Fecha, Numero de registro, Vigencia."
    }
  ]
}
```

## Using Excel file content in base64
```json
{
    "system": "No uses lenguaje natural para la respuesta.\n                Dame la información que puedas extraer de la imagen en formato JSON.\n                Solo devuelve la información, no formatees con caracteres adicionales la respuesta.",
    "messages": [
      {
        "additional_content": {
          "base64_content_or_url": "<base64 pdf content>",
          "file_format": "xlsx"
        },
        "type": "ms_base64",
        "user": "Dame los siguientes datos: Expediente, radicación, Fecha, Numero de registro, Vigencia."
      }
    ]
}
```


---

# Semantic Versioning

logyca_ai < MAJOR >.< MINOR >.< PATCH >

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

## [0.0.1aX] - 2024-08-02
### Added
- First tests using pypi.org in develop environment.

## [0.1.0] - 2024-08-02
### Added
- Completion of testing and launch into production.

## [0.1.1] - 2024-08-16
### Added
- The functions of extracting text from PDF files are refactored, using disk to optimize the use of ram memory and methods are added to extract text from images within the pages of the PDF files.

## [0.2.0] - 2024-08-30
### Added
- New feature of attaching documents with txt, csv, docx, xlsx extension

## [0.2.1] - 2024-09-16
### Added
- New tiktoken function to count tokens and check model capacity, returning if it meets the maximum_request_tokens requirements for both input and output.
### Fixed
- Extract excel files to output formats json, csv and list.

## [0.2.2] - 2024-10-22
### Added
- New functionalities are added to extract images from documents in base64 lists: extract_images_from_pdf_file, extract_images_from_docx_file
- The Swagger documentation is improved in the FastAPI example, adding the parameter: just_extract_images to the POST method to use the new document image extraction features.

## [0.2.3] - 2024-10-31
### Added
- new functionality when extracting text in Excel, you can select only extraction of visible sheets or all sheets.

## [0.2.4] - 2024-11-01
### Fixed
- Minimum adjustment when extracting images from an Excel file, leaving the extension in lowercase in the result.

## [0.2.5] - 2024-11-22
### Fixed
- __init__.py: Adjustment to which items will be available when the package is imported

## [0.2.6] - 2024-12-02
### Added
- Read pdf files from disk or ram memory

## [0.2.7,0.2.8] - 2024-12-18
### Fixed
- Improve prompt engineer for data extraction in Excel, specifying the JSON spreadsheet format used in data extraction.

## [0.2.9] - 2025-02-05
### Fixed
- When extracting images from PDF and Microsoft docx,xlsx documents, there are unsupported image formats such as WMF, these images are skipped.

## [0.2.10] - 2025-02-05
### Fixed
- Due to so many restrictions on the part of openai, due to the rate limits, a message is created to return the request http error status_code 429 for this reason.



