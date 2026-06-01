def detect_indicators(text):

    text = text.lower()

    indicators = []

    payment_keywords = [

        "registration fee",
        "training fee",
        "processing fee",
        "joining fee",
        "joining amount",
        "security deposit",
        "application fee",
        "onboarding fee",

        "participation contribution",
        "training contribution",
        "onboarding contribution",
        "processing charges",
        "small contribution",
        "initial payment",
        "activation fee",
        "verification fee",
        "membership fee",
        "deposit required"
    ]


    contact_keywords = [

        "whatsapp",
        "telegram",
        "contact hr",
        "dm on telegram",
        "message hr",
        "send your details to",
        "email your details to",
        "contact recruitment manager"
    ]


    urgency_keywords = [

        "urgent hiring",
        "immediate joining",
        "limited seats",
        "apply immediately",
        "few positions remain",
        "confirm your slot",
        "high demand",
        "hurry up",
        "last few openings"
    ]


    if any(word in text for word in payment_keywords):
        indicators.append("payment_request")


    if any(word in text for word in contact_keywords):
        indicators.append("external_contact")


    if any(word in text for word in urgency_keywords):
        indicators.append("urgency_tactic")


    if "no interview" in text:
        indicators.append("no_interview")


    return indicators



def detect_patterns(indicators):

    patterns = []

    if "payment_request" in indicators and "external_contact" in indicators:
        patterns.append("Payment requested with external messaging")

    if "payment_request" in indicators and "urgency_tactic" in indicators:
        patterns.append("Payment requested with urgency tactic")

    if "external_contact" in indicators and "urgency_tactic" in indicators:
        patterns.append("External messaging combined with urgency tactic")

    if "external_contact" in indicators and "no_interview" in indicators:
        patterns.append("Hiring without interview via messaging platform")

    return patterns



def generate_reasoning(indicators, patterns):

    explanations = []

    if "payment_request" in indicators:
        explanations.append(
            "The job requests payment during the hiring process which is uncommon for legitimate employers."
        )

    if "external_contact" in indicators:
        explanations.append(
            "The employer asks applicants to communicate via external messaging platforms."
        )

    if "urgency_tactic" in indicators:
        explanations.append(
            "The job uses urgency language such as limited seats or immediate joining."
        )

    if "no_interview" in indicators:
        explanations.append(
            "The job claims hiring without an interview process."
        )

    if indicators and patterns:
        explanations.append(
            "Multiple scam indicators appear together which increases fraud risk."
        )

    return explanations