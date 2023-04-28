//define part
let numbers = document.querySelectorAll('.num');
let Zero = document.querySelector('.zero');
let operators = document.querySelectorAll('.opr');
let isopr = true;
let result = document.querySelector('.calculator-output');
let C = document.querySelector('#clear');
let Switch = document.querySelector('.switch');
let isSwitch = true;
let Dot = document.querySelector('.dot');
let isDot = true;
let equal = document.querySelector('.equ');
let displays = "";
//push number
for(i = 0; i < numbers.length; i++){
    let number = numbers[i];
    number.onclick = function(){
        if(displays === '0'){  //the first number can't be zero
            displays = this.innerHTML;
            result.innerHTML = displays;
        }else{
            displays += this.innerHTML;
            result.innerHTML = displays
        }
        isopr = true;
    }
}
//zero judge
Zero.onclick = function(){
    if(displays === '0'){  //the first number can't be zero
        displays = '0';
        result.innerHTML = displays;
    }else{
        displays += '0';
        result.innerHTML = displays;
    }
}
//get operator
for(i = 0; i < operators.length; i++){
    let operator = operators[i];
    operator.onclick = function(){  
        if(displays === ""){  //a operator is preceded by a number
            displays = '0' + this.innerHTML;
            result.innerHTML = displays
        }else if(isopr){  //can't have two or more oprators between two numbers
            displays = displays + this.innerHTML;
            result.innerHTML = displays;
        }
        isopr = false;
        isDot = true;
        isSwitch = true;
    }
}
//clear displays
C.onclick = function(){
    displays = "";
    result.innerHTML = '0';
    isDot = true;
    isSwitch = true;
    isopr = true;
}
//the switch of positive and negtive
Switch.onclick = function(){
    if(isSwitch){
        displays = displays + '-';
        result.innerHTML = displays;
    }
    isSwitch = false;
}
//dot part
Dot.onclick = function(){
    if(displays === ""){  //a dot is preceded by a number
        displays += '0.';
        result.innerHTML = displays;
    }else if(isDot){  //can't have more dots in one number
        displays += '.';
        result.innerHTML = displays;       
    }
    isDot = false;
}
//calculate the result
equal.onclick = function(){
    displays = eval(displays);
    result.innerHTML = displays;
}
/* 
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/ClientSide/javascript.js to edit this template
 */


