from datetime import datetime, timedelta
import numpy as np


class Orbit:
    def __init__(self, semi_major_axis_epoch, semi_major_axis_delta,
                 eccentricity_epoch, eccentricity_delta,
                 inclination_epoch, inclination_delta,
                 mean_longitude_epoch, mean_longitude_delta,
                 long_of_perihelion_epoch, long_of_perihelion_delta,
                 long_of_asc_node_epoch, long_of_asc_node_delta,
                 const_b=1, const_c=1, const_s=1, const_f=1):
        self.semi_major_axis_epoch = semi_major_axis_epoch  # astronomical units
        self.semi_major_axis_delta = semi_major_axis_delta  # astronomical units / century
        self.eccentricity_epoch = eccentricity_epoch  # radians
        self.eccentricity_delta = eccentricity_delta  # radians / century
        self.inclination_epoch = inclination_epoch  # degrees
        self.inclination_delta = inclination_delta  # degrees / century
        self.mean_longitude_epoch = mean_longitude_epoch  # degrees
        self.mean_longitude_delta = mean_longitude_delta  # degrees / century
        self.long_of_perihelion_epoch = long_of_perihelion_epoch  # degrees
        self.long_of_perihelion_delta = long_of_perihelion_delta  # degrees / century
        self.long_of_asc_node_epoch = long_of_asc_node_epoch  # degrees
        self.long_of_asc_node_delta = long_of_asc_node_delta  # degrees / century
        self.const_b = const_b  # additional values needed to adjust formula for gas giants
        self.const_c = const_c  # don't really know what they represent
        self.const_s = const_s
        self.const_f = const_f

    def get_pos_at_date(self, julian_date):
        delta_time = (julian_date - 2451545)/36525
        print(delta_time)

        # get current values for all base variables
        semi_major_axis = self.semi_major_axis_epoch + (self.semi_major_axis_delta * delta_time)
        eccentricity = self.eccentricity_epoch + (self.eccentricity_delta * delta_time)
        inclination = self.inclination_epoch + (self.inclination_delta * delta_time)
        mean_longitude = self.mean_longitude_epoch + (self.mean_longitude_delta * delta_time)
        long_of_perihelion = self.long_of_perihelion_epoch + (self.long_of_perihelion_delta * delta_time)
        long_of_asc_node = self.long_of_asc_node_epoch + (self.long_of_asc_node_delta * delta_time)

        # calculate argument of perihelion and the mean anomaly
        # argument_of_perihelion = long_of_perihelion - long_of_asc_node
        mean_anomaly = (mean_longitude - long_of_perihelion + (self.const_b * delta_time * delta_time) +
                        (self.const_c * np.cos(self.const_f * delta_time)) +
                        (self.const_s * np.sin(self.const_f * delta_time)))

        # modulus mean_anomaly so it is between -180 and 180
        mean_anomaly = (mean_anomaly % 360) - 180
        print(mean_anomaly)

        # calculate eccentric_anomaly
        eccentric_anomaly = mean_anomaly - (np.rad2deg(eccentricity) * np.sin(mean_anomaly))
        tolerance = pow(10, -6)
        while True:
            d_mean_anomaly = (mean_anomaly - (eccentric_anomaly - (np.rad2deg(eccentricity)) * np.sin(eccentric_anomaly)))
            d_eccentric_anomaly = d_mean_anomaly / (1 - (eccentricity * np.cos(eccentric_anomaly)))
            eccentric_anomaly = eccentric_anomaly + d_eccentric_anomaly
            if d_eccentric_anomaly <= tolerance:
                break

        # calculate heliocentric coordinates
        x_helio = semi_major_axis * (np.cos(eccentric_anomaly - eccentricity))
        y_helio = semi_major_axis * np.sqrt(1 - ((eccentricity * eccentricity) * np.sin(eccentric_anomaly))) * np.sin(eccentric_anomaly)

        return [x_helio, y_helio, 0]
