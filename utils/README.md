## Utils for dataset creation:
 File | What does it do   | Libraries  
--- | --- | ---
[bounding_box_generator.py](https://github.com/LadaChernenko/bird_species_guide/blob/main/utils/bounding_box_generator.py) | generate txt file with bounding box coordinate from json | os; pandas; json

`bounding_box_generator` make txt file for each image with bounding boxes coordinate and labels 
```
[[0, 0.2725, 0.5341463414634147, 0.495, 0.8731707317073171]]
```
Label studio create json file, but it contains redundant information.
```javascript
{"id": 5618, 
"annotations": [{"id": 5848, 
                 "completed_by": {"id": 1, 
                                  "email": "", 
                                  "first_name": "", 
                                  "last_name": ""}, 
                 "state": {}, 
                 "result": [{"original_width": 640, 
                            "original_height": 480, 
                            "image_rotation": 0, 
                            "value": {"x": 12.5, 
                                      "y": 16.875,
                                      "width": 46.40625, 
                                      "height": 78.125, 
                                      "rotation": 0, 
                                      "rectanglelabels": ["willow_grouse"]}, 
                            "id": "slQsY9CKWc", 
                            "from_name": "label", 
                            "to_name": "image", 
                            "type": "rectanglelabels"}], 
                  "was_cancelled": false, 
                  "ground_truth": false, 
                  "created_at": "2021-07-03T14:27:52.880146Z", 
                  "updated_at": "2021-07-03T14:27:52.880146Z", 
                  "lead_time": 7.556, 
                  "prediction": {}, 
                  "result_count": 0, 
                  "task": 5618}], 
"predictions": [], 
"file_upload": "b019_0238.jpg", 
"data": {"image": "/data/upload/b019_0238.jpg"}, 
"meta": {}, 
"created_at": "2021-07-03T14:18:47.230796Z", 
"updated_at": "2021-07-03T14:18:47.230796Z", 
"project": 7}
```
