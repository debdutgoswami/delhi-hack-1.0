## imports
import numpy as np

#Distancing Algorithm
def haversine_distance(lat1, lon1, lat2, lon2):
   r = 6371 # Radius of Earth
   phi1 = np.radians(lat1)
   phi2 = np.radians(lat2)
   delta_phi = np.radians(lat2-lat1)
   delta_lambda = np.radians(lon2-lon1)
   a = np.sin(delta_phi / 2)**2 + np.cos(phi1) * np.cos(phi2) *  np.sin(delta_lambda / 2)**2
   res = r * (2 * np.arctan2(np.sqrt(a), np.sqrt(1-a)))
   return np.round(res, 2)

#Driver Function
def withinRange(requestLocation, donorLocation, radius):
    lat1 = requestLocation[0]
    lon1 = requestLocation[1]

    lat2 = donorLocation[0]
    lon2 = donorLocation[1]
    
    #Consider the radius as float
    if haversine_distance(lat1, lon1, lat2, lon2) < radius:
        return True
    else:
        return False
    ## returns True or False whether the user is in range or not

# Test Case
if __name__ == "__main__":
    print(withinRange((22.8637511,88.3669716), (26.8704699,88.3593088), 30.00))