const form = document.getElementById("formConvert");

// const fromCurrency = form.elements.namedItem("fromCurrency");
// console.log(fromCurrency);

const toCurrency = form.elements.namedItem("toCurrency");
// console.log(toCurrency);

const amount = form.elements.namedItem("amount");
console.log(amount);

const convertButton = form.elements.namedItem("convertButton");
console.log(convertButton);

const result = document.getElementById("result")
console.log(result);


async function getCurrency(){
    
    const currencyData = fetch("https://v6.exchangerate-api.com/v6/13e850427b43de4ce15525b3/codes")
    currencyData
    .then(response =>{
        if(response.ok){
            return response.json()
        }
        else{
            throw new Error("Something went wrong")
        }
    })
    .then(data =>{
        let currency = data["supported_codes"]
        console.log(currency);
        for(let element of currency){
            createCurrencyList(`${element[0]} ${element[1]}`)
        }
    })
    .catch(error=>{
        console.log(error);
    })
}

getCurrency()

let base = 'EUR';
let target = 'AOA';

// "base_code": "EUR",
// "target_code": "GBP",
// "conversion_rate": 0.8412,
// "conversion_result": 5.8884


// async function getCurrency(base, target){
    
//     const pconversionData = fetch("https://v6.exchangerate-api.com/v6/13e850427b43de4ce15525b3/pair/EUR/GBP/AMOUNT")
//     // const pconversionData = fetch(`https://v6.exchangerate-api.com/v6/13e850427b43de4ce15525b3/pair/${base}/${target}`)
//     pconversionData
//     .then(response =>{
//         if(response.ok){
//             return response.json()
//         }
//         else{
//             throw new Error("Something went wrong")
//         }
//     })
//     .then(data =>{
//         let conversionRate = data["conversion_rate"]
//         console.log(conversionRate);

//     })
//     .catch(error=>{
//         console.log(error);
//     })
// }

// getCurrency(base, target)




const pconversionData = fetch("https://v6.exchangerate-api.com/v6/13e850427b43de4ce15525b3/pair/EUR/GBP/AMOUNT")
// const pconversionData = fetch(`https://v6.exchangerate-api.com/v6/13e850427b43de4ce15525b3/pair/${base}/${target}`)
// pconversionData
// .then(response =>{
//     if(response.ok){
//         return response.json()
//     }
//     else{
//         throw new Error("Something went wrong")
//     }
// })
// .then(data =>{
//     let conversionRate = data["conversion_rate"]
//     console.log(conversionRate);

// })
// .catch(error=>{
//     console.log(error);
// })



function createCurrencyList(currencyCode){
    const selectFromCurrency = form.elements.namedItem("fromCurrency");
    const selectToCurrency = form.elements.namedItem("toCurrency")

    const currencyName = currencyCode;

    const optionFromCurrency = document.createElement('option');
    optionFromCurrency.setAttribute('value', currencyName);
    optionFromCurrency.textContent=currencyName;
    selectFromCurrency.appendChild(optionFromCurrency);

    const optionToCurrency = document.createElement('option');
    optionToCurrency.setAttribute('value', currencyName);
    optionToCurrency.textContent=currencyName;

    selectToCurrency.appendChild(optionToCurrency);
}



// console.log(selectFromCurrency);

// const selectToCurrency = form.elements.namedItem("toCurrency");
// console.log(selectToCurrency);