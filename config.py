
from flask import Flask, jsonify, request
import configparser

filename = 'config.ini'
config = configparser.ConfigParser()
config.read(filename)
# i need to make sure that the config file is read properly and raise an error gracefully
if not config.sections():
    raise FileNotFoundError(f"Configuration file {filename} not found or is empty.")
# print the config to see if it is read properly
# for section in config.sections():
#     print(f"[{section}]")
#     for key, value in config[section].items():
#         print(f"{key} = {value}")

# need to extract key value pairs from the config file and store them in a dictionary

#config_dict = {section: dict(config[section]) for section in config.sections()}
try:
    config_dict = {}
    for section in config.sections():
        config_dict[section] = {}
        config_dict[section] = dict(config[section])
        
except Exception as e:
    print(f"Error extracting key-value pairs: {e}")
# Finally save the output file data as JSON data in the database.

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the config API. If you want to see the config, go to /config"

@app.route('/config', methods=['GET'])
def get_config():
    return jsonify(config_dict)

if __name__ == '__main__':
    app.run(debug=True)

