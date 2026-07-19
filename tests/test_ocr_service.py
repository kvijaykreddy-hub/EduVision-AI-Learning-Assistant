"""
Test OCR Service.
"""

from PIL import Image

from eduvision_ai.services.ocr_service import OCRService


def main():

    image = Image.open("sample_images/sample_text.png")

    service = OCRService()

    response = service.extract_text(image)

    print("=" * 60)
    print("OCR RESULT")
    print("=" * 60)

    print(response.content)

    print("\nResponse Time:", response.response_time)
    print("Model:", response.model)


if __name__ == "__main__":
    main()