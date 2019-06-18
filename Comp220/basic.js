"use strict";

const button = document.getElementById("clickme");

console.log("Hello World from basic.js");

function onButtonClicked() {
    console.log("I'm in the button click event");
    let valueby = Number(document.getElementById("inputtext").value);
    valueby++;
    console.log("Value is now", valueby);

}

button.addEventListener("click", onButtonClicked);

//////////////////////////////////////////////////
//    simple calculator
//    2019/02/18 Angela Henders
//////////////////////////////////////////////////

const btn1 = document.getElementById("btn1");
const btn2 = document.getElementById("btn2");
const btn3 = document.getElementById("btn3");
const btn4 = document.getElementById("btn4");
const btn5 = document.getElementById("btn5");
const btn6 = document.getElementById("btn6");
const btn7 = document.getElementById("btn7");
const btn8 = document.getElementById("btn8");
const btn9 = document.getElementById("btn9");
const btn0 = document.getElementById("btn0");

// Create Variables for each button
let calcdisplay = document.getElementById("calcdisplay");
let btnclear = document.getElementById("btnclear");
let btndiv = document.getElementById("btndiv");
let btnmult = document.getElementById("btnmult");
let btnsub = document.getElementById("btnsub");
let btndec = document.getElementById("btndec");
let btneq = document.getElementById("btneq");
let btnadd = document.getElementById("btnadd");

let operandStack = [];
let operatorStack = [];

let workingNum = "";
let displayNum = "";
let decimalInPlay = false;
let lastClickedOperator = false;

//working with HTML input
function onButtonClicked() {
    console.log("I'm in the button click event");
}

// calculator implmentation
//disallow the user to enter text in the input field, for display only
calcdisplay.disabled = true;

//called when a number button is clicked
function calculateWorkingNum(num) {

    // workingNum = getInputDisplay();

    if (workingNum == "") {
        workingNum = num.toString();
    }
    else {
        workingNum = workingNum + num.toString();
    }

    displayNum = workingNum;
    calcdisplay.value = displayNum;

//    console.log("Working Number is now: " + workingNum);

}

function onDecimalClicked() {

    if (!decimalInPlay) {
        decimalInPlay = true;
        displayNum = displayNum + ".";
        workingNum = displayNum;
        calcdisplay.value = displayNum;
    }
}

function onNumButtonClicked(value) {
    return function () {
        calculateWorkingNum(value);
        lastClickedOperator = false;
    }
}

function pushNumberandOperatortoStack(operator) {

    //if operator was last clicked, replace with current operator
    if (lastClickedOperator === true) {
        operatorStack.shift();
    }
    operandStack.push(Number(displayNum));
    workingNum = "";
    lastClickedOperator = true;

    operatorStack.push(operator);

    //console.log ("Operators: " + operatorStack);
    //console.log ("Operands: " + operandStack);
}

//reduce the operand and operator stack after performing the operation
function updateStacksandDisplay(newNum, i, j) {

    operandStack.splice(i, 1);
    operandStack[i-1] = newNum;
    operatorStack.splice(j-1, 1);
    if (operatorStack[0]=== "=") {
        operatorStack.pop();
        operandStack.pop();
    }

    displayNum = newNum.toString();
    workingNum = "";
    calcdisplay.value = displayNum;

    //   console.log("operator stack after cleanup: " + operatorStack);
    //   console.log("operand stack after cleanup: " + operandStack);
}
//perform the operation
function performOperation(operator, i, j) {

    let newNum = 0;

    switch (operator) {
        case '+':
            newNum = operandStack[i-1] + operandStack[i];
            updateStacksandDisplay(newNum, i, j);
            break;
        case '-':
            newNum = operandStack[i-1] - operandStack[i];
            updateStacksandDisplay(newNum, i, j);
            break;
        case '*' :
            newNum = operandStack[i-1] * operandStack[i];
            updateStacksandDisplay(newNum, i, j);
            break;
        case '/' :
            newNum = operandStack[i-1] / operandStack[i];
            updateStacksandDisplay(newNum, i, j);
            break;
        default: {
            console.log("Something went weird with performing the operation");
        }
    }
}

