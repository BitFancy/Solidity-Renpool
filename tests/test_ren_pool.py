def test_ren_mint(accounts, ren_token):
    """
    Test REN tokens are properly minted.
    """
    assert ren_token.balanceOf(accounts[0]) == 1e21

def test_ren_symbol(accounts, ren_token):
    """
    Test REN token has the correct symbol.
    """
    assert ren_token.symbol() == 'REN'

def test_ren_pool_deploy(accounts, ren_pool):
    """
    Test if the contract is correctly deployed.
    """
    assert ren_pool.owner() == accounts[0]
    assert ren_pool.totalPooled() == 0

def test_ren_pool_deposit(accounts, ren_pool, ren_token):
    """
    Test deposit.
    """
    DEPOSIT = 100
    assert ren_pool.totalPooled() == 0
    ren_token.approve(ren_pool.address, DEPOSIT, {'from': accounts[0]})
    ren_pool.deposit(DEPOSIT, {'from': accounts[0]})
    assert ren_token.balanceOf(ren_pool.address, {'from': accounts[0]}) == DEPOSIT
    assert ren_pool.balanceOf(accounts[0], {'from': accounts[0]}) == DEPOSIT
    assert ren_pool.totalPooled() == DEPOSIT

def test_ren_pool_withdraw(accounts, ren_pool, ren_token):
    """
    Test withdraw.
    """
    DEPOSIT = 100
    assert ren_pool.totalPooled() == 0
    ren_token.approve(ren_pool.address, DEPOSIT, {'from': accounts[0]})
    ren_pool.deposit(DEPOSIT, {'from': accounts[0]})
    assert ren_token.balanceOf(ren_pool.address, {'from': accounts[0]}) == DEPOSIT
    assert ren_pool.balanceOf(accounts[0], {'from': accounts[0]}) == DEPOSIT
    assert ren_pool.totalPooled() == DEPOSIT
    ren_pool.withdraw(DEPOSIT, {'from': accounts[0]})
    assert ren_pool.balanceOf(accounts[0], {'from': accounts[0]}) == 0
    assert ren_pool.totalPooled() == 0
    assert ren_token.balanceOf(ren_pool.address, {'from': accounts[0]}) == 0
