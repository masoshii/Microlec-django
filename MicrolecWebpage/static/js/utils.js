$(document).ready(function() {
  if (readCookie("cart_items") == null) {
    document.cookie = "cart_items=; expires=Fri, 31 Dec 2100 12:00:00 UTC; path=/";
  }
 
});
function isEmailValid(emailString){
    const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(com|org|net|cl|ar|co|uy|uk|pe|br|bo)$/;
    return emailRegex.test(emailString);
}

function cookieProcess(cookieValue){
  
    var actualChar;
    var productID = "";
    var productQuantity = "";
    var fetchingID = true;
    var products = new Map();
  
    for (let i = 0; i < cookieValue.length; i++) {
      actualChar = cookieValue.charAt(i);
      if(actualChar == '%'){
        fetchingID = false;
      } else if (actualChar == '&'){
        products.set(productID,productQuantity);
        productID = "";
        productQuantity = "";
        fetchingID = true;
      } else if (isNumeric(actualChar)) {
        if (fetchingID){
          productID += actualChar;
        } else {
          productQuantity += actualChar; 
        };
      };
    }
    return products;
}


function productsInCookie(cookieValue){
    var actualChar;
    var fetchingID = true;
    var quantity = 0;
  
    for (let i = 0; i < cookieValue.length; i++) {
      actualChar = cookieValue.charAt(i);
      if(actualChar == '%'){
        quantity += 1;
        fetchingID = false;
      } else if (actualChar == '&'){
        fetchingID = true;
    }
  }
  return quantity;
}

function productIsInCookie(cookieValue, productId){
  var actualChar;
  var iterProductId = "";
  var fetchingID = true;

  for (let i = 0; i < cookieValue.length; i++) {
    actualChar = cookieValue.charAt(i);
    if(actualChar == '%'){
      fetchingID = false;
    } else if (actualChar == '&'){
      if (productId == iterProductId){
        return true;
      }
      iterProductId = "";
      fetchingID = true;
    } else if (isNumeric(actualChar)) {
      if (fetchingID){
        iterProductId += actualChar;
      }
    };
  }
  return false;
}
  
function readCookie(name)
{
name += '=';
var parts = document.cookie.split(/;\s*/);
for (var i = 0; i < parts.length; i++)
{
    var part = parts[i];
    if (part.indexOf(name) == 0)
    return part.substring(name.length)
}
return null;
}



function isNumeric(str) {
if (typeof str != "string") return false
return !isNaN(str) && !isNaN(parseFloat(str))
}

function deleteProductCookie(cookieValue, idToRemove) {

  if (productsInCookie(cookieValue) == 1){
    document.cookie = `cart_items=; expires=Fri, 31 Dec 2100 12:00:00 UTC; path=/`
    return;
  }

  var regex = new RegExp(`${idToRemove}%\\d+&`, 'g');
  
  var updatedCookieValue = cookieValue.replace(regex, '');
  
  if (updatedCookieValue.charAt(updatedCookieValue.length - 1) !== '&') {
    updatedCookieValue = updatedCookieValue.slice(0, -1) + '&';
  }
  
  document.cookie = `cart_items=${updatedCookieValue}; expires=Fri, 31 Dec 2100 12:00:00 UTC; path=/`
}

function addProductToCookie(cookieValue, productId, quantity){
  var percAdition;
  var quaAdition;
  var finalCookie;
  var idAdition;

  if (cookieValue == null){
    percAdition = productId += '%';
    quaAdition = percAdition += quantity;
    finalCookie = quaAdition += '&';
    document.cookie = `cart_items=${finalCookie}; expires=Fri, 31 Dec 2100 12:00:00 UTC; path=/`;
    return;
  } else {
    if (!productIsInCookie(cookieValue, productId)){
      idAdition = cookieValue += productId;
      percAdition = idAdition += '%';
      quaAdition = percAdition += quantity;
      finalCookie = quaAdition += '&';
      document.cookie = `cart_items=${finalCookie}; expires=Fri, 31 Dec 2100 12:00:00 UTC; path=/`;
      return;
    }
  }
}


