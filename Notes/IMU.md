# Inertial Measurement Units

Contains *multiple* sensors. Doesn't exist in reality on drones, as sensors are scattered.

Sensors:
- [[#Gyro]] - Rotational Velocity (in all three axis)
- [[#Accelerometer]]
- [[#Magnetometer]] - Magnetic fields
- [[#Barometer]] - Changes in preasure

These are [[#Combinding Gyro and Accelerometers|combined to get good pose estimates]].

### Gyro
> *"The sensor itself is actually a really **really** accurate sensor with very low noise"*
> \- Keld

> [!warning] Drift
> Integrating velocity will cause the estimated pose to drift from reality over time, as it accumulated small errors.


We integrate the small changes in position (velocity) $w$ to get the pose $A$.
$$
A = \int_{0}^{T} w \,\mathrm{dt}
$$
In practice, this is done with a sum
$$
A = \sum_{0}^{t} w \cdot \Delta t
$$

### Accelerometer

> *"Accelerometers as **crappy** sensors. They are very noisy."*
> \- Keld

Measures accelerations. Can be used to measure the direction of gravity.

It may be noisy but it makes **absolute measurements**.

### Magnetometer
Measures the magnetic fields. Can be used as a compas if one axis is locked down. This could be by the accelerometer.

*Crappy sensors* in a drone enviormnent.

### Barometer
Measures preasure. Combined with GPS it can be used to estimate altitude, as the presure on the ground changes depending on the terrain.

## Combinding Sensor Measurements
*Every* drone uses a [[Kalman Filter|kalman filter]] to combine the measurements of the gyro and accelerometer (and other sensors). This makes it possible to use the accuracy of the gyro, and account for its drift with the accelerometer and a physical model of the drone.

---
#drones