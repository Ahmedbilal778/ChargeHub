from django.core.management.base import BaseCommand

from ai_assistant.gemini_service import generate_ai_response


class Command(BaseCommand):

    help = "Test Gemini API connection"

    def handle(self, *args, **options):

        self.stdout.write(
            "Testing Gemini API..."
        )

        prompt = """
        You are an AI assistant for an EV Charging Management System.

        Give a short response explaining one useful tip
        for an EV owner about charging their vehicle.
        """

        response = generate_ai_response(
            prompt
        )

        self.stdout.write(
            "\nGemini Response:\n"
        )

        self.stdout.write(
            response
        )