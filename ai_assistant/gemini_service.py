import json

from google import genai
from django.conf import settings


# =========================================================
# GEMINI CLIENT
# =========================================================

client = genai.Client(
    api_key=settings.GEMINI_API_KEY
)


# =========================================================
# GENERIC GEMINI RESPONSE
# =========================================================

def generate_ai_response(prompt):

    try:

        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=prompt
        )

        return response.text

    except Exception as e:

        return f"Gemini Error: {str(e)}"


# =========================================================
# CHARGING INSIGHT
# =========================================================

def generate_charging_insight(user_data):

    prompt = f"""
You are an AI assistant for ChargeHub,
an EV Charging Management System.

Analyze the following user's EV charging information
and provide short, practical and personalized insights.

USER DATA:

Vehicle:
{user_data.get("vehicle")}

Battery Capacity:
{user_data.get("battery_capacity")} kWh

Current Battery:
{user_data.get("current_battery")}%

Total Bookings:
{user_data.get("total_bookings")}

Completed Charging Sessions:
{user_data.get("charging_sessions")}

Average Charging Cost:
₹{user_data.get("average_cost")}


YOUR TASK:

Generate:

1. Recommended Charging
2. Battery Insight
3. Cost Insight
4. Green Insight
5. Overall AI Summary


IMPORTANT RULES:

- Return ONLY valid JSON.
- Do NOT use markdown.
- Do NOT use ```json.
- Do NOT add any explanation before or after the JSON.
- Keep every insight concise.
- Keep the overall summary to 2-3 sentences.
- Do not invent electricity prices.
- Do not invent unavailable user data.
- If cost information is unavailable, clearly say so.
- Base recommendations only on the provided data.


RETURN EXACTLY THIS JSON STRUCTURE:

{{
    "recommended_charging": "Short personalized charging recommendation.",
    "battery_insight": "Short battery health or charging advice.",
    "cost_insight": "Short cost-saving recommendation.",
    "green_insight": "Short environmental or green charging recommendation.",
    "overall_summary": "A short 2-3 sentence personalized summary of the user's current EV charging situation."
}}
"""

    try:

        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=prompt
        )

        response_text = response.text.strip()


        # -------------------------------------------------
        # REMOVE MARKDOWN CODE BLOCK
        # -------------------------------------------------

        if response_text.startswith("```json"):

            response_text = response_text[7:].strip()

        elif response_text.startswith("```"):

            response_text = response_text[3:].strip()


        if response_text.endswith("```"):

            response_text = response_text[:-3].strip()


        # -------------------------------------------------
        # CONVERT JSON TO PYTHON DICTIONARY
        # -------------------------------------------------

        insight = json.loads(response_text)


        # -------------------------------------------------
        # RETURN ALL AI INSIGHTS
        # -------------------------------------------------

        return {

            "recommended_charging":
                insight.get(
                    "recommended_charging",
                    "No charging recommendation available."
                ),

            "battery_insight":
                insight.get(
                    "battery_insight",
                    "No battery insight available."
                ),

            "cost_insight":
                insight.get(
                    "cost_insight",
                    "No cost insight available."
                ),

            "green_insight":
                insight.get(
                    "green_insight",
                    "No green charging insight available."
                ),

            "overall_summary":
                insight.get(
                    "overall_summary",
                    "No overall AI summary available."
                ),
        }


    except json.JSONDecodeError:

        return {

            "recommended_charging":
                "Unable to process the charging recommendation.",

            "battery_insight":
                "Unable to process the battery insight.",

            "cost_insight":
                "Unable to process the cost insight.",

            "green_insight":
                "Unable to process the green charging insight.",

            "overall_summary":
                "Unable to generate the overall AI summary.",
        }


    except Exception as e:

        return {

            "recommended_charging":
                "Unable to generate charging recommendation.",

            "battery_insight":
                "Unable to generate battery insight.",

            "cost_insight":
                "Unable to generate cost insight.",

            "green_insight":
                "Unable to generate green insight.",

            "overall_summary":
                "Unable to generate the overall AI summary.",

            "error":
                str(e),
        }