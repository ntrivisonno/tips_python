"""
Script that computes de Convergency Error for different refinaments

Meshes readed form meshes dict, supports variable size

$python3 convergencyPlot.py
"""
import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

plt.close('all')

# Data for multiple meshes
meshes = {
    "DynaMesh": {
        "divisions": np.array([4, 8, 16, 32, 64]), # dx: 10,20,40,80,160 ~/dynaMesh/OpenFOAM/run/S53-S54-S55-S56-S57
        "RMS_Ux": np.array([0.1903510099269464, 0.009918428220705143, 0.002100265592300084, 0.0004956942976506593, 0.0001225514854043294]),
        "RMS_Uy": np.array([0.1945676464798565, 0.009301347473562547, 0.001879838126173432, 0.0004715239549622438, 0.0001181141375924694])
    },
    "Malla2": {
        "divisions": np.array([4, 8, 16]), # dx: 10,20,40,80,160 ~/dynaMesh/OpenFOAM/run/S53-S54-S55-S56-S57
        "RMS_Ux": np.array([0.1903510099269464, 0.009918428220705143, 0.002100265592300084]),
        "RMS_Uy": np.array([0.1945676464798565, 0.009301347473562547, 0.001879838126173432])
    }
}

# Initialize plot for subplots of RMS_Ux, RMS_Uy, and Error Magnitude
fig, axs = plt.subplots(1, 3, figsize=(18, 6))

# Store convergence rates and error magnitudes for table
convergence_rates = []
error_magnitudes = []

# Separate figure for Error Magnitude
fig_normError, ax_normError = plt.subplots(figsize=(18,12))#(figsize=(12, 10))
fig_normError.suptitle('Log-Log Error Magnitude vs Refinement')

# Plotting
for mesh_name, data in meshes.items():
    divisions = data["divisions"]
    RMS_Ux = data["RMS_Ux"]
    RMS_Uy = data["RMS_Uy"]

    # Compute log-log values
    log_divisions = np.log2(divisions)
    log_RMS_Ux = np.log2(RMS_Ux)
    log_RMS_Uy = np.log2(RMS_Uy)

    # Calculate convergence rates
    rate_Ux = [np.log2(RMS_Ux[i + 1] / RMS_Ux[i]) for i in range(len(RMS_Ux) - 1)]
    rate_Uy = [np.log2(RMS_Uy[i + 1] / RMS_Uy[i]) for i in range(len(RMS_Uy) - 1)]

    # Calculate error magnitudes
    error_magnitude = np.sqrt(RMS_Ux**2 + RMS_Uy**2)

    # Calculate convergence rates for error magnitude
    rate_err = [np.log2(error_magnitude[i + 1] / error_magnitude[i]) for i in range(len(error_magnitude) - 1)]

    # Store rates and error magnitudes for table
    convergence_rates.append([mesh_name, rate_Ux, rate_Uy, rate_err])
    error_magnitudes.append([mesh_name, error_magnitude])

    # Plot RMS Ux
    axs[0].plot(log_divisions, log_RMS_Ux, marker='o', label=f'RMS Ux {mesh_name}')
    for i in range(len(divisions)):
        axs[0].text(log_divisions[i], log_RMS_Ux[i], f'({divisions[i]}, {RMS_Ux[i]:.2e})')

    # Plot RMS Uy
    axs[1].plot(log_divisions, log_RMS_Uy, marker='o', label=f'RMS Uy {mesh_name}')
    for i in range(len(divisions)):
        axs[1].text(log_divisions[i], log_RMS_Uy[i], f'({divisions[i]}, {RMS_Uy[i]:.2e})')

    # Plot Error Magnitude
    log_error_magnitude = np.log2(error_magnitude)
    axs[2].plot(log_divisions, log_error_magnitude, marker='o', label=f'Error Magnitude {mesh_name}')
    for i in range(len(divisions)):
        axs[2].text(log_divisions[i], log_error_magnitude[i], f'({divisions[i]}, {error_magnitude[i]:.2e})')

    # Plot Error Magnitude in separate figure
    ax_normError.plot(log_divisions, log_error_magnitude, marker='o', label=f'Error Magnitude {mesh_name}')
  
    for i in range(len(divisions)):
        ax_normError.text(log_divisions[i], log_error_magnitude[i], f'({divisions[i]}, {error_magnitude[i]:.2e})')

# Reference lines for all subplots
offset = 1  # Offset to avoid overlapping
for ax in axs:
    x_ref = np.array([log_divisions[0], log_divisions[-1]])
    y_ref_1 = np.array([log_RMS_Ux[0] - offset, log_RMS_Ux[0] - offset - (log_divisions[-1] - log_divisions[0])])
    y_ref_2 = np.array([log_RMS_Ux[0] - offset, log_RMS_Ux[0] - offset - 2 * (log_divisions[-1] - log_divisions[0])])
    ax.plot([x_ref[0], x_ref[1]], [y_ref_1[0], y_ref_1[1]], 'k--', label='Slope -1')
    ax.plot([x_ref[0], x_ref[1]], [y_ref_2[0], y_ref_2[1]], 'g--', label='Slope -2')
    ax.grid(True)
    ax.legend()

# Titles and labels for subplots
titles = ['Log-Log Plot of RMS Ux vs Refinements', 'Log-Log Plot of RMS Uy vs Refinements', 'Log-Log Plot of Error Magnitude vs Refinements']
ylabels = ['log2(RMS Ux)', 'log2(RMS Uy)', 'log2(Error Magnitude)']

for i, ax in enumerate(axs):
    ax.set_title(titles[i])
    ax.set_xlabel('log2(divisions)')
    ax.set_ylabel(ylabels[i])

plt.tight_layout()

# Create table
table = []
for rates in convergence_rates:
    mesh_name, rate_Ux, rate_Uy, rate_err = rates
    for i in range(len(rate_Ux)):
        table.append([mesh_name, f'R{i + 1}', rate_Ux[i], rate_Uy[i], rate_err[i]])

# Headers for the table
headers = ['Mesh', 'Refinement', 'Convergence Rate Ux', 'Convergence Rate Uy', 'Convergence Rate Error Magnitude']

# Show table
print(tabulate(table, headers, tablefmt="grid"))


# Plot reference lines in the separate figure for Error Magnitude
x_ref = np.array([log_divisions[0], log_divisions[-1]])
y_ref_1 = np.array([log_error_magnitude[0] - offset, log_error_magnitude[0] - offset - (log_divisions[-1] - log_divisions[0])])
y_ref_2 = np.array([log_error_magnitude[0] - offset, log_error_magnitude[0] - offset - 2 * (log_divisions[-1] - log_divisions[0])])
ax_normError.plot([x_ref[0], x_ref[1]], [y_ref_1[0], y_ref_1[1]], 'k--', label='Slope -1')
ax_normError.plot([x_ref[0], x_ref[1]], [y_ref_2[0], y_ref_2[1]], 'g--', label='Slope -2')

ax_normError.set_xlabel('log2(divisions)')
ax_normError.set_ylabel('log2(Error Magnitude)')
ax_normError.grid(True)
ax_normError.legend()

fig_normError.tight_layout()
#fig_normError.savefig('ErrorConvergenceDynaMesh.pdf')

print('#--------------------------------------------')
print('\n FIN, OK!')
plt.show()
