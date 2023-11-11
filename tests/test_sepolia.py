import pytest
from brownie import accounts, token

CONTRACT_ADDRESS = "Sepoliaにデプロイしたスマートコントラクトのコントラクトアドレス"
account_1 = accounts.load("account_1")
account_2 = "MetaMaskのアカウント2"


def test_transfer():
    contract = token.at(CONTRACT_ADDRESS)

    balance_1 = contract.balances(account_1)
    balance_2 = contract.balances(account_2)
    
    tx = contract.transfer(account_2, 100, {'from': account_1})

    assert contract.balances(account_1) == balance_1 - 100
    assert contract.balances(account_2) == balance_2 + 100

    assert tx.events["Transfer"][0]["sender"] == account_1
    assert tx.events["Transfer"][0]["receiver"] == account_2
    assert tx.events["Transfer"][0]["value"] == 100


def test_transfer_reverts():
    contract = token.at(CONTRACT_ADDRESS)

    balance_1 = contract.balances(account_1)
    balance_2 = contract.balances(account_2)

    with pytest.raises(Exception):
        tx = contract.transfer(account_2, balance_1 + 1, {'from': account_1})

    assert contract.balances(account_1) == balance_1
    assert contract.balances(account_2) == balance_2