import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Функція для інтегрування
def f(x):
    return x**2

# Межі інтегрування
a, b = 0, 2

# === Метод Монте-Карло ===
def monte_carlo_integral(f, a, b, n=1000000):
    x = np.random.uniform(a, b, n)
    fx = f(x)
    estimate = (b - a) * fx.mean()
    return estimate

if __name__ == "__main__":
    # Обчислення методом Монте-Карло
    mc_result = monte_carlo_integral(f, a, b, n=1000000)

    # Перевірка через scipy.quad
    quad_result, quad_error = spi.quad(f, a, b)

    # Аналітичне значення: ∫ x^2 dx = x^3/3
    analytic = (b**3 - a**3) / 3

    # Вивід результатів
    print("Метод Монте-Карло:", mc_result)
    print("SciPy quad:", quad_result, "з оцінкою похибки:", quad_error)
    print("Аналітичний результат:", analytic)

    # Побудова графіка
    x = np.linspace(a - 0.5, b + 0.5, 400)
    y = f(x)

    fig, ax = plt.subplots()
    ax.plot(x, y, "r", linewidth=2)

    # Заштрихована область під кривою
    ix = np.linspace(a, b, 100)
    iy = f(ix)
    ax.fill_between(ix, iy, color="gray", alpha=0.3)

    ax.axvline(x=a, color="gray", linestyle="--")
    ax.axvline(x=b, color="gray", linestyle="--")

    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.set_title("Графік f(x) = x^2 від " + str(a) + " до " + str(b))
    plt.grid()
    plt.show()