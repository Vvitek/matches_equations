"use strict";
const coordinates = [[0,0,0],[10,0,1],[110,0,0],[110,100,0],[10,190,1],[0,100,0],[10,100,1],[55,55,0],[10,90,1],[10,110,1]];
const SIGNS = {      '0': [1,1,1,1,1,1,0,0,0,0],
		     '1': [0,0,1,1,0,0,0,0,0,0],
		     '2': [0,1,1,0,1,1,1,0,0,0],
		     '3': [0,1,1,1,1,0,1,0,0,0],
		     '4': [1,0,1,1,0,0,1,0,0,0],
		     '5': [1,1,0,1,1,0,1,0,0,0],
		     '6': [1,1,0,1,1,1,1,0,0,0],
		     '7': [0,1,1,1,0,0,0,0,0,0],
		     '8': [1,1,1,1,1,1,1,0,0,0],
		     '9': [1,1,1,1,1,0,1,0,0,0],
		     '-': [0,0,0,0,0,0,1,0,0,0],
		     '+': [0,0,0,0,0,0,1,1,0,0],
		     '=': [0,0,0,0,0,0,0,0,1,1]};

var selectedElement = 0;
var currentX = 0;
var currentY = 0;
var currentMatrix = 0;
let EQUATION = [];

function getEquation() {
	let xhr = new XMLHttpRequest();
	xhr.open('GET', '/equation');
	xhr.send(null);
	let form = document.createElement("form");
	xhr.onreadystatechange = function () {
		let DONE = 4;
		let OK = 200;
		if (xhr.readyState === DONE) {
			if (xhr.status === OK) {
				drawMatches(xhr.responseText);
			}
			else { console.log('Error' + xhr.status); }
		}
	}
}

function check() {
	var xhr = new XMLHttpRequest();
	xhr.open('GET', '/solution');
	xhr.send('');
	var solution = "";
	for(var i=0;i<5;i++) {
		for(let j in SIGNS) {
			for(let k=0;k<10;k++) {
				if(k==9) {EQUATION[i][k] === SIGNS[j][k] ? solution = solution.concat(j) : console.log('invalid') }
				else if(EQUATION[i][k] !== SIGNS[j][k]) { break; }
			}
		}
	}
	if(solution.length<i) { console.log("invalid syntax"); }
	else {
		var form = document.createElement("form");
		xhr.onreadystatechange = function () {
			let DONE = 4;
			let OK = 200;
			if (xhr.readyState === DONE) {
				if (xhr.status === OK) {
					alert(JSON.parse(xhr.responseText).solution.includes(solution) ? "Correct!":"Incorrect");
					document.getElementById('equation-button').innerHTML = "Wanna try again?";
					document.getElementById('equation-button').onclick = getEquation;
				} else { console.log('Error' + xhr.status); }
			}
		}
	}
}

function moveElement(evt) {
	currentMatrix[4] = evt.clientX - currentX;
	currentMatrix[5] = evt.clientY - currentY;
	var newMatrix = "matrix(" + currentMatrix.join(' ') + ")";
	selectedElement.setAttributeNS(null, "transform", newMatrix);
}

function deselectElement(evt) {
	if(selectedElement != 0) {
		var index = -1;
		var smallest = 80;
		var X = evt.clientX-document.getElementById('field').getBoundingClientRect().left;
		var Y = evt.clientY-document.getElementById('field').getBoundingClientRect().top;
		var position = Math.floor(X/130);
		var limits =(position%2===0 ? [0,7]:(Math.floor(X/130)===1 ? [6,8]:[8,10]));
		for(var i=limits[0];i<limits[1];i++) {
			if(Math.abs(coordinates[i][0]+(coordinates[i][2] ? 50:5)-X%130)+Math.abs(coordinates[i][1]+(coordinates[i][2] ? 5:50)-Y)<smallest && EQUATION[position][i]===0) { 
				index = i;
				smallest = Math.abs(coordinates[i][0]+(coordinates[i][2] ? 50:5)-X%130)+Math.abs(coordinates[i][1]+(coordinates[i][2] ? 5:50)-Y+150);
				selectedElement.setAttribute("transform", "matrix(1 0 0 1 0 0)");
			}
		}
		
		selectedElement.setAttribute("transform", "matrix(1 0 0 1 0 0)");
		selectedElement.removeAttributeNS(null, "onmousemove");
		//selectedElement.removeAttributeNS(null, "onmouseout");
		selectedElement.removeAttributeNS(null, "onmouseup");

		if(index>=0) {
			var i=0;
			while(selectedElement.getAttribute("x")%130 != coordinates[i][0] || selectedElement.getAttribute("y")%130 != coordinates[i][1]) { i++; }
			EQUATION[Math.floor(selectedElement.getAttribute("x")/130)][i] = 0;
			EQUATION[position][index]=1;
			selectedElement.setAttribute("x", coordinates[index][0] + 130 * position);
			selectedElement.setAttribute("y", coordinates[index][1]);
			selectedElement.setAttribute("class", "match");
			selectedElement.setAttribute("width", coordinates[index][2] ? 100 : 10);
			selectedElement.setAttribute("height", coordinates[index][2] ? 10 : 100);
		}
		selectedElement = 0;
	}
}

function selectElement(evt) {
	selectedElement = evt.target;
	currentX = evt.clientX;
	currentY = evt.clientY;
	currentMatrix = selectedElement.getAttributeNS(null, "transform").slice(7,-1).split(' ');
	for(let i=0;i<currentMatrix.length;i++){
		currentMatrix[i] = parseFloat(currentMatrix[i]);
	}
	selectedElement.setAttributeNS(null, "onmousemove", "moveElement(evt)");
	//selectedElement.setAttributeNS(null, "onmouseout", "deselectElement(evt)");
	selectedElement.setAttributeNS(null, "onmouseup", "deselectElement(evt)");
}

function drawMatches(equation) {
	let svgField = document.getElementById("field");
	while(svgField.firstChild) { svgField.removeChild(svgField.firstChild); }
	for(var i=0;i<equation.length;i++) {
		EQUATION.push(SIGNS[equation[i]].slice());
		for(let j=0;j<10;j++) {
		  if(SIGNS[equation[i]][j]) {
		    var temp = document.createElementNS("http://www.w3.org/2000/svg", 'rect');
		    temp.setAttribute("class", "match")
		    temp.setAttribute("width", coordinates[j][2] ? 100 : 10);
		    temp.setAttribute("height", coordinates[j][2] ? 10 : 100);
		    temp.setAttribute("x", coordinates[j][0]+i*130);
		    temp.setAttribute("y", coordinates[j][1]);
		    temp.setAttribute("onmousedown", "selectElement(evt)");
		    temp.setAttribute("transform", "matrix(1 0 0 1 0 0)");
		    svgField.appendChild(temp);
		  }
		}
	}				
	document.getElementById('equation-button').innerHTML = "Check my solution";
	document.getElementById('equation-button').onclick = check;
}
