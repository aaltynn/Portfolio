from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Dynamic data to show off your exact skill set
    profile = {
        "name": "Altyn",
        "title": "Full-Stack Python & Mobile Developer",
        "bio": "Passionate developer specializing in building modular backend systems with Flask, cross-platform mobile apps with Kivy, and integrating advanced AI/Third-Party APIs.",
        "skills": {
            "Backend": ["Python", "Flask", "REST APIs", "Modular Architecture", "Environment Safety (.env)"],
            "Mobile & Frontend": ["Kivy", "HTML5", "CSS3", "JavaScript"],
            "Tools & DevOPS": ["Git / GitHub", "VS Code", "Git Bash / CMD", "Custom Domain Deployment"]
        },
        "projects": [
            {
                "title": "AI Plant Detector",
                "subtitle": "Full-Stack AI & Weather Analytics App",
                "desc": "A modular system built with Flask (Web) and Kivy (Mobile) that integrates OpenAI and Crop Health APIs along with OpenWeather data to diagnose plant health.",
                "link": "https://github.com/aaltynn/Plant_detector",
                "tags": ["Python", "Flask", "Kivy", "APIs", "AI"]
            },
            {
                "title": "Personal Portfolio",
                "subtitle": "Production-Ready Full-Stack Portfolio",
                "desc": "This exact portfolio website, engineered with Python and Flask, structured with industry-standard practices, and deployed on a custom domain.",
                "link": "https://github.com/aaltynn/Website",
                "tags": ["Flask", "Python", "UI/UX", "Custom Domain"]
            }
        ]
    }
    return render_template('index.html', profile=profile)

if __name__ == '__main__':
    app.run(debug=True)