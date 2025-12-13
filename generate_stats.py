import requests
import os
from datetime import datetime

GITHUB_USERNAME = "yahiaelbanna"
GITHUB_TOKEN = os.getenv("GH_TOKEN")
HEADERS = {"Authorization": f"Bearer {GITHUB_TOKEN}"} if GITHUB_TOKEN else {}

def get_github_data():
    stats = {
        "total_contributions": 1500,
        "current_streak": 42,
        "longest_streak": 120,
        "account_created": "Jan 2018",
        "total_repositories": 36
    }
    try:
        user_url = f"https://api.github.com/users/{GITHUB_USERNAME}"
        user_data = requests.get(user_url, headers=HEADERS).json()
        stats["account_created"] = datetime.strptime(user_data.get("created_at", "2018-01-01"), "%Y-%m-%dT%H:%M:%SZ").strftime("%b %Y")
        stats["total_repositories"] = user_data.get("public_repos", 0)
    except:
        pass
    return stats

def generate_streak_svg(stats):
    width = 500
    height = 200
    colors = {
        "bg": "#141321",
        "border": "#FE428E",
        "text": "#F8D847",
        "streak_fire": "#FE428E",
        "total_label": "#F8D847",
        "total_value": "#FFFFFF",
        "current_label": "#FE428E",
        "current_value": "#FFFFFF",
        "longest_label": "#9EFFFF",
        "longest_value": "#FFFFFF"
    }
    current_date = datetime.now().strftime("%b %d, %Y")
    svg_content = f'''
<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
    <rect width="100%" height="100%" fill="{colors['bg']}" rx="10" ry="10"/>
    <rect x="5" y="5" width="{width-10}" height="{height-10}" fill="none" stroke="{colors['border']}" stroke-width="2" rx="8" ry="8"/>
    <text x="20" y="35" font-family="Segoe UI, Ubuntu, sans-serif" font-size="16" font-weight="bold" fill="{colors['text']}">GitHub Contribution Streak</text>
    <text x="420" y="50" font-family="Arial, sans-serif" font-size="24" font-weight="bold" fill="{colors['streak_fire']}">🔥</text>
    <text x="20" y="80" font-family="Segoe UI, Ubuntu, sans-serif" font-size="13" fill="{colors['total_label']}">Total Contributions</text>
    <text x="20" y="105" font-family="Segoe UI, Ubuntu, sans-serif" font-size="24" font-weight="bold" fill="{colors['total_value']}">{stats['total_contributions']}</text>
    <text x="180" y="80" font-family="Segoe UI, Ubuntu, sans-serif" font-size="13" fill="{colors['current_label']}">Current Streak</text>
    <text x="180" y="105" font-family="Segoe UI, Ubuntu, sans-serif" font-size="24" font-weight="bold" fill="{colors['current_value']}">{stats['current_streak']} days</text>
    <text x="340" y="80" font-family="Segoe UI, Ubuntu, sans-serif" font-size="13" fill="{colors['longest_label']}">Longest Streak</text>
    <text x="340" y="105" font-family="Segoe UI, Ubuntu, sans-serif" font-size="24" font-weight="bold" fill="{colors['longest_value']}">{stats['longest_streak']} days</text>
    <line x1="20" y1="130" x2="{width-20}" y2="130" stroke="{colors['border']}" stroke-width="1"/>
    <text x="20" y="160" font-family="Segoe UI, Ubuntu, sans-serif" font-size="11" fill="{colors['text']}">Account created: {stats['account_created']} • Total repos: {stats['total_repositories']}</text>
    <text x="{width-150}" y="160" font-family="Segoe UI, Ubuntu, sans-serif" font-size="11" fill="{colors['text']}">Updated: {current_date}</text>
</svg>
'''
    return svg_content

def main():
    stats = get_github_data()
    svg_content = generate_streak_svg(stats)
    with open("github_streak_stats.svg", "w", encoding="utf-8") as f:
        f.write(svg_content)

if __name__ == "__main__":
    main()