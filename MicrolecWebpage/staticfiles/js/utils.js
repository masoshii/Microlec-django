
function isEmailValid(emailString){
    const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(com|org|net|cl|ar|co|uy|uk|pe|br|bo)$/;
    return emailRegex.test(emailString);
}


function isNumeric(str) {
if (typeof str != "string") return false
return !isNaN(str) && !isNaN(parseFloat(str))
}


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
