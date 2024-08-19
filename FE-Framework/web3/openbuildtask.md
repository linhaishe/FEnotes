# task 3

## 1. 部署

1. erc20token.sol
2. erc721.sol
3. nft-market.sol

币创造者：0x5B38Da6a701c568545dCfcB03FcB875f56beddC4

0xd7fC917C41d27667343F22379d34E96974047Ae2

INITIALOWNER： 0x5B38Da6a701c568545dCfcB03FcB875f56beddC4

0xd7fC917C41d27667343F22379d34E96974047Ae2

操作人：0x5B38Da6a701c568545dCfcB03FcB875f56beddC4

0xd7fC917C41d27667343F22379d34E96974047Ae2

-----

erc20: 0x8ca254F8dBe77CD3d76D784D83aF13595566e91A

erc721(NFTM: 0x813BAeBAFB5AA1EFFF20A5537285E3E92FD84B1b

market: 0x5A8028042a4F29a867fbCD78836A11af1C92e563

## 2. 创造者A给用户B转两个nft，其实一个就行

id分别为0,1

走nftM(erc721)的safeMint函数

用户a: 0x5B38Da6a701c568545dCfcB03FcB875f56beddC4

​	用户b: 0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2

操作人：0x5B38Da6a701c568545dCfcB03FcB875f56beddC4

## 3. 上架nft

data参数：0x0000000000000000000000000000000000000000000000000001c6bf52634000

在nftM合约中(erc721)，走safeTransferFrom函数。

from拥有者to合约市场

操作者：0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2

上架hash: 0xcc41426cccd5e1843b20d35a723f7ef30a4140e4162f7bc76638190a1a80359a

![image-20240622202403700](https://s2.loli.net/2024/06/22/6ZW9KXyFqdYMl5v.png)

## 4. 改价格

in market

1e18 不要 ， 1就行

操作者：0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2

## 5. 购买

1. 授权Market， 操作者为创建者即：0x5B38Da6a701c568545dCfcB03FcB875f56beddC4
2. erc20 approval
3. Spender: market / value 1e33
4. 我这里好像是0wei购买的

购买hash: 0x7f9bb74636e12f2d597583ee4434fff8eeff06e5505f91da65c9d2d07ee7f880

---

# task 4 & 5

## 使用ethers.js和wagmi与NFTMarket合约交互
### 任务目标
使用ethers.js和wagmi库编写一个前端应用程序，允许用户上架NFT并使用ERC20代币购买NFT。
### 前端组件要求

1. 查看owned listing unlist状态

- 连接钱包：用户可以通过MetaMask连接他们的钱包。✅
- 上架NFT：用户可以输入NFT合约地址、Token ID和价格（ERC20代币），并将NFT上架到市场。✅
- 显示上架的NFT：显示所有上架的NFT，包括NFT的合约地址、Token ID、价格和卖家地址。✅
- 购买NFT：用户可以选择一个上架的NFT并使用ERC20代币进行购买。✅



拿到所有的nft，Home页面遍历展示 forsale的数据 和 alchemy 数据做并集，如果seller是当前用户则 unsell，否则 buy

owned 页面，自己的nft中的数据 + 和市场list数据，市场数据中找到seller是自己的，如果状态是upforsale那么按钮就是unsell+ alcmemy 中查到的信息（listing），如果状态是!upforsale &&  exist && !sold 那就listing

分为 listing 和 unlisting. 两部分

然后结合原有的list信息 形成新的数据数据结构，进行条件展示



### 提交要求
- 提交完整代码
- 提交界面截图

## 开发一个完整的NFTMarket的Dapp
### 任务目标
在task4基础上开发一个完整的NFTMarket-Dapp并对功能点进行测试
### 任务要求
- 合约增加一个==下架NFT==功能，用户可以在上架NFT后、被别人购买前下架NFT
- 在Market界面展示出所有上架的NFT（==图片==、NFT信息）
- NFT信息包括（价格、==上架时间==、拥有者）
- 测试上架、下架、购买NFT的功能
### 提交要求
- 提交完整代码
- 提交界面的截图
- 提交测试的截图（上架后、下架后、购买NFT后买家获得NFT的三个截图）

-----

an ERC 20 token can be created for transacting of ERC 721 type NFT on a custom marketplace contract.

可以创建一种ERC20代币，用于在一个定制的市场合约上进行ERC721类型NFT的交易。具体解释如下：

### 详细解释

1. **ERC20代币**：这是一种可替代的代币标准，用于代表同质化的资产。ERC20代币可以被分割和互换，每个单位的价值都是相同的。
2. **ERC721代币**：这是一种不可替代的代币标准，用于代表独特的资产，如艺术品、收藏品或游戏内物品。每个ERC721代币都是独一无二的，具有独特的属性和价值。
3. **定制市场合约**：这是一种智能合约，用于构建一个特定用途的交易平台。在这种情况下，这个平台是用于ERC721代币的交易。

### 整合和用途

在这个定制市场合约中，可以设计一种机制，使得用户能够使用ERC20代币来交易ERC721代币。具体操作可能包括以下几种方式：

1. **定价和支付**：在市场合约中，可以设定ERC721代币的价格以ERC20代币表示。买家使用ERC20代币支付来购买特定的ERC721代币。
2. **交易媒介**：ERC20代币可以作为交易的媒介，使得交易更加便捷和标准化。比如，用户可以使用一个常用的ERC20代币（如USDT）来购买和出售不同的ERC721代币。
3. **流动性和市场**：使用ERC20代币可以增加市场的流动性和便利性，因为ERC20代币具有更广泛的接受度和使用范围。

### 举例说明

假设我们有一个定制的市场平台（MarketPlaceContract），用户可以在这个平台上买卖NFT（ERC721代币）。我们决定使用某种ERC20代币（例如MyToken）作为交易媒介。

- **上架NFT**：卖家将他们的NFT上架到MarketPlaceContract，并设置一个价格，例如10 MyToken。
- **购买NFT**：买家在MarketPlaceContract上看到这个NFT，决定购买，并支付10 MyToken。
- **交易完成**：MarketPlaceContract从买家账户中扣除10 MyToken，将其转给卖家，同时将NFT的所有权从卖家转移给买家。

### 优势

- **标准化支付**：使用ERC20代币作为支付手段，可以实现更加标准化和便捷的支付流程。
- **灵活性**：卖家和买家可以自由选择不同的ERC20代币进行交易，提高交易的灵活性和便捷性。
- **流动性提升**：ERC20代币的广泛应用可以提升市场的流动性，使得交易更加活跃。

总之，这种设计使得在一个定制的市场合约上，可以通过创建和使用ERC20代币来促进ERC721代币（NFT）的交易。

1. 先搭建前端交互页面
2. 用wagmi，etherjs，写合约交互
   1. 登录/退出/连接钱包
   2. 上架NFT：用户可以输入NFT合约地址、Token ID和价格（ERC20代币），并将NFT上架到市场。
   3. 显示上架的NFT：显示所有上架的NFT，包括NFT的合约地址、Token ID、价格和卖家地址/图片。
   4. 购买NFT：用户可以选择一个上架的NFT并使用ERC20代币进行购买。
3. 提交此次代码
4. 增加测试
5. 增加下架等新功能
6. 提交代码



---

```
const axios = require('axios')
const FormData = require('form-data')
const fs = require('fs')
const JWT = eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySW5mb3JtYXRpb24iOnsiaWQiOiI4NzAyMmJjZC02OTA3LTRkZWUtOTE1Yi1hNjI3M2Q0ZDBlYmMiLCJlbWFpbCI6Inh1c3VtdUBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwicGluX3BvbGljeSI6eyJyZWdpb25zIjpbeyJpZCI6IkZSQTEiLCJkZXNpcmVkUmVwbGljYXRpb25Db3VudCI6MX0seyJpZCI6Ik5ZQzEiLCJkZXNpcmVkUmVwbGljYXRpb25Db3VudCI6MX1dLCJ2ZXJzaW9uIjoxfSwibWZhX2VuYWJsZWQiOmZhbHNlLCJzdGF0dXMiOiJBQ1RJVkUifSwiYXV0aGVudGljYXRpb25UeXBlIjoic2NvcGVkS2V5Iiwic2NvcGVkS2V5S2V5IjoiMTVhOGZkMmE4MTFlOThkYzRlMjgiLCJzY29wZWRLZXlTZWNyZXQiOiI2ODJmMzZiY2I0YzRjNTU2M2JiODIyYmU2ZTAxZGNlMjJhNWQyZDY4NzdiNjM1YWIxNWUwNmZlOWE4ZjJhM2YzIiwiaWF0IjoxNzE5NDk0NDQzfQ.VzIdn5-QTSwBsc0VkEd3VA8Xz8pwwMci6gzz20wlc2M

const pinFileToIPFS = async () => {
    const formData = new FormData();
    const src = "path/to/file.png";

    const file = fs.createReadStream(src)
    formData.append('file', file)

    const pinataMetadata = JSON.stringify({
      name: 'File name',
    });
    formData.append('pinataMetadata', pinataMetadata);

    const pinataOptions = JSON.stringify({
      cidVersion: 0,
    })
    formData.append('pinataOptions', pinataOptions);

    try{
      const res = await axios.post("https://api.pinata.cloud/pinning/pinFileToIPFS", formData, {
        maxBodyLength: "Infinity",
        headers: {
          'Content-Type': `multipart/form-data; boundary=${formData._boundary}`,
          'Authorization': `Bearer ${JWT}`
        }
      });
      console.log(res.data);
    } catch (error) {
      console.log(error);
    }
}
pinFileToIPFS()

```

```
// approvalRes

{
    "to": "0x7b4a0AF79B11d65ff6a21450E053Fd73D3a9107e",
    "from": "0xd7fC917C41d27667343F22379d34E96974047Ae2",
    "contractAddress": null,
    "transactionIndex": 35,
    "gasUsed": {
        "type": "BigNumber",
        "hex": "0xb63b"
    },
    "logsBloom": "0x00000000000020001000000000000000000000000000000000000000000000000000000000000000000000000000080000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002000000000000080000000000000000000000000000000000000000000000000000000000000000000000000002000000000200000000000000000000000040000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000200800000080000000000000040000000000000000000000000000000000",
    "blockHash": "0x9c5f525e83c66d3fcc9d4629b53f83c75111ee7092478002969e361249c2f0db",
    "transactionHash": "0x55557bfcfa292556da56cd8b932ba36d534fad35b6e80c7ae067cc6bcfb1fc00",
    "logs": [
        {
            "transactionIndex": 35,
            "blockNumber": 6225619,
            "transactionHash": "0x55557bfcfa292556da56cd8b932ba36d534fad35b6e80c7ae067cc6bcfb1fc00",
            "address": "0x7b4a0AF79B11d65ff6a21450E053Fd73D3a9107e",
            "topics": [
                "0x17307eab39ab6107e8899845ad3d59bd9653f200f220920489ca2b5937696c31",
                "0x000000000000000000000000d7fc917c41d27667343f22379d34e96974047ae2",
                "0x0000000000000000000000005c48d4fca7065cf7e79b905ddd3dc773fa3da4de"
            ],
            "data": "0x0000000000000000000000000000000000000000000000000000000000000001",
            "logIndex": 66,
            "blockHash": "0x9c5f525e83c66d3fcc9d4629b53f83c75111ee7092478002969e361249c2f0db"
        }
    ],
    "blockNumber": 6225619,
    "confirmations": 1,
    "cumulativeGasUsed": {
        "type": "BigNumber",
        "hex": "0x540d7b"
    },
    "effectiveGasPrice": {
        "type": "BigNumber",
        "hex": "0x2b6ac77e76"
    },
    "status": 1,
    "type": 2,
    "byzantium": true,
    "events": [
        {
            "transactionIndex": 35,
            "blockNumber": 6225619,
            "transactionHash": "0x55557bfcfa292556da56cd8b932ba36d534fad35b6e80c7ae067cc6bcfb1fc00",
            "address": "0x7b4a0AF79B11d65ff6a21450E053Fd73D3a9107e",
            "topics": [
                "0x17307eab39ab6107e8899845ad3d59bd9653f200f220920489ca2b5937696c31",
                "0x000000000000000000000000d7fc917c41d27667343f22379d34e96974047ae2",
                "0x0000000000000000000000005c48d4fca7065cf7e79b905ddd3dc773fa3da4de"
            ],
            "data": "0x0000000000000000000000000000000000000000000000000000000000000001",
            "logIndex": 66,
            "blockHash": "0x9c5f525e83c66d3fcc9d4629b53f83c75111ee7092478002969e361249c2f0db",
            "args": [
                "0xd7fC917C41d27667343F22379d34E96974047Ae2",
                "0x5C48D4fcA7065cf7e79B905ddd3dC773fA3dA4de",
                true
            ],
            "event": "ApprovalForAll",
            "eventSignature": "ApprovalForAll(address,address,bool)"
        }
    ]
}
```

```
approvesRsp

{
    "to": "0x0078f766CCa2876da1F43cC6743b32F5f577C0c8",
    "from": "0xd7fC917C41d27667343F22379d34E96974047Ae2",
    "contractAddress": null,
    "transactionIndex": 49,
    "gasUsed": {
        "type": "BigNumber",
        "hex": "0xb709"
    },
    "logsBloom": "0x00000000000020001000000000000000000000000000000000000000000000000000000000000000000000000000080000020000000000000000000000200000000000000000000000000000000000000000000040000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002000000000200000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000010000000000080000000000000000000000000000000000000000000000000",
    "blockHash": "0x09f70077b057644a7b09ecaf165f8f21dd03c517c37787e7fa49500a81d8d6a3",
    "transactionHash": "0xc2a2239a584848db588909ed8a61883180befb692d54e01d13f46c2b2a1551c8",
    "logs": [
        {
            "transactionIndex": 49,
            "blockNumber": 6225878,
            "transactionHash": "0xc2a2239a584848db588909ed8a61883180befb692d54e01d13f46c2b2a1551c8",
            "address": "0x0078f766CCa2876da1F43cC6743b32F5f577C0c8",
            "topics": [
                "0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925",
                "0x000000000000000000000000d7fc917c41d27667343f22379d34e96974047ae2",
                "0x0000000000000000000000005c48d4fca7065cf7e79b905ddd3dc773fa3da4de"
            ],
            "data": "0x000000000000000000000000000000000000000000000000000000000000000b",
            "logIndex": 99,
            "blockHash": "0x09f70077b057644a7b09ecaf165f8f21dd03c517c37787e7fa49500a81d8d6a3"
        }
    ],
    "blockNumber": 6225878,
    "confirmations": 2,
    "cumulativeGasUsed": {
        "type": "BigNumber",
        "hex": "0x65c154"
    },
    "effectiveGasPrice": {
        "type": "BigNumber",
        "hex": "0x1aa6b0276d"
    },
    "status": 1,
    "type": 2,
    "byzantium": true,
    "events": [
        {
            "transactionIndex": 49,
            "blockNumber": 6225878,
            "transactionHash": "0xc2a2239a584848db588909ed8a61883180befb692d54e01d13f46c2b2a1551c8",
            "address": "0x0078f766CCa2876da1F43cC6743b32F5f577C0c8",
            "topics": [
                "0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925",
                "0x000000000000000000000000d7fc917c41d27667343f22379d34e96974047ae2",
                "0x0000000000000000000000005c48d4fca7065cf7e79b905ddd3dc773fa3da4de"
            ],
            "data": "0x000000000000000000000000000000000000000000000000000000000000000b",
            "logIndex": 99,
            "blockHash": "0x09f70077b057644a7b09ecaf165f8f21dd03c517c37787e7fa49500a81d8d6a3",
            "args": [
                "0xd7fC917C41d27667343F22379d34E96974047Ae2",
                "0x5C48D4fcA7065cf7e79B905ddd3dC773fA3dA4de",
                {
                    "type": "BigNumber",
                    "hex": "0x0b"
                }
            ],
            "event": "Approval",
            "eventSignature": "Approval(address,address,uint256)"
        }
    ]
}
```

```
addItemToMarketRes

{
    "to": "0x5C48D4fcA7065cf7e79B905ddd3dC773fA3dA4de",
    "from": "0xd7fC917C41d27667343F22379d34E96974047Ae2",
    "contractAddress": null,
    "transactionIndex": 21,
    "gasUsed": {
        "type": "BigNumber",
        "hex": "0x044a56"
    },
    "logsBloom": "0x00000000000020001000000000000000000000000000000000000000000000000000000000000000000000000000080000020000000000000000000000240000000000000000000000000008000000000000000040040000000000000000000000000000020000080000000000000800000000000000000000000010000000000000000000200000000000000002000000000200000000000000000000000140020000000000000000000000000000000000000004000000000000000000000000000002000000000000010000000000000000000000000000200000000060000010000000000080000000000000040100000000000000000000000000000000",
    "blockHash": "0x2e816d7930aab9b0e387459da662789c9e069fb87d5bd684e6e3b3a0a23d2094",
    "transactionHash": "0xad28e8b80c5c2d1a88fd8f2fd88d3cf4bf4aa66db7cdfbe1c668531b46a0f3f0",
    "logs": [
        {
            "transactionIndex": 21,
            "blockNumber": 6225912,
            "transactionHash": "0xad28e8b80c5c2d1a88fd8f2fd88d3cf4bf4aa66db7cdfbe1c668531b46a0f3f0",
            "address": "0x0078f766CCa2876da1F43cC6743b32F5f577C0c8",
            "topics": [
                "0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925",
                "0x000000000000000000000000d7fc917c41d27667343f22379d34e96974047ae2",
                "0x0000000000000000000000005c48d4fca7065cf7e79b905ddd3dc773fa3da4de"
            ],
            "data": "0x000000000000000000000000000000000000000000000000000000000000000a",
            "logIndex": 20,
            "blockHash": "0x2e816d7930aab9b0e387459da662789c9e069fb87d5bd684e6e3b3a0a23d2094"
        },
        {
            "transactionIndex": 21,
            "blockNumber": 6225912,
            "transactionHash": "0xad28e8b80c5c2d1a88fd8f2fd88d3cf4bf4aa66db7cdfbe1c668531b46a0f3f0",
            "address": "0x0078f766CCa2876da1F43cC6743b32F5f577C0c8",
            "topics": [
                "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef",
                "0x000000000000000000000000d7fc917c41d27667343f22379d34e96974047ae2",
                "0x0000000000000000000000005c48d4fca7065cf7e79b905ddd3dc773fa3da4de"
            ],
            "data": "0x0000000000000000000000000000000000000000000000000000000000000001",
            "logIndex": 21,
            "blockHash": "0x2e816d7930aab9b0e387459da662789c9e069fb87d5bd684e6e3b3a0a23d2094"
        },
        {
            "transactionIndex": 21,
            "blockNumber": 6225912,
            "transactionHash": "0xad28e8b80c5c2d1a88fd8f2fd88d3cf4bf4aa66db7cdfbe1c668531b46a0f3f0",
            "address": "0x7b4a0AF79B11d65ff6a21450E053Fd73D3a9107e",
            "topics": [
                "0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925",
                "0x000000000000000000000000d7fc917c41d27667343f22379d34e96974047ae2",
                "0x0000000000000000000000000000000000000000000000000000000000000000",
                "0x0000000000000000000000000000000000000000000000000000000000000000"
            ],
            "data": "0x",
            "logIndex": 22,
            "blockHash": "0x2e816d7930aab9b0e387459da662789c9e069fb87d5bd684e6e3b3a0a23d2094"
        },
        {
            "transactionIndex": 21,
            "blockNumber": 6225912,
            "transactionHash": "0xad28e8b80c5c2d1a88fd8f2fd88d3cf4bf4aa66db7cdfbe1c668531b46a0f3f0",
            "address": "0x7b4a0AF79B11d65ff6a21450E053Fd73D3a9107e",
            "topics": [
                "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef",
                "0x000000000000000000000000d7fc917c41d27667343f22379d34e96974047ae2",
                "0x0000000000000000000000005c48d4fca7065cf7e79b905ddd3dc773fa3da4de",
                "0x0000000000000000000000000000000000000000000000000000000000000000"
            ],
            "data": "0x",
            "logIndex": 23,
            "blockHash": "0x2e816d7930aab9b0e387459da662789c9e069fb87d5bd684e6e3b3a0a23d2094"
        },
        {
            "transactionIndex": 21,
            "blockNumber": 6225912,
            "transactionHash": "0xad28e8b80c5c2d1a88fd8f2fd88d3cf4bf4aa66db7cdfbe1c668531b46a0f3f0",
            "address": "0x5C48D4fcA7065cf7e79B905ddd3dC773fA3dA4de",
            "topics": [
                "0x38690a554ffbc44eb6a75016e47d517d0db8e6c37494adc68d6d0b2c66f0ab21",
                "0x0000000000000000000000000000000000000000000000000000000000000001",
                "0x0000000000000000000000000000000000000000000000000000000000000000"
            ],
            "data": "0x000000000000000000000000d7fc917c41d27667343f22379d34e96974047ae20000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000a",
            "logIndex": 24,
            "blockHash": "0x2e816d7930aab9b0e387459da662789c9e069fb87d5bd684e6e3b3a0a23d2094"
        }
    ],
    "blockNumber": 6225912,
    "confirmations": 1,
    "cumulativeGasUsed": {
        "type": "BigNumber",
        "hex": "0x20b937"
    },
    "effectiveGasPrice": {
        "type": "BigNumber",
        "hex": "0x12630afcd3"
    },
    "status": 1,
    "type": 2,
    "byzantium": true,
    "events": [
        {
            "transactionIndex": 21,
            "blockNumber": 6225912,
            "transactionHash": "0xad28e8b80c5c2d1a88fd8f2fd88d3cf4bf4aa66db7cdfbe1c668531b46a0f3f0",
            "address": "0x0078f766CCa2876da1F43cC6743b32F5f577C0c8",
            "topics": [
                "0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925",
                "0x000000000000000000000000d7fc917c41d27667343f22379d34e96974047ae2",
                "0x0000000000000000000000005c48d4fca7065cf7e79b905ddd3dc773fa3da4de"
            ],
            "data": "0x000000000000000000000000000000000000000000000000000000000000000a",
            "logIndex": 20,
            "blockHash": "0x2e816d7930aab9b0e387459da662789c9e069fb87d5bd684e6e3b3a0a23d2094"
        },
        {
            "transactionIndex": 21,
            "blockNumber": 6225912,
            "transactionHash": "0xad28e8b80c5c2d1a88fd8f2fd88d3cf4bf4aa66db7cdfbe1c668531b46a0f3f0",
            "address": "0x0078f766CCa2876da1F43cC6743b32F5f577C0c8",
            "topics": [
                "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef",
                "0x000000000000000000000000d7fc917c41d27667343f22379d34e96974047ae2",
                "0x0000000000000000000000005c48d4fca7065cf7e79b905ddd3dc773fa3da4de"
            ],
            "data": "0x0000000000000000000000000000000000000000000000000000000000000001",
            "logIndex": 21,
            "blockHash": "0x2e816d7930aab9b0e387459da662789c9e069fb87d5bd684e6e3b3a0a23d2094"
        },
        {
            "transactionIndex": 21,
            "blockNumber": 6225912,
            "transactionHash": "0xad28e8b80c5c2d1a88fd8f2fd88d3cf4bf4aa66db7cdfbe1c668531b46a0f3f0",
            "address": "0x7b4a0AF79B11d65ff6a21450E053Fd73D3a9107e",
            "topics": [
                "0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925",
                "0x000000000000000000000000d7fc917c41d27667343f22379d34e96974047ae2",
                "0x0000000000000000000000000000000000000000000000000000000000000000",
                "0x0000000000000000000000000000000000000000000000000000000000000000"
            ],
            "data": "0x",
            "logIndex": 22,
            "blockHash": "0x2e816d7930aab9b0e387459da662789c9e069fb87d5bd684e6e3b3a0a23d2094"
        },
        {
            "transactionIndex": 21,
            "blockNumber": 6225912,
            "transactionHash": "0xad28e8b80c5c2d1a88fd8f2fd88d3cf4bf4aa66db7cdfbe1c668531b46a0f3f0",
            "address": "0x7b4a0AF79B11d65ff6a21450E053Fd73D3a9107e",
            "topics": [
                "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef",
                "0x000000000000000000000000d7fc917c41d27667343f22379d34e96974047ae2",
                "0x0000000000000000000000005c48d4fca7065cf7e79b905ddd3dc773fa3da4de",
                "0x0000000000000000000000000000000000000000000000000000000000000000"
            ],
            "data": "0x",
            "logIndex": 23,
            "blockHash": "0x2e816d7930aab9b0e387459da662789c9e069fb87d5bd684e6e3b3a0a23d2094"
        },
        {
            "transactionIndex": 21,
            "blockNumber": 6225912,
            "transactionHash": "0xad28e8b80c5c2d1a88fd8f2fd88d3cf4bf4aa66db7cdfbe1c668531b46a0f3f0",
            "address": "0x5C48D4fcA7065cf7e79B905ddd3dC773fA3dA4de",
            "topics": [
                "0x38690a554ffbc44eb6a75016e47d517d0db8e6c37494adc68d6d0b2c66f0ab21",
                "0x0000000000000000000000000000000000000000000000000000000000000001",
                "0x0000000000000000000000000000000000000000000000000000000000000000"
            ],
            "data": "0x000000000000000000000000d7fc917c41d27667343f22379d34e96974047ae20000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000a",
            "logIndex": 24,
            "blockHash": "0x2e816d7930aab9b0e387459da662789c9e069fb87d5bd684e6e3b3a0a23d2094",
            "args": [
                {
                    "type": "BigNumber",
                    "hex": "0x01"
                },
                {
                    "type": "BigNumber",
                    "hex": "0x00"
                },
                "0xd7fC917C41d27667343F22379d34E96974047Ae2",
                "0x0000000000000000000000000000000000000000",
                {
                    "type": "BigNumber",
                    "hex": "0x0a"
                }
            ],
            "event": "MarketItemCreated",
            "eventSignature": "MarketItemCreated(uint256,uint256,address,address,uint256)"
        }
    ]
}
```

```
// createSaleRes

{
    "to": "0x5C48D4fcA7065cf7e79B905ddd3dC773fA3dA4de",
    "from": "0xd7fC917C41d27667343F22379d34E96974047Ae2",
    "contractAddress": null,
    "transactionIndex": 47,
    "gasUsed": {
        "type": "BigNumber",
        "hex": "0xb8af"
    },
    "logsBloom": "0x00000000000000000000000000000000000000000000000000000000000000000000000000000000002000000000000000000000000000000000000000041000000000000000000000000000000000000000000000040000000000000000000000000000020000000000000000000800000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000000000040000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000200000000060000000000000000000000000000000000100000000000000000000000000000000",
    "blockHash": "0xca9192efead638b6036ffbce8f38d8238efb2806dafd1c56bc2c33beead29e0d",
    "transactionHash": "0x1b2bfd2f5de9f1eb4513cad62b7bd1168fbabaa2ec308bdc7f9025089c76d161",
    "logs": [
        {
            "transactionIndex": 47,
            "blockNumber": 6226072,
            "transactionHash": "0x1b2bfd2f5de9f1eb4513cad62b7bd1168fbabaa2ec308bdc7f9025089c76d161",
            "address": "0x5C48D4fcA7065cf7e79B905ddd3dC773fA3dA4de",
            "topics": [
                "0x0b59dfc56db79c6259bcd97a3fc890ab90008a8b5781d89dd763e01651bc7bc8",
                "0x0000000000000000000000000000000000000000000000000000000000000001",
                "0x0000000000000000000000000000000000000000000000000000000000000000"
            ],
            "data": "0x000000000000000000000000d7fc917c41d27667343f22379d34e96974047ae2000000000000000000000000d7fc917c41d27667343f22379d34e96974047ae20000000000000000000000000000000000000000000000000000000000000005",
            "logIndex": 110,
            "blockHash": "0xca9192efead638b6036ffbce8f38d8238efb2806dafd1c56bc2c33beead29e0d"
        }
    ],
    "blockNumber": 6226072,
    "confirmations": 1,
    "cumulativeGasUsed": {
        "type": "BigNumber",
        "hex": "0x67973b"
    },
    "effectiveGasPrice": {
        "type": "BigNumber",
        "hex": "0x070807c5c3"
    },
    "status": 1,
    "type": 2,
    "byzantium": true,
    "events": [
        {
            "transactionIndex": 47,
            "blockNumber": 6226072,
            "transactionHash": "0x1b2bfd2f5de9f1eb4513cad62b7bd1168fbabaa2ec308bdc7f9025089c76d161",
            "address": "0x5C48D4fcA7065cf7e79B905ddd3dC773fA3dA4de",
            "topics": [
                "0x0b59dfc56db79c6259bcd97a3fc890ab90008a8b5781d89dd763e01651bc7bc8",
                "0x0000000000000000000000000000000000000000000000000000000000000001",
                "0x0000000000000000000000000000000000000000000000000000000000000000"
            ],
            "data": "0x000000000000000000000000d7fc917c41d27667343f22379d34e96974047ae2000000000000000000000000d7fc917c41d27667343f22379d34e96974047ae20000000000000000000000000000000000000000000000000000000000000005",
            "logIndex": 110,
            "blockHash": "0xca9192efead638b6036ffbce8f38d8238efb2806dafd1c56bc2c33beead29e0d",
            "args": [
                {
                    "type": "BigNumber",
                    "hex": "0x01"
                },
                {
                    "type": "BigNumber",
                    "hex": "0x00"
                },
                "0xd7fC917C41d27667343F22379d34E96974047Ae2",
                "0xd7fC917C41d27667343F22379d34E96974047Ae2",
                {
                    "type": "BigNumber",
                    "hex": "0x05"
                }
            ],
            "event": "MarketItemUpForSale",
            "eventSignature": "MarketItemUpForSale(uint256,uint256,address,address,uint256)"
        }
    ]
}
```

```
如果市场上有很多NFT，需要一次性获取并展示它们的属性，你可以采取以下方法：

批量查询智能合约：
如果智能合约支持批量查询，你可以一次性获取多个NFT的属性。

批量请求元数据：
使用并行HTTP请求来批量获取NFT的元数据。

后端服务聚合：
构建一个后端服务来聚合和缓存NFT属性，然后前端从这个服务中获取数据。

方法1：批量查询智能合约
如果你的智能合约支持批量查询，你可以调用一个批量方法获取多个NFT的属性。如果合约不支持，你可以在智能合约中添加一个批量查询方法。

假设你有一个批量查询方法 getAttributesBatch：

javascript
复制代码
async function getNftAttributesBatch(tokenIds) {
    const attributesBatch = await contract.getAttributesBatch(tokenIds);
    return attributesBatch;
}

const tokenIds = [1, 2, 3, 4, 5]; // 你想要查询的 tokenId 数组
getNftAttributesBatch(tokenIds).then(attributesBatch => {
    console.log('NFT Attributes Batch:', attributesBatch);
    // 在前端展示这些属性
    // ...
}).catch(error => {
    console.error('Error getting NFT attributes batch:', error);
});
方法2：批量请求元数据
使用并行HTTP请求来批量获取NFT的元数据。你可以使用 Promise.all 来并行处理多个请求：

javascript
复制代码
async function getNftMetadata(tokenId) {
    const tokenURI = await contract.tokenURI(tokenId);
    const response = await fetch(tokenURI);
    const metadata = await response.json();
    return metadata;
}

async function getNftMetadataBatch(tokenIds) {
    const metadataPromises = tokenIds.map(tokenId => getNftMetadata(tokenId));
    const metadataBatch = await Promise.all(metadataPromises);
    return metadataBatch;
}

const tokenIds = [1, 2, 3, 4, 5]; // 你想要查询的 tokenId 数组
getNftMetadataBatch(tokenIds).then(metadataBatch => {
    console.log('NFT Metadata Batch:', metadataBatch);
    // 在前端展示这些属性
    // ...
}).catch(error => {
    console.error('Error getting NFT metadata batch:', error);
});
```

# 流程

1. 合同部署
2. erc20token创造者调用mint函数创造一定数量的币种，自己调用吧，页面就不走这个函数的交互了
3. 挖nft  -- nft safeMint 
4. 上架nft 
   - nft - setApprovalForAll - 用于授权市场的操作权限，这个方法只需要操作一次即可永久授权
     - 参数 市场address , true
   - erc20Contract.approve - erc20 授权一定的操作津贴，否则市场无法交易
     - 参数  spender - 市场
   - 添加到市场：market.addItemToMarket (transferFrom & safeTransferFrom) - 转移给市场 token price
   - 修改链上的item数据 createSale ,这一步和上面的一步一起操作上架
5. 购买
   1. 购买的用户也需要给市场一定的erc20 allowance
