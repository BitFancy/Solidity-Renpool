# @version >=0.2.7 <0.3.0

# TODO: what happens in case of the pool being slashed?
# TODO: Earnings distribution
# TODO: Node fees
# TODO: Do we need to store the node/server id? And or we pass said value to the REN protocol on node submission
# Question: do we need to mint REN tokens to test the contract?
# MintableForkToken to create test REN? (brownie). source: https://www.youtube.com/watch?v=jh9AuCfw6Ck
# Watch video on how to mint dai and usdc https://www.youtube.com/watch?v=0JrDbvBClEA
# Question: should we have a single vault/pool where we send all the tokens (even if surpassing the 100.000 mark)?
# Or it'd be better to have mini pools of 100.000 tokens each or a single pool of 100.000 to get started?

# Constants
LIMIT: constants(uint256) = 100000 # amount of REN required to set a node

# Variables
owner: public(address)
balances: public(HashMap[address, uint256])
totalBalance: public(uint256)
fee: public(uint256) # pool's fee percentage

# Events
event RenDeposited:
    user: indexed(address)
    amount: uint256
    time: uint256

event RenWithdrawn:
    user: indexed(address)
    amount: uint256
    time: uint256

event PoolLimitReached:
    time: uint256

# Class
@external
def __init__():
    self.owner = msg.sender
    self.fee = 10
    self.totalBalance = 0

@external
@payable
def deposit():
    user: indexed(address) = msg.sender # TODO: do we need index here?
    amount: uint256 = convert(msg.value, uint256) # TODO: can we assert msg.value to be uint instead?

    assert amount > 0, "Amount must be positive"
    assert amount + self.totalBalance <= LIMIT, "Amount surpasses pool limit"

    # TODO: make sure REN token is being transferred and not any other ERC20 token
    balances[user] += amount # uint256 is set to zero by default
    totalBalance += amount

    log RenDeposited(user, amount, now)
    if totalBalance == LIMIT:
        log PoolLimitReached(now)

@external
@view
def withdraw(_amount: uint256):
    user: address = msg.sender
    balance: uint256 = balances[user]

    assert balance > 0 and balance <= _amount, "Insufficient balance"

    balances[user] -= _amount
    send(user, _amount) # TODO: actually, we should add the request to the queue and only perform the withdraw when there is another user whilling to take it's place

    log RenWithdrawn(user, amount, now)

@external
@view
def balanceOf(_user: address) -> uint256:
    return balances[_user]
}

# TODO add fallback function to receive ETH on case we need to pay for transaction fees or whatever
