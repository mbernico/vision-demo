# Copyright 2020 Google LLC. This software is provided as-is, without
#  warranty or representation for any use or purpose. Your use of it 
# is subject to your agreement with Google.

from google.cloud import storage


def bb_intersection_over_union(box_a, box_b):
    """Computes the Intersection over Union for two rectangular bounding boxes."""
    
    #determine the (x, y)-coordinates of the intersection rectangle
    x_1 = max(box_a[0], box_b[0])
    y_1 = max(box_a[1], box_b[1])
    x_2 = min(box_a[2], box_b[2])
    y_2 = min(box_a[3], box_b[3])
    
    # compute the area of intersection rectangle
    intersection_area = max(0, x_2 - x_1 + 1) * max(0, y_2 - y_1 + 1)
    
    # compute the area of both rectangles
    box_a_area = (box_a[2] - box_a[0] + 1) * (box_a[3] - box_a[1] + 1)
    box_b_area = (box_b[2] - box_b[0] + 1) * (box_b[3] - box_b[1] + 1)

    # intersection area divided by union area - intersection area
    iou = intersection_area / float(box_a_area + box_b_area - intersection_area)
    return iou


def get_image_uris(bucket_name):
    """Get a list of image uris to annotate from a GCS bucket"""
    storage_client = storage.Client()
    blobs = storage_client.list_blobs(bucket_name)

    gs_uris = []
    for blob in blobs:
        gs_uris.append("gs://"+bucket_name+"/"+blob.name)
    return gs_uris

def build_request(uri):
    """Build an annotation request from a gcs uri"""
    request = {
        'image': {
            'source': {'image_uri': uri},
        },
    }
    return request

