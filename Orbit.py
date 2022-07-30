from datetime import datetime, timedelta
import numpy as np


# https://ssd.jpl.nasa.gov/planets/approx_pos.html
# https://www.stjarnhimlen.se/comp/tutorial.html#11

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

        # additional values needed to adjust formula for gas giants
        # don't really know what they represent
        self.b = const_b
        self.c = const_c
        self.s = const_s
        self.f = const_f

    def get_pos_at_date(self, date):
        # IMPORTANT INFO
        # Astronomers like to use DEGREES, numpy only likes RADIANS
        # This has caused me many headaches

        # calculate the number of centuries between J2000 and the target date
        epoch = datetime(2000, 1, 1)
        SECONDS_PER_CENTURY = 3_153_600_000
        delta_T = (date - epoch).total_seconds() / SECONDS_PER_CENTURY

        # get current values for all base variables
        # x = x_0 + Δx*ΔT
        sm_axis = self.semi_major_axis_epoch + (self.semi_major_axis_delta * delta_T)  # a - astronomical units
        ecc = self.eccentricity_epoch + (self.eccentricity_delta * delta_T)  # e - unitless from 0 to 1
        inc_deg = self.inclination_epoch + (self.inclination_delta * delta_T)  # I - degrees
        m_long_deg = self.mean_longitude_epoch + (self.mean_longitude_delta * delta_T)  # L - degrees
        long_peri_deg = self.long_of_perihelion_epoch + (self.long_of_perihelion_delta * delta_T)  # ῶ - degrees
        long_asc_deg = self.long_of_asc_node_epoch + (self.long_of_asc_node_delta * delta_T)  # Ω - degrees

        # calculate argument of perihelion - degrees
        # ω = ῶ - Ω
        arg_of_p_deg = long_peri_deg - long_asc_deg

        # calculate mean anomaly - degrees
        # M = L - ῶ + b*(T^2) + c*cos(f*T) + s*sin(f*T)
        m_anomaly_deg = (m_long_deg + (self.b * (delta_T * delta_T)) + (self.c * np.cos(np.deg2rad(self.f * delta_T)))
                         + (self.s * np.sin(np.deg2rad(self.f * delta_T))))

        # convert mean anomaly to radians
        m_anomaly_rad = np.deg2rad(m_anomaly_deg)

        # calculate eccentric anomaly
        # can only be approximated by iterations

        ecc_anomaly_rad = m_anomaly_rad - (ecc * np.sin(m_anomaly_rad))
        tolerance = pow(10, -6)
        while True:
            d_m_anomaly_rad = m_anomaly_rad - (ecc_anomaly_rad - (ecc * np.sin(m_anomaly_rad)))
            d_ecc_anomaly_rad = d_m_anomaly_rad / (1 - (ecc * np.cos(ecc_anomaly_rad)))
            ecc_anomaly_rad = ecc_anomaly_rad + d_ecc_anomaly_rad
            if d_ecc_anomaly_rad <= tolerance:
                break

        # calculate heliocentric (origin at sun) in the orbital plane (z = 0)
        x_orb = sm_axis * (np.cos(ecc_anomaly_rad) - ecc)
        y_orb = sm_axis * (np.sqrt(1 - (ecc * ecc)) * np.sin(ecc_anomaly_rad))

        # convert to the ecliptic reference plane (the plane of the earth's orbit)
        sin_P = np.sin(np.deg2rad(arg_of_p_deg))
        cos_P = np.cos(np.deg2rad(arg_of_p_deg))
        sin_ASC = np.sin(np.deg2rad(long_asc_deg))
        cos_ASC = np.cos(np.deg2rad(long_asc_deg))
        sin_I = np.sin(np.deg2rad(inc_deg))
        cos_I = np.cos(np.deg2rad(inc_deg))

        x_ecl = ((((cos_P * cos_ASC) - (sin_P * sin_ASC * cos_I)) * x_orb) +
                 ((-1 * (sin_P * cos_ASC) - (cos_P * sin_ASC * cos_I)) * y_orb))

        y_ecl = ((((cos_P * sin_ASC) + (sin_P * cos_ASC * cos_I)) * x_orb) +
                 ((-1 * sin_P * sin_ASC) + (cos_P * cos_ASC * cos_I)) * y_orb)

        z_ecl = (sin_P * sin_I * x_orb) + (cos_P * sin_I * y_orb)

        return [x_ecl, y_ecl, z_ecl]
