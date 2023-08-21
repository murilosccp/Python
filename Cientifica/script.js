function insertChar(char) {
    document.getElementById("result").value += char;
}

function clearDisplay() {
    document.getElementById("result").value = "";
}

function deleteChar() {
    var value = document.getElementById("result").value;
    document.getElementById("result").value = value.substr(0, value.length - 1);
}

function calculate() {
    let result = document.getElementById("result");
    try {
      result.value = eval(result.value.replace("sqrt", "Math.sqrt").replace("sin", "Math.sin").replace("cos", "Math.cos").replace("tan", "Math.tan").replace("log", "Math.log").replace("pi", "Math.PI").replace("e", "Math.E"));
    } catch (error) {
      alert("Entrada inválida!");
    }
  }
  
