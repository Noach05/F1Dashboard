import matplotlib.pyplot as plt
import fastf1
import fastf1.plotting

fastf1.plotting.setup_mpl(misc_mpl_mods=False, color_scheme='fastf1')

session = fastf1.get_session(2022, 'Monza', 'R')

session.load()
fast_verstappen = session.laps.pick_driver('VER').pick_fastest()
lec_car_data = fast_verstappen.get_car_data()
t = lec_car_data['Time']
vCar = lec_car_data['Speed']

# The rest is just plotting
fig, ax = plt.subplots()
ax.plot(t, vCar, label='Fast')
ax.set_xlabel('Time')
ax.set_ylabel('Speed [Km/h]')
ax.set_title('Verstappen is')
ax.legend()
plt.show()