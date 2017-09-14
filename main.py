from draw import *

from signal import *

N = 512


def frequencies_plot():
    frequencies = [5, 4, 2, 6, 3]
    params = [(3, pi / 2, x) for x in frequencies]
    draw_plots(r'f', harmonic_signal, params, N, 2)


def phases_plot():
    phases = [0, pi, pi / 6, pi / 4, pi / 2]
    params = [(10, x, 2) for x in phases]
    draw_plots(r'p', harmonic_signal, params, N, 1)


def amplitudes_plot():
    amplitudes = [2, 3, 6, 5, 1]
    params = [(x, pi / 2, 1) for x in amplitudes]
    draw_plots(r'a', harmonic_signal, params, N, 0)


def polyharmonic_linear_plot():
    plt.plot(list(polyharmonic_linear_signal(10, 0, 2, N)))


def polyharmonic_plot():
    params = [
        (1, 0, 1),
        (1, pi / 4, 2),
        (1, pi / 6, 3),
        (1, 2 * pi, 4),
        (1, pi, 5)
    ]
    draw_polyharmonic(polyharmonic_signal, params, N)


if __name__ == '__main__':
    results = []
    for i, plot in enumerate([phases_plot, frequencies_plot, amplitudes_plot, polyharmonic_linear_plot]):
        plt.subplot(2, 2, i + 1)
        results.append(plot())
    results.append(polyharmonic_plot())
    plt.show()