function updateCookieQuantity(cookieValue, productId, newQuantity){
  var actualChar;
  var iterProductId = "";
  var iterProductQua = "";
  var fetchingID = true;
  var newCookie = "";
  var temp_cambiado;
  for (let i = 0; i < cookieValue.length; i++) {
    actualChar = cookieValue.charAt(i);
    if(actualChar == '%'){
      if(iterProductId == productId){
        temp_cambiado = iterProductId;
        newCookie += iterProductId;
        newCookie += '%';
        newCookie += newQuantity;
        fetchingID = true;
        iterProductId = "";
        iterProductQua = "";
      } else {
        newCookie += iterProductId;
        newCookie += '%'
        fetchingID = false;
      }
    } else if (actualChar == '&'){
      newCookie += iterProductQua;
      newCookie += '&';
      fetchingID = true;
      iterProductId = "";
      iterProductQua = "";
    } else if (isNumeric(actualChar)) {
      if (fetchingID){
        iterProductId += actualChar;
      } else if (!fetchingID){
        iterProductQua += actualChar;
      }
    };
  }
  document.cookie = `cart_items=${newCookie}; expires=Fri, 31 Dec 2100 12:00:00 UTC; path=/`;
}

const delay = ms => new Promise(res => setTimeout(res, ms));

function isMultiple(multiple,base){
  if (isNaN(multiple) || isNaN(base)){
    return false;
  } else {
    var remainder = multiple % base;
    if (remainder == 0){
      return true;
    } else {
      return false;
    }
  }
}

function deleteExtraSpace(str) {
  while (str.charAt(0) === ' ') {
      str = str.slice(1);
  }
  while (str.charAt(str.length - 1) === ' ') {
      str = str.slice(0, -1);
  }
  return str;
}

function formatTimeHM(timeString) {
  if (!/^([01]\d|2[0-3]):([0-5]\d):([0-5]\d)$/.test(timeString)) {
      throw new Error('Unexpected format.');
  }
  const hourAndMinute = timeString.split(':').slice(0, 2).join(':');

  return hourAndMinute; 
}

function capitalize(string) {
  return string.charAt(0).toUpperCase() + string.slice(1);
}

function removeElementsByClass(className){
  const elements = document.getElementsByClassName(className);
  while(elements.length > 0){
      elements[0].parentNode.removeChild(elements[0]);
  }
}

function isBlank(str) {
  return (!str || /^\s*$/.test(str));
}

function isRunValid(run) {
  run = String(run);
  
  if (run.length < 9 || run.length > 10) {
      return false;    
  }

  let parts = run.split('-');

  if (parts.length !== 2) {
      return false;
  }

  let nodv_run = parts[0];
  let dv_run = parts[1];

  if (!/^\d+$/.test(dv_run)) {
    if (dv_run.toUpperCase() !== 'K') {
      return false;
    } else {
      dv_run = 10;
    }
  } else {
    dv_run = parseInt(dv_run);
    if (dv_run === 0) {
      dv_run = 11;
    }
  }
  
  let nodv_run_str;
  try {
      nodv_run = parseInt(nodv_run);
      nodv_run_str = String(nodv_run);
  } catch (error) {
      return false;
  }
  
  let inverted_run = nodv_run_str.split('').reverse().join('');

  let total_sum = 0;
  let factor = 2;
  for (let index = 0; index < inverted_run.length; index++) {
      let char = inverted_run[index];
      let value = parseInt(char) * factor;
      total_sum += value;
      factor++;
      if (factor > 7) {
          factor = 2;
      }
  }
  
  let differencenum = Math.trunc(total_sum/11);
  differencenum = differencenum * 11;
  let real_dvrun = total_sum-differencenum;
  real_dvrun = 11-real_dvrun;
  
  if (dv_run === real_dvrun){
    return true
  }
  return false;
}
