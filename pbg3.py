import numpy as np
import matplotlib.pyplot as plt

def stock_price_sim(S0, mu, sigma, T=1, N=252, simulations=1000):
    """
    S0: Initial stock price
    mu: Expected return
    sigma: Volatility
    T: Time horizon (years)
    N: Number of time steps
    simulations: Number of paths
    """
    dt = T/N
    paths = np.zeros((simulations, N+1))
    paths[:, 0] = S0
    
    for t in range(1, N+1):
        z = np.random.standard_normal(simulations)
        paths[:, t] = paths[:, t-1] * np.exp((mu - 0.5*sigma**2)*dt + sigma*np.sqrt(dt)*z)
    
    # Plot first 50 paths
    plt.figure(figsize=(10,6))
    plt.plot(paths[:50].T)
    plt.title(f"Monte Carlo Stock Price Simulation\nμ={mu}, σ={sigma}")
    plt.xlabel("Time Steps")
    plt.ylabel("Stock Price")
    plt.show()
    
    # Calculate statistics
    final_prices = paths[:, -1]
    print(f"Expected Price: ${np.mean(final_prices):.2f}")
    print(f"5% VaR: ${np.percentile(final_prices, 5):.2f}")
    print(f"95% VaR: ${np.percentile(final_prices, 95):.2f}")

# Example usage
stock_price_sim(S0=100, mu=0.08, sigma=0.2, T=1, simulations=1000)