### **Preparing visualizations**

```
input: route_id, direction_id → output: map.html
```

```
Step 0:
[X] Enter route_id & direction_id.
```

```
Step 1:
[X] Open gtfs files using pandas.
[ ] Ventana del tiempo del cálculo. (?)
```

```
Step 2:
[X] Filter route_id & direction_id in trips.txt.
[X] Create shape_id & trip_id lists.
```

```
Step 3:
[X] Select 1st shape_id in list.
[X] Find its geometry in shapes.txt. (→)
```

```
Step 4:
[X] Select 1st trip_id in stop_times.txt.
[X] Find stops sequence in shapes.txt.
```

```
Step 5:
[X] Find coordinates of each stop in stops.txt. (→)
```

```
Step 6:
[X] Convert geo coordinantes into utm coordinates.
[X] Create Linestring using shapes. (→)
[X] Create Point using stop_id's.
[X] Iterate linestring.projection(point). (→)
```

```
Step 7:
[ ] Calculate velocity per section (input, route_id, direction_id, time_lapse). (→)
```

```
Step 8:
[ ] Make a color graph to show velocity-section relation.
```

```
Step 9:
[ ] Show map, drawing the trip on it.
```