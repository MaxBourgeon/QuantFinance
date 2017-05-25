import numpy
import numpy.random as nrand


def vol(returns):
    # Return the standard deviation of returns
    return numpy.std(returns)


def beta(returns, market):
    # Create a matrix of [returns, market]
    m = numpy.matrix([returns, market])
    # Return the covariance of m divided by the standard deviation of the market returns
    return numpy.cov(m)[0][1] / numpy.std(market)


# Example usage
r = nrand.uniform(-1, 1, 50)
m = nrand.uniform(-1, 1, 50)
print("vol =", vol(r))
print("beta =", beta(r, m))