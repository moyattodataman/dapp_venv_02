import pytest
from brownie import accounts, token


def test_transfer():
    contract = token.deploy(10000, {'from': accounts[1]})

    tx = contract.transfer(accounts[2], 100, {'from': accounts[1]})

    assert contract.balances(accounts[1]) == 9900
    assert contract.balances(accounts[2]) == 100

    assert tx.events["Transfer"][0]["sender"] == accounts[1]
    assert tx.events["Transfer"][0]["receiver"] == accounts[2]
    assert tx.events["Transfer"][0]["value"] == 100


def test_transfer_reverts():
    contract = token.deploy(10000, {'from': accounts[1]})

    with pytest.raises(Exception):
        tx = contract.transfer(accounts[2], 10001, {'from': accounts[1]})

    assert contract.balances(accounts[1]) == 10000
    assert contract.balances(accounts[2]) == 0