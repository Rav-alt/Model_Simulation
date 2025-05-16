import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon, norm, poisson, binom, triang, lognorm, gamma, beta, weibull_min, uniform


plt.figure(figsize=(15, 20))
plt.suptitle("Family of Distributions for Input Data Modeling", fontsize=16, y=1.02)

#Exponential Distribution
plt.subplot(5, 2, 1)
x = np.linspace(0, 5, 100)
plt.plot(x, expon.pdf(x, scale=1/0.5), 'r-', lw=2)
plt.title('Exponential (λ=0.5)')
plt.xlabel('Time between events')
plt.ylabel('PDF')

#Normal Distribution
plt.subplot(5, 2, 2)
x = np.linspace(-5, 5, 100)
plt.plot(x, norm.pdf(x, 0, 1), 'b-', lw=2)
plt.title('Normal (μ=0, σ=1)')
plt.xlabel('Value')
plt.ylabel('PDF')

#Poisson Distribution
plt.subplot(5, 2, 3)
x = np.arange(0, 15)
plt.bar(x, poisson.pmf(x, mu=3), color='green')
plt.title('Poisson (λ=3)')
plt.xlabel('Number of events')
plt.ylabel('PMF')

#Binomial Distribution
plt.subplot(5, 2, 4)
x = np.arange(0, 11)
plt.bar(x, binom.pmf(x, n=10, p=0.5), color='orange')
plt.title('Binomial (n=10, p=0.5)')
plt.xlabel('Successes')
plt.ylabel('PMF')

#Triangular Distribution
plt.subplot(5, 2, 5)
x = np.linspace(2, 8, 100)
plt.plot(x, triang.pdf(x, loc=2, scale=6, c=0.5), 'purple', lw=2)
plt.title('Triangular (min=2, mode=5, max=8)')
plt.xlabel('Value')
plt.ylabel('PDF')

#Lognormal Distribution
plt.subplot(5, 2, 6)
x = np.linspace(0, 5, 100)
plt.plot(x, lognorm.pdf(x, s=0.5, scale=np.exp(0)), 'cyan', lw=2)
plt.title('Lognormal (μ=0, σ=0.5)')
plt.xlabel('Value')
plt.ylabel('PDF')

#Gamma Distribution
plt.subplot(5, 2, 7)
x = np.linspace(0, 10, 100)
plt.plot(x, gamma.pdf(x, a=2, scale=2), 'magenta', lw=2)
plt.title('Gamma (k=2, θ=2)')
plt.xlabel('Value')
plt.ylabel('PDF')

#Beta Distribution
plt.subplot(5, 2, 8)
x = np.linspace(0, 1, 100)
plt.plot(x, beta.pdf(x, a=2, b=5), 'brown', lw=2)
plt.title('Beta (α=2, β=5)')
plt.xlabel('Value')
plt.ylabel('PDF')

#Weibull Distribution
plt.subplot(5, 2, 9)
x = np.linspace(0, 5, 100)
plt.plot(x, weibull_min.pdf(x, c=1.5, scale=1), 'pink', lw=2)
plt.title('Weibull (k=1.5, λ=1)')
plt.xlabel('Time')
plt.ylabel('PDF')

#Uniform Distribution
plt.subplot(5, 2, 10)
x = np.linspace(1, 6, 100)
plt.plot(x, uniform.pdf(x, loc=1, scale=5), 'gray', lw=2)
plt.title('Uniform (a=1, b=6)')
plt.xlabel('Value')
plt.ylabel('PDF')

plt.tight_layout()
plt.savefig('all_distributions.png', dpi=300, bbox_inches='tight')
plt.show()