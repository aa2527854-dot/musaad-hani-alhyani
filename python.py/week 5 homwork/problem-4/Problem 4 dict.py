company = {
    "ceo": "Ahmed",
    "departments": {
        "engineering": {
            "manager": "Sara",
            "team_size": 12,
            "projects": ["Backend API", "Mobile App"],
        },
        "design": {
            "manager": "Omar",
            "team_size": 5,
            "projects": ["Website Redesign"],
        },
    },
}


print("CEO:", company["ceo"])
print("Engineering Manager:", company["departments"]["engineering"]["manager"])
print("Design Team Size:", company["departments"]["design"]["team_size"])
print("First Engineering Project:", company["departments"]["engineering"]["projects"][0])
total_team = (
    company["departments"]["engineering"]["team_size"]
    + company["departments"]["design"]["team_size"]
)
print("Total Team Size:", total_team)
company["departments"]["design"]["team_size"] = 6
company["departments"]["marketing"] = {
    "manager": "Lina",
    "team_size": 3,
    "projects": [],
}
print("Marketing Department:", company["departments"]["marketing"])
