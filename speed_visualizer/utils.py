import os

import pandas as pd
import plotly.express as px
import utm
from matplotlib import pyplot as plt
from shapely import Point, LineString

from speed_visualizer.config import INPUT_PATH, OUTPUT_PATH


# ------------------------------------------------------------------------------------------------------------------- #
#                                                                                                                     #
#                                               Plotting figures & map                                                #
#                                                                                                                     #
# ------------------------------------------------------------------------------------------------------------------- #


def show_curve_with_stops(curve_geo, points_in_curve):
    """Given the shape's geographical coordinates and its stops, generates a simple graph."""

    # plotting shapes
    plt.plot(curve_geo["shape_pt_lat"], curve_geo["shape_pt_lon"])

    # plotting stops
    plt.scatter(points_in_curve["stop_lat"], points_in_curve["stop_lon"])

    plt.show()


def generate_stop_matching_evaluation_map(shape_, stops_, filename, auto_open=True):
    """Given a dataframe with shapes and another with stops (both in geographic coordinates), generates an
    interactive html map with the route's shape segmented and colored by speeds."""

    mapbox_access_token = 'pk.eyJ1IjoidHJhbnNhcHAiLCJhIjoiY2w4czhubzh3MXhwajNwbzgwM2dzM3R6bCJ9.vsA2xogBFcRYH2DbwDOb4w'

    # all stops
    fig1 = px.scatter_mapbox(stops_, lat='stop_lat', lon='stop_lon', hover_name='stop_name',
                             color_discrete_sequence=['white'], hover_data=['stop_id', 'stop_name'],
                             height=700, title="stops")

    # shape
    fig2 = px.line_mapbox(shape_, lat='shape_pt_lat', lon='shape_pt_lon', color_discrete_sequence=['blue'], zoom=12)

    # end shape point
    fig3 = px.scatter_mapbox(shape_.iloc[-1:], lat='shape_pt_lat', lon='shape_pt_lon', title="final",
                             color_discrete_sequence=['red'], height=700, size=[20])

    fig2.add_trace(fig3.data[0])
    fig2.add_trace(fig1.data[0])

    fig2.update_layout(mapbox_style="dark", mapbox_accesstoken=mapbox_access_token)
    fig2.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    fig2.show()
    fig2.write_html(os.path.join(OUTPUT_PATH, '{0}.html'.format(filename)), auto_open=auto_open)


# ------------------------------------------------------------------------------------------------------------------- #
#                                                                                                                     #
#                                                 Getting coordinates                                                 #
#                                                                                                                     #
# ------------------------------------------------------------------------------------------------------------------- #


def get_shapes_dict(route_id, direction_id):
    """Given route and direction, gets a dictionary that holds shapes with theirs respective trips."""

    trips = pd.read_csv(os.path.join(INPUT_PATH, 'trips.txt'))

    shapes_trips_dict = dict()

    # filtering by route_id & direction_id
    _trips = trips[(trips["route_id"] == route_id) & (trips["direction_id"] == direction_id)][["shape_id", "trip_id"]]

    unique_shades_in_trips = _trips["shape_id"].unique()

    # adding shape with its trips
    for shape_id in list(unique_shades_in_trips):
        shapes_trips_dict[f'{shape_id}'] = _trips[_trips["shape_id"] == shape_id]['trip_id'].tolist()

    return shapes_trips_dict


def get_shapes_coordinates(shape_id):
    """Given a shape_id, gets a dataframe with the curve coordinates in (lat,lon) & (x,y) tuples."""

    shapes = pd.read_csv(os.path.join(INPUT_PATH, 'shapes.txt'))

    def _utm_converter(row):
        """Auxiliary function for creating new columns with geographical coordinates."""

        return latlon_point_to_utm(row["shape_pt_lat"], row["shape_pt_lon"])

    curve = shapes[shapes["shape_id"] == int(shape_id)][["shape_pt_lat", "shape_pt_lon"]]
    curve[["shape_pt_x", "shape_pt_y"]] = curve.apply(_utm_converter, axis="columns", result_type="expand")

    curve_geo = curve[["shape_pt_lat", "shape_pt_lon"]]
    curve_utm = curve[["shape_pt_x", "shape_pt_y"]]

    return curve_geo, curve_utm


def get_stops_coordinates(trip_id):
    """Given trip_id, gets a dataframe with the stops coordinates in (lat,lon) & (x,y) tuples."""

    stop_times = pd.read_csv(os.path.join(INPUT_PATH, 'stop_times.txt'))
    stops = pd.read_csv(os.path.join(INPUT_PATH, 'stops.txt'))

    def _utm_converter(row):
        """Auxiliary function for creating new columns with geographical coordinates."""

        return latlon_point_to_utm(row["stop_lat"], row["stop_lon"])

    stops_sequence = stop_times[stop_times["trip_id"] == trip_id]["stop_id"].tolist()

    stop_points = stops[stops["stop_id"].isin(stops_sequence)][["stop_id", "stop_name", "stop_lat", "stop_lon"]]
    stop_points[["stop_x", "stop_y"]] = stop_points.apply(_utm_converter, axis="columns", result_type="expand")

    stops_geo = stop_points[["stop_id", "stop_name", "stop_lat", "stop_lon"]]
    stops_utm = stop_points[["stop_id", "stop_name", "stop_x", "stop_y"]]

    return stops_geo, stops_utm


# ------------------------------------------------------------------------------------------------------------------- #
#                                                                                                                     #
#                                             Converting geographical-utm                                             #
#                                                                                                                     #
# ------------------------------------------------------------------------------------------------------------------- #


def latlon_point_to_utm(latitude, longitude):
    x, y, _, _ = utm.from_latlon(latitude, longitude)
    return x, y


def utm_point_to_latlon(x, y, zone_number, zone_letter):
    latitude, longitude = utm.to_latlon(x, y, zone_number, zone_letter)
    return latitude, longitude
