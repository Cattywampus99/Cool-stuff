import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

def fourier_drawing_from_points(points, n_terms=200):
    """
    Perform Fourier drawing on a set of (x, y) points.
    :param points: list of (x, y) tuples
    :param n_terms: number of Fourier terms to use
    :return: reconstructed path as complex array
    """
    z = np.array([x + 1j*y for x, y in points])
    N = len(z)

    # FFT to get complex Fourier coefficients
    Z = fft(z)
    freqs = np.fft.fftfreq(N)

    # Sort indices by amplitude
    indices = np.argsort(-np.abs(Z))

    # Select top n_terms
    terms = [(freqs[i], Z[i]/N) for i in indices[:n_terms]]

    # Time parameter for reconstruction
    t = np.linspace(0, 1, N)
    path = []
    for ti in t:
        z_sum = sum(c * np.exp(2j * np.pi * f * ti) for f, c in terms)
        path.append(z_sum)

    return np.array(path), z  # return original complex path too for reference

def plot_drawing(reconstructed, original=None):
    plt.figure(figsize=(8, 8))
    if original is not None:
        plt.plot(original.real, original.imag, 'ro', markersize=1, alpha=0.4, label='Original Points')
    plt.plot(reconstructed.real, reconstructed.imag, 'b-', linewidth=2, label='Fourier Approximation')
    plt.title('Fourier Drawing')
    plt.axis('equal')
    plt.grid(True)
    plt.legend()
    plt.show()

# ✏️ Input your points here (x, y)
points = [
    (0, 0), (1, 2), (2, 3), (3, 5), (4, 4), (5, 2), (6, 0),
    (7, -2), (8, -3), (9, -1), (10, 0)  # You can enter hundreds or thousands of points
]

# Run Fourier drawing
reconstructed, original = fourier_drawing_from_points(points, n_terms=50)
plot_drawing(reconstructed, original)
