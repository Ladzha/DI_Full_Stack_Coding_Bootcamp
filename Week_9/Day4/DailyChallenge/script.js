const form = document.getElementById("formConvert");

const convertButton = form.elements.namedItem("convertButton");
// const switchButton = form.elements.namedItem("switchButton");

convertButton.addEventListener("click", getUserInput)
// switchButton.addEventListener("click", switchCurrency)

// function switchCurrency(event){
//     event.preventDefault()

//     const fromCurrency = form.elements.namedItem("fromCurrency").value; 
//     fromCurrency.innerHTML = "lol"
//     const toCurrency = form.elements.namedItem("toCurrency").value;
    
// }

function getUserInput(event){
    event.preventDefault()
    const fromCurrency = form.elements.namedItem("fromCurrency").value;
    const fromCurrencyArr = fromCurrency.split(" ")
    const base = fromCurrencyArr[0];

    const toCurrency = form.elements.namedItem("toCurrency").value;
    const toCurrencyArr = toCurrency.split(" ")
    const target = toCurrencyArr[0];

    let amountInput = form.elements.namedItem("amount").value;
    if(amountInput == ''){
        amountInput ='1'
    }
    getCurrency(base, target, amountInput)
}

//getting list of currency code
function getCodeData(){   
    const currencyCodeList = fetch("https://v6.exchangerate-api.com/v6/13e850427b43de4ce15525b3/codes")
    currencyCodeList
    .then(response =>{
        if(response.ok){
            return response.json()
        }
        else{
            throw new Error("Something went wrong")
        }
    })
    .then(data =>{
        let currencyCodeArray = data["supported_codes"]
        for(let element of currencyCodeArray){
            createCurrencyCodeList(`${element[0]} ${element[1]}`)
            // console.log(element[0]);
        }
    })
    .catch(error=>{
        console.log(error);
    })
}

getCodeData();

//getting converted result
function getCurrency(base, target, amount){
  
    const pconversionData = fetch(`https://v6.exchangerate-api.com/v6/13e850427b43de4ce15525b3/pair/${base}/${target}/${amount}`)
    pconversionData
    .then(response =>{
        if(response.ok){
            return response.json()
        }
        else{
            throw new Error("Something went wrong")
        }
    })
    .then(data =>{
        let conversionResult = data["conversion_result"]
        displayResult(conversionResult)

    })
    .catch(error=>{
        console.log(error);
    })
};

//displaying result in div
function displayResult(result){
    const resultDiv = document.getElementById("result");
    resultDiv.textContent = result; 
};

//creating list of currency code
function createCurrencyCodeList(currencyCode){
    const selectFromCurrency = form.elements.namedItem("fromCurrency");
    const selectToCurrency = form.elements.namedItem("toCurrency")

    const currencyName = currencyCode;

    const optionFromCurrency = document.createElement('option');
    optionFromCurrency.setAttribute('value', currencyName);
    optionFromCurrency.classList.add('option')

    if(optionFromCurrency.value =='EUR Euro'){
        optionFromCurrency.setAttribute('selected', 'selected');
    }
    optionFromCurrency.textContent=currencyName;
    selectFromCurrency.appendChild(optionFromCurrency);

    const optionToCurrency = document.createElement('option');
    optionToCurrency.setAttribute('value', currencyName);
    optionToCurrency.classList.add('option')

    if(optionToCurrency.value =='USD United States Dollar'){
        optionToCurrency.setAttribute('selected', 'selected');
    }
    optionToCurrency.textContent=currencyName;

    selectToCurrency.appendChild(optionToCurrency);
};