function assessPrecedenceWeight(operator) {

    let weight = 0;

    switch(operator) {
        case "+" :
        case "-" :
            weight = 1;
            break;
        case "*" :
        case "/" :
            weight = 2;
            break;
        case "=" :
            weight = 1;
            break;
        default:
            console.log("unexpected operator");
    }

    return(weight);
}

function getNumberofOperators() {

    return (operatorStack.length);
}

function getOperator(index) {

    return (operatorStack[index]);
}

function getOperandIndex() {

    return operandStack.length-1;
}

function assessForOperation() {
    //if there are at least 2 operands check if need to perform operation

    let numOperators = getNumberofOperators();
    let lastOperandIndex = 0;
    let lastOperator = "";
    let secondLastOperator = "";
    let keepLooking = true;

    //there must be at least 2 operators to need an operation
    while ((numOperators >= 2) && (keepLooking == true)) {

        lastOperandIndex = getOperandIndex();
        lastOperator = getOperator(numOperators-1);
        secondLastOperator = getOperator(numOperators-2);
        //if operators are equal precedence, perform the operation
        //e.g. 1+2+ or 1*2* or 1+2- or 1-2+ or 1/2*
        if ((assessPrecedenceWeight(lastOperator) <= assessPrecedenceWeight(secondLastOperator))
            && (numOperators >=2)) {
            performOperation(secondLastOperator, lastOperandIndex, numOperators-1);
            numOperators = getNumberofOperators();
        }
        else {
            keepLooking = false;
        }
    }
}

function onOperatorButtonClicked(operator) {
    return function () {
        pushNumberandOperatortoStack(operator);
        assessForOperation();
        decimalInPlay = false;
    }
}

//clear the calculator display value and operand and operator stacks to empty
function clearCalcDisplay() {
    calcdisplay.value = "0";
    workingNum = "";
    displayNum = workingNum;
    operatorStack = [];
    operandStack = [];
    decimalInPlay = false;
    lastClickedOperator = false;
    //console.log("calcdisplay is " + calcdisplay.value);
}

btnclear.addEventListener("click", clearCalcDisplay);

btnadd.addEventListener("click", onOperatorButtonClicked("+"));
btnsub.addEventListener("click", onOperatorButtonClicked("-"));
btnmult.addEventListener("click", onOperatorButtonClicked("*"));
btndiv.addEventListener("click", onOperatorButtonClicked("/"));
btneq.addEventListener("click", onOperatorButtonClicked("="));

btn1.addEventListener("click", onNumButtonClicked(1));
btn2.addEventListener("click", onNumButtonClicked(2));
btn3.addEventListener("click", onNumButtonClicked(3));
btn4.addEventListener("click", onNumButtonClicked(4));
btn5.addEventListener("click", onNumButtonClicked(5));
btn6.addEventListener("click", onNumButtonClicked(6));
btn7.addEventListener("click", onNumButtonClicked(7));
btn8.addEventListener("click", onNumButtonClicked(8));
btn9.addEventListener("click", onNumButtonClicked(9));
btn0.addEventListener("click", onNumButtonClicked(0));

btndec.addEventListener("click", onDecimalClicked);

////////////////////////////////////////
// Tax Rates for 2019
//
// 2019 02 18
// Angela Henders
//
///////////////////////////////////////
//
// Referenced from: https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/canadian-income-tax-rates-individuals-current-previous-years.html#federal
//
/////////////////////////////////////////
/*
  Federal Taxes
  ---------------------------------------
  15% on the first $47,630 of taxable income, plus
  20.5% on the next $47,629 of taxable income
    (on the portion of taxable income over 47,630 up to $95,259), plus
  26% on the next $52,408 of taxable income
    (on the portion of taxable income over $95,259 up to $147,667), plus
  29% on the next $62,704 of taxable income
    (on the portion of taxable income over 147,667 up to $210,371), plus
  33% of taxable income over $210,371
 */

