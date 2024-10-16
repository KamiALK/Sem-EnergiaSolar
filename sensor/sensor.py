
import dash
from dash.dependencies import Output, Input
from dash import dcc, html
from datetime import datetime
import json
import plotly.graph_objs as go
from collections import deque
from flask import Flask, request

# Configuración del servidor Flask
server = Flask(__name__)
app = dash.Dash(__name__, server=server)

# Constantes
MAX_DATA_POINTS = 1000
UPDATE_FREQ_MS = 1000  # Actualización cada segundo

# Listas para almacenar los datos
time = deque(maxlen=MAX_DATA_POINTS)
lux_values = deque(maxlen=MAX_DATA_POINTS)

app.layout = html.Div(
    [
        dcc.Markdown(
            children="""
            # Live Sensor Readings
            Streamed from Sensor Logger
        """
        ),
        dcc.Graph(id="live_graph"),
        dcc.Interval(id="counter", interval=UPDATE_FREQ_MS),
    ]
)

@app.callback(Output("live_graph", "figure"), Input("counter", "n_intervals"))
def update_graph(_counter):
    data = [
        go.Scatter(x=list(time), y=list(lux_values), name="Light (Lux)")
    ]

    graph = {
        "data": data,
        "layout": go.Layout(
            {
                "xaxis": {"type": "date"},
                "yaxis": {"title": "Lux"},
            }
        ),
    }
    if len(time) > 0:
        graph["layout"]["xaxis"]["range"] = [min(time), max(time)]
        graph["layout"]["yaxis"]["range"] = [min(lux_values), max(lux_values)]

    return graph

@server.route("/data", methods=["POST"])
def receive_data():
    if request.method == "POST":
        try:
            data = json.loads(request.data)
            for d in data['payload']:
                if d.get("name") == "light":
                    ts = datetime.fromtimestamp(d["time"] / 1000000000)
                    if len(time) == 0 or ts > time[-1]:
                        time.append(ts)
                        lux_values.append(d["values"].get("lux", 0))
        except json.JSONDecodeError as e:
            print(f"JSON decode error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
    return "success"

if __name__ == "__main__":
    app.run_server(port=8000, host="0.0.0.0")
