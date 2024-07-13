// https://api.pro.coins.ph/openapi/v1/ticker/price?symbols=[BTCPHP,DOGEPHP,BONKPHP,SOLPHP]

const axios = require('axios').default;

const getPrice = async () => {
  const url = "https://api.pro.coins.ph/openapi/v1/ticker/price?symbols=[BTCPHP,DOGEPHP,BONKPHP,SOLPHP]"
  try {
    const response = await axios.get(url);
    console.log(response.data);
  } catch (error) {
    console.error(error);
  }
}

getPrice()


async function getUser() {
  const url = "https://api.pro.coins.ph/openapi/v1/ticker/price?symbols=[BTCPHP,DOGEPHP,BONKPHP,SOLPHP]"
  try {
    const response = await axios.get(url);
    console.log(response.data);
  } catch (error) {
    console.error(error);
  }
}

// getUser()

// const url: string = "https://api.pro.coins.ph/openapi/v1/ticker/price"

// axios.get(url, {
//     params: {
//       symbols: ["BTCPHP", "DOGEPHP", "BONKPHP", "SOLPHP"]
//     }
//   })
//   .then(function (response) {
//     console.log(response);
//   })
//   .catch(function (error) {
//     console.log(error);
//   })
//   .then(function () {
//     // 常に実行
//   });  

/*
// 指定された ID のユーザーに対してリクエストを行う
axios.get('/user?ID=12345')
  .then(function (response) {
    // 処理が成功した場合
    console.log(response);
  })
  .catch(function (error) {
    // エラー処理
    console.log(error);
  })
  .then(function () {
    // 常に実行
  });
*/


/*
// オプションとして、上記のリクエストは次のようにすることもできます
axios.get('/user', {
    params: {
      ID: 12345
    }
  })
  .then(function (response) {
    console.log(response);
  })
  .catch(function (error) {
    console.log(error);
  })
  .then(function () {
    // 常に実行
  });  

*/
