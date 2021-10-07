from brownie import ZERO_ADDRESS
from utils import base58_to_hex

DECIMALS = 18

TENS = 10 ** DECIMALS

INITIAL_SUPPLY = 1000_000_000 * TENS

POOL_BOND = 100_000 * TENS

FAUCET_AMOUNT = 1000 * TENS

NETWORKS = {
  'MAINNET': 'mainnet',
  'MAINNET_FORK': 'mainnet-fork',
  'KOVAN': 'kovan',
  'DEVELOPMENT': 'development',
}

CONTRACT_ADDRESSES = {
  NETWORKS['MAINNET']: {
    'REN_TOKEN': '0x408e41876cCCDC0F92210600ef50372656052a38',
    'DARKNODE_REGISTRY': '0x2D7b6C95aFeFFa50C068D50f89C5C0014e054f0A',
    'DARKNODE_REGISTRY_STORE': '0x60Ab11FE605D2A2C3cf351824816772a131f8782',
  },
  NETWORKS['MAINNET_FORK']: {
    'REN_TOKEN': '0x408e41876cCCDC0F92210600ef50372656052a38',
    'DARKNODE_REGISTRY': '0x2D7b6C95aFeFFa50C068D50f89C5C0014e054f0A',
    'DARKNODE_REGISTRY_STORE': '0x60Ab11FE605D2A2C3cf351824816772a131f8782',
		'CLAIM_REWARDS': ZERO_ADDRESS,
		'GATEWAY': ZERO_ADDRESS,
  },
  NETWORKS['KOVAN']: {
    'REN_TOKEN': '0x2CD647668494c1B15743AB283A0f980d90a87394',
    'DARKNODE_REGISTRY': '0x9954C9F839b31E82bc9CA98F234313112D269712',
    'DARKNODE_REGISTRY_STORE': '0x9daa16aA19e37f3de06197a8B5E638EC5e487392',
		'CLAIM_REWARDS': '0x7F8f7Aff44a63f61b7a120Ef2c34Ea2c4D9bD216',
		'GATEWAY': ZERO_ADDRESS,
  },
}

NODE_ID = '8MHJ9prQt7UGupfZKSMVes3VzPrGBB' # In base58
NODE_ID_2 = '8MHJ9prQt7UGupfZKSMVes3VzPrGB1' # In base58

NODE_ID_HEX = base58_to_hex(NODE_ID)
NODE_ID_2_HEX = base58_to_hex(NODE_ID_2)

PUBLIC_KEY = '0x000000077373682d727361000000030100010000010100d0feba4ae65ea9ad771d153419bcc21189d954b6bf75fd5488055cd2641231014f190c0e059a452d301c535e931df33590ec0e18c59341a2766cc885d1dc6e66f5cc65b94522ec944ae4200bd56a30223328b258d50b507dd94b4c4742768f3fec2b815c9c4b0fe26727e82865f6a064fa3ff2443d135d9788095a1c17487fd5c389a491c16b73385d516a303debc3bcccae337a7ec0d89d51ce05262a0c4c1f2178466c85379b8cd4e5cbe1c90a05fb0c1ed3eee2134774b450e7b0b70c792abad55beef919e21a03cb9de4e963a820c2f84421a4559d0b67cfd17c1686ff6f2d1bb07ac2c82cede1cf5f16a57e125a29fef65891715b061606bca1a0eb026b'
PUBLIC_KEY_2 = '0x000000077373682d727361000000030100010000010100d0feba4ae65ea9ad771d153419bcc21189d954b6bf75fd5488055cd2641231014f190c0e059a452d301c535e931df33590ec0e18c59341a2766cc885d1dc6e66f5cc65b94522ec944ae4200bd56a30223328b258d50b507dd94b4c4742768f3fec2b815c9c4b0fe26727e82865f6a064fa3ff2443d135d9788095a1c17487fd5c389a491c16b73385d516a303debc3bcccae337a7ec0d89d51ce05262a0c4c1f2178466c85379b8cd4e5cbe1c90a05fb0c1ed3eee2134774b450e7b0b70c792abad55beef919e21a03cb9de4e963a820c2f84421a4559d0b67cfd17c1686ff6f2d1bb07ac2c82cede1cf5f16a57e125a29fef65891715b061606bca1a0eb026c' # Last character has been modified

ONE_MONTH = 60 * 60 * 24 * 31
