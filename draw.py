import matplotlib.pyplot as plt


def draw_plots(title, signal_func, params_tuples, n, pos):
    for params in params_tuples:
        plt.plot(list(signal_func(*params, n)),
                 label='${}={}$'.format(title, round(params[pos], 2)))
    plt.legend(loc='center left')


def draw_polyharmonic(signal_func, params, n):
    fig = plt.figure()
    plt.subplots_adjust(bottom=0.3)

    plot, = plt.plot(list(signal_func(params, n)))
    plt.ylim([-5, 5])
