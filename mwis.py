# third-party modules
import numpy as np
from numpy import ndarray

def divide_conquer(G: ndarray, p: int, q: int) -> ndarray:
    """Divide and conquer recursive implementation for solving MWIS problem for
    path graphs.
    ----------------------------------------------------------------------------
    Args:
        G: path graph represented as a numpy array of integers
        p: left bound
        q: right bound
    Returns:
        idxs: array of indices for elements in maximum weighted independent set"""
    if q - p <= 1: # terminal case
        return np.array(p).reshape(-1)
    # compute index for mid element
    mid = (q + p) // 2

    # solve and right subproblems
    idxs_left = divide_conquer(G, p, mid)
    idxs_right = divide_conquer(G, mid, q)

    # combine solutions
    if idxs_right[0] - idxs_left[-1] > 1:
        idxs = np.concatenate((idxs_left, idxs_right))
        return idxs
    else:
        # solve left subproblem without rightmost element
        if mid - 1 > p:
            combine_left = divide_conquer(G, p=p, q=mid-1)
            opt1 = np.concatenate((combine_left, idxs_right))
        else:
            opt1 = idxs_right
        # solve right subproblem without leftmost element
        if mid + 1 < q:
            combine_right = divide_conquer(G, p=mid+1, q=q)
            opt2 = np.concatenate((idxs_left, combine_right))
        else:
            opt2 = idxs_left
        # compute solution given by both options
        sum1 = np.sum(G[opt1])
        sum2 = np.sum(G[opt2]) 

        # compare solutions
        if sum1 >= sum2:
            return opt1
        else:
            return opt2

def dynamic_programming(G: ndarray):
    """Dynamic programming implementation for solving MWIS problem for path
    graphs.
    ----------------------------------------------------------------------------
    Args:
        G: path graph represented as a numpy array of integers
    Return:
        idxs: array of indices for elements in maximum weighted independent set"""
    n = len(G)
    dp = n * [None] # initialize DP table to None
    idxs = n * [None] # initialize list of indices
    dp[0] = G[0] # base case
    idxs[0] = [0]
    for i in range(1, n):
        sub = G[:i+1]
        opt1 = dp[i - 1] # not considering G[i]
        idx1 = idxs[i-1]
        if i - 2 >= 0:
            opt2 = dp[i - 2] + G[i] # considering G[i]
            idx2 = idxs[i - 2] + [i]
        else:
            opt2 = G[i] # there's only one element in the left array
            idx2 = [i]
        # store solution inside DP table
        dp[i] = opt1 if opt2 <= opt1 else opt2
        idxs[i] = idx1 if opt2 <= opt1 else idx2

    return idxs[-1]