const btncalculatetax = document.getElementById("btncalculatetax");
const line1 = document.getElementById("Line1");
const line2 = document.getElementById("Line2");
const line3 = document.getElementById("Line3");
const line4 = document.getElementById("Line4");
const line5 = document.getElementById("Line5");
const line6 = document.getElementById("Line6");
const line7 = document.getElementById("Line7");
const etaxrate = document.getElementById("etaxrate");

let userIncome = 0;
let federalTaxOwed = 0;

const taxRates = [
    {   baseamount: 0,
        taxCeiling: 47630,
        taxRate:  0.15,
        maxTax:   7145,
        maxTaxcum:   0},
    {   baseamount: 47630,
        taxCeiling: 95259,
        taxRate:  0.205,
        maxTax:   9764,
        maxTaxcum: 7145},
    {   baseamount: 95259,
        taxCeiling: 147667,
        taxRate:  0.26,
        maxTax:   13626,
        maxTaxcum: 16908},
    {   baseamount: 147667,
        taxCeiling: 210371,
        taxRate:  0.29,
        maxTax:   18184,
        maxTaxcum: 30535},
    {   baseamount: 210371,
        taxRate: 0.33,
        maxTaxcum: 48719
    }
];

//display line calculations 1-7

function displayCalculations (line3Calc, line5Calc, totalFederalTax, effectiveTax, i) {

    line2.value = "- " + taxRates[i].baseamount.toString();
    line3.value = "= " + line3Calc.toString();
    line4.value = "x " + (taxRates[i].taxRate*100).toString() + "%";
    line5.value = "= " + line5Calc.toString();
    line6.value = "+ " + taxRates[i].maxTaxcum.toString();
    line7.value = "= " + totalFederalTax.toString();
    etaxrate.value = effectiveTax.toString() + "%";
}

function getFederalTaxAmount(income) {

    let totalFederalTax = 0;
    let effectiveTax = 0;
    let line3Calc = 0;
    let line5Calc = 0;
    let i = 0;

    do {
        if((income < taxRates[i].taxCeiling) || (i===taxRates.length-1)) {
            console.log("income is " + income + " and taxCeiling is " + taxRates[i].taxCeiling);
            line3Calc = income-taxRates[i].baseamount;
            line3Calc = Number.parseFloat(line3Calc).toFixed(2);
            line5Calc = line3Calc * taxRates[i].taxRate;
            line5Calc = Number(Number.parseFloat(line5Calc).toFixed(2));
            console.log("line5 calc is " + line5Calc);
            totalFederalTax = Number(line5Calc + taxRates[i].maxTaxcum);
            totalFederalTax = Number.parseFloat(totalFederalTax).toFixed(2);
            console.log("total federal tax is " + totalFederalTax);
            effectiveTax = totalFederalTax/income * 100;

            effectiveTax = +effectiveTax.toFixed(2);
            displayCalculations(line3Calc, line5Calc, totalFederalTax, effectiveTax, i);
            return;
        }
        i++;
    } while (i< taxRates.length);
}

function onCalcTaxButtonClicked() {

    userIncome = line1.value;
    getFederalTaxAmount(userIncome);

}

btncalculatetax.addEventListener("click", onCalcTaxButtonClicked);

/////////////////////////////////////////////////////////
//
// Working with Arrays
// 2019 02 20
// Angela Henders
//
/////////////////////////////////////////////////////////
//
// button add - add input field to array if a number
//            - messages a number added to array or error
// button show - show contents of array in messg area as 1,2,3,4
// button total - add all numbers in the array, show in messg area
// button clear - clear array so no entries in array
//
// assumptions - dealing with just integers
/////////////////////////////////////////////////////////

const btnaddarr = document.getElementById("btnaddarr");
const btnshowarr = document.getElementById("btnshowarr");
const btntotalarr = document.getElementById("btntotalarr");
const btncleararr = document.getElementById("btncleararr");
let arrinput = document.getElementById("arrinput");
let messagesarea = document.getElementById("messagesarea");

let workArray = [];

