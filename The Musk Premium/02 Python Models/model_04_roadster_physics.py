"""
MODEL 04  Can a car really do 0 to 60 in one second, and what is in the tanks?
Simple physics with stated assumptions, not Tesla data.
1. Acceleration: 60 mph (26.82 m/s) in 1.0 s is 26.82 m/s2, or 2.73 g on average.
2. Grip: a road tyre can push a car forward at roughly 1.1 g (friction coefficient of about
   1.1, an assumption for good performance tyres). The rest must come from the thrusters.
3. Thrust and air needed: car mass of 1,900 kg (the '4000+ pound' car plus a driver).
   Extra force = (2.73 - 1.1) g x mass for one second, so the impulse in newton seconds equals
   the force. Cold gas thrusters on compressed air have a specific impulse of about 65 s (range
   50 to 75 s), so air needed = impulse / (Isp x g0).
4. Tank: 600 litres. Air held at 100, 200 and 300 bar from the ideal gas law at 20 C
   (density = p / (R T), R = 287), which slightly overstates mass at high pressure.
5. Stored energy: energy released if the gas expands isothermally to air pressure,
   W = p V ln(p / p0), expressed in kilograms of TNT at 4.184 MJ per kg.
"""
from common import *

style()
g0, mph60, mass, mu, isp = 9.81, 26.82, 1900, 1.1, 65
a_g = mph60 / 1.0 / g0
extra_g = a_g - mu
impulse = extra_g * g0 * mass * 1.0
air_kg = {i: impulse / (i * g0) for i in (50, 65, 75)}
V, R, T, p0 = 0.6, 287, 293, 1e5
rows = []
for bar in (100, 200, 300):
    p = bar * 1e5
    held = p * V / (R * T)
    energy = p * V * np.log(p / p0)
    rows.append({"pressure_bar": bar, "air_held_kg": held, "launches_possible": held / air_kg[65],
                 "stored_energy_mj": energy / 1e6, "tnt_equivalent_kg": energy / 4.184e6})
tank = pd.DataFrame(rows).set_index("pressure_bar")
res = pd.Series({"average_g_0_60_in_1s": a_g, "g_from_tyres": mu, "g_from_thrusters": extra_g,
                 "thrust_kn": impulse / 1000, "air_needed_kg_isp65": air_kg[65], "air_needed_kg_isp50": air_kg[50], "air_needed_kg_isp75": air_kg[75]})
save_table(tank.round(1), "m04_tank"); save_table(res.round(2).to_frame("value"), "m04_launch")

fig, axes = plt.subplots(1, 2, figsize=(11, 4.4))
ax = axes[0]
cases = ["Family car\n0 to 60 in 8s", "Model S Plaid\n0 to 60 in 2s", "Roadster Thrust\n0 to 60 in 1s"]
g = [mph60 / 8 / g0, mph60 / 2 / g0, a_g]
ax.bar(range(3), [min(v, mu) for v in g], 0.55, color=BLUE, label="From the tyres")
ax.bar(range(3), [max(v - mu, 0) for v in g], 0.55, bottom=[min(v, mu) for v in g], color=ORANGE, label="From the thrusters")
for i, v in enumerate(g):
    ax.text(i, v + 0.06, f"{v:.2f} g", ha="center", fontsize=9)
ax.axhline(mu, color=INK2, ls="--", lw=1); ax.text(-0.42, mu + 0.05, "Rough grip limit of a road tyre", fontsize=7.5, color=INK2)
ax.set_xticks(range(3)); ax.set_xticklabels(cases, fontsize=8); ax.set_ylabel("Average acceleration, g")
ax.set_ylim(0, 3.2); ax.grid(axis="x", visible=False); ax.legend(fontsize=8, loc="upper left", bbox_to_anchor=(0, 0.88))
ax.set_title("Why it needs rockets", fontsize=11)
ax = axes[1]
ax.bar(range(3), tank.tnt_equivalent_kg, 0.55, color=[YELLOW, ORANGE, RED])
for i, (b, r) in enumerate(tank.iterrows()):
    ax.text(i, r.tnt_equivalent_kg + 0.6, f"{r.tnt_equivalent_kg:.0f} kg TNT\n{r.launches_possible:.1f} launches", ha="center", fontsize=8.5)
ax.set_xticks(range(3)); ax.set_xticklabels([f"{b} bar" for b in tank.index]); ax.set_ylabel("Stored energy, kg of TNT equivalent")
ax.set_ylim(0, 31); ax.grid(axis="x", visible=False); ax.set_title("What 600 litres of compressed air holds", fontsize=11)
finish(fig, "Figure 4: The physics of a one second Roadster",
       "author's model 04; Tesla claims via TechCrunch and Fortune (Oct 2026); assumptions in the model description.", "fig04_roadster_physics.png")
print(res.round(2)); print(tank.round(1))
