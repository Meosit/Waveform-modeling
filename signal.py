from math import pi, sin


def harmonic_value(amplitude, phase, frequency, n, iteration):
    return amplitude * sin((2 * pi * frequency * iteration) / n + phase)


def harmonic_signal(amplitude, phase, frequency, n):
    for i in range(n):
        yield harmonic_value(amplitude, phase, frequency, n, i)


def polyharmonic_linear_signal(amplitude, phase, frequency, n):
    def linear_function(x, i): return x * (1 + (i % n) * 0.00039)

    _amplitude, _phase, _frequency = amplitude, phase, frequency
    for i in range(n * 2):
        yield harmonic_value(_amplitude, _phase, _frequency, n, i % n)
        _phase = linear_function(phase, i)
        _amplitude = linear_function(amplitude, i)
        _frequency = linear_function(frequency, i)


def polyharmonic_signal(params_tuples, n):
    for i in range(n):
        def harmonic_func(amp, ph, freq): return harmonic_value(amp, ph, freq, n, i)

        yield sum((harmonic_value(*params, n, i) for params in params_tuples))