let total = 0;

function getInput() {

    return(arrinput.value);
}

function checkIfNumber(userInput) {

    if (Number(userInput)) {
        return true;
    }
    else {
        console.log("is not a number");
        return false;
    }
}


function onButtonAddArrClicked() {

    let userInput = getInput();

    if(checkIfNumber(userInput)===true) {
        workArray.push(Number(userInput));
        console.log("array is now:" + workArray);
        messagesarea.innerHTML = "added " + userInput + " to the array";
        console.log("message area should be" + messagesarea.value);
    }
    else {
        console.log("not a number, need update display");
        messagesarea.textContent = "Not a number.  Please enter a number";
    }

    arrinput.value = "";

}

function onButtonShowArrClicked() {

    let arrayString = "";
    let arrayLength = workArray.length;


    for (let i = 0; i<arrayLength ; i++) {

        arrayString += String(workArray[i])
        if (i < (arrayLength-1)) {
            arrayString += ",";
            console.log("string is now" + arrayString);
        }
    }

    messagesarea.textContent = arrayString;

}

function onButtonTotalArrClicked() {

    let arrayTotal = 0;
    let arrayLength = workArray.length;

    for (let i = 0; i<arrayLength ; i++) {

        arrayTotal += workArray[i];
    }

    messagesarea.innerHTML = "Sum of Array elements is " + arrayTotal;
}

function onButtonClearArrClicked() {
    workArray = [];
    arrinput.value = "";
    messagesarea.textContent = "";
}

btnaddarr.addEventListener("click", onButtonAddArrClicked);
btnshowarr.addEventListener("click", onButtonShowArrClicked);
btntotalarr.addEventListener("click", onButtonTotalArrClicked);
btncleararr.addEventListener("click", onButtonClearArrClicked);

/////////////////////////////////////////////
//
//  Working with Dictionaries
//
/////////////////////////////////////////////
//
//  based on an input capitalized province code display the
//  matching province name
//
//  enhancements: make code case agnostic eg. AB = ab
//    check user input for errors first
//
/////////////////////////////////////////////

let lookupword = document.getElementById("lookupword");
const btnlookup = document.getElementById("btnlookup");
let messagesarea2 = document.getElementById("messagesarea2");

const provinces = [
    {   province: "Alberta",
        code: "AB"
    },
    {   province: "British Columbia",
        code: "BC"
    },
    {   province: "Ontario",
        code: "ON"
    },
    {   province: "Nova Scotia",
        code: "NS"
    },
    {   province: "New Brunswick",
        code: "NB"
    },
    {   province: "Newfoundland",
        code: "NL"
    },
    {   province: "Prince Edward Island",
        code: "PE"
    },
    {   province: "Quebec",
        code: "QC"
    },
    {
        province: "Manitoba",
        code: "MB"
    },
    {   province: "Saskatchewan",
        code: "SK"
    }
];

function getLookupRequest() {

    return lookupword.value;
}

function codeNotFound(provcode) {

    messagesarea2.innerHTML = "Province code " + provcode + " was not found";

}
function lookupCode(provcode, provinces){
    for (var i=0; i < (provinces.length-1); i++) {
        console.log("is is " + i);
        if (provinces[i].code === provcode) {
            console.log("found province code");
            return i;
        }
    }
    console.log("Code not found");
    codeNotFound(provcode);
    return(-1);

}

function displayLookupResult(i) {

    let provincetoDisplay = provinces[i].province;
    let codetoDisplay = provinces[i].code;
    console.log("in displaylookupresult");
    console.log("matching province is " + provinces[i].province);
    messagesarea2.textContent = "Province for code " + codetoDisplay +
        " is " + provincetoDisplay;

}

function onButtonLookupClicked() {

    let lookup = "";

    lookup = getLookupRequest();
    let entryindex = lookupCode(lookup, provinces);
    console.log("entry index is" + entryindex);
    if (entryindex >= 0) {
        displayLookupResult(entryindex);
    }

}

btnlookup.addEventListener("click", onButtonLookupClicked);