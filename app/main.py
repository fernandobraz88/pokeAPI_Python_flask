from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

teams_db = {}
team_id_counter = 1


@app.route('/api/teams', methods = ['GET'])
def get_teams():
    return jsonify(teams_db)

@app.route('/api/teams/<user>', methods=['GET'])
def get_team_by_user(user):
    for team_id, team in teams_db.items():
        if team["owner"] == user:
            return jsonify({team_id: team})
    return jsonify({"error": "Team not found"}), 404


@app.route('/api/teams', methods=['POST'])
def create_team():
    global team_id_counter
    data = request.json
    user = data.get('user')
    team_names = data.get('team')

    if not user or not team_names:
        return jsonify({"error": "User and team are required"}), 400

    team_data = []
    for name in team_names:
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name.lower()}')
        if response.status_code == 404:
            return jsonify({"error": f"Pokemon {name} not found"}), 404
        pokemon_data = response.json()
        team_data.append({
            "id": pokemon_data["id"],
            "name": pokemon_data["name"],
            "weight": pokemon_data["weight"],
            "height": pokemon_data["height"]
        })

    team_id = team_id_counter
    teams_db[team_id] = {"owner": user, "pokemons": team_data}
    team_id_counter += 1

    return jsonify({"message": "Team created successfully", "id": team_id})

if __name__ == '__main__':
    app.run(debug=True)