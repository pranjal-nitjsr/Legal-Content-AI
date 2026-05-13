from flask import Flask, render_template, request

app = Flask(__name__)

def generate_legal_content(service_type, audience, location, tone):
    content = f"""
Service Page Draft

Our {service_type} service in {location} is designed to help {audience}
understand their legal requirements in a simple and clear way.

We focus on providing information that is easy to understand, practical,
and suitable for people who need basic guidance before taking the next step.

Tone: {tone}

FAQs:

1. What is this service about?
This service helps users understand basic information related to {service_type}.

2. Who can use this service?
This service is useful for {audience}.

3. Is this content final legal advice?
No, this is an AI-generated draft and should be reviewed by a legal expert.
"""
    return content


@app.route("/", methods=["GET", "POST"])
def index():
    generated_content = ""

    if request.method == "POST":
        service_type = request.form.get("service_type")
        audience = request.form.get("audience")
        location = request.form.get("location")
        tone = request.form.get("tone")

        generated_content = generate_legal_content(
            service_type,
            audience,
            location,
            tone
        )

    return render_template("index.html", generated_content=generated_content)


if __name__ == "__main__":
    app.run(debug=True)
