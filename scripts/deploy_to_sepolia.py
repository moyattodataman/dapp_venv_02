from brownie import token, accounts

def main():
    token.deploy(10000, {'from': accounts.load('account_1')})