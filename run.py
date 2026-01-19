from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/dashboard')
def get_dashboard_data():
    data = {
        "user": {
            "name": "Alex Johnson",
            "title": "Premium Member",
            "avatar": "https://lh3.googleusercontent.com/aida-public/AB6AXuDncb98cFnjTUG0_qZX9xj9aF7aaU2Kx4LnvpsHmCPt6nmhlTBNgkRstaP139-LTgs91QHlv4k6RJ6VO99FS4-hP1h5vPaxWIxEHL9l6zH6npd484TbP7ntUBQdpztKzZysRogUbaxCyGWEUlaEJpVuFNcF0BehGAq0HtN_T6tJqeXjDx9nbI8Kp0CqQ9ZVfFLtoGX2mAMLIb5Oqpa4vZSjt3yqQLaoxLVcGKbIkjmR4uIFWfFq-28xFW-Q5Yh_r-5mvz4V2DbQBXZe"
        },
        "greeting": "Good morning, Alex.",
        "goal_progress": "You're 15% closer to your goal today. Keep the momentum going!",
        "readiness": {
            "score": 82,
            "change": 5,
            "description": "Interview Ready status achieved. Your performance in Speaking improved significantly."
        },
        "daily_goal": {
            "completed": 2,
            "total": 3,
            "description": "Complete 1 more mock interview to reach your daily target.",
            "avg_session_time": 15
        },
        "performance_trends": {
            "average": 78.5,
            "change": 12,
            "chart_data": [109, 21, 41, 93, 33, 101, 61, 45, 121, 149, 1, 81, 129, 25]
        },
        "recommendation": {
            "title": "Ready to level up?",
            "description": "Start a tailored Mock Interview for Senior Product Manager roles and get real-time AI feedback."
        },
        "skills_breakdown": [
            {"skill": "Aptitude", "score": 90, "color": "blue-500"},
            {"skill": "Speaking", "score": 75, "color": "indigo-500"},
            {"skill": "Listening", "score": 88, "color": "cyan-500"},
            {"skill": "Reading", "score": 82, "color": "sky-500"}
        ],
        "reminders": {
            "email_notifications": True,
            "next_session": "Tomorrow, 10:00 AM"
        },
        "recent_activity": [
            {
                "type": "Mock Interview",
                "title": "Tech Lead",
                "status": "Completed",
                "score": "88%",
                "icon": "check"
            },
            {
                "type": "New Skill",
                "title": "Active Listening",
                "status": "Lesson finished",
                "time": "20 mins ago",
                "icon": "history_edu"
            }
        ]
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
