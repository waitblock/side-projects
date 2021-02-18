//p5.js version
let r = 255;
let g = 255;
let b = 255;

let curr = 0;

const tcm = 45;

function setup(){
    createCanvas(800,600);
}

function draw(){
    background(r,g,b);
    if(r < tcm || g < tcm || b < tcm){
        fill(255);
    }
    else{
        fill(0);
    }
    textSize(60);
    textAlign(CENTER);
    text(r+", "+g+", "+b, width/2, height/2);
    displayColor();
}

function displayColor(){
    textSize(20);
    if(r < tcm || g < tcm || b < tcm){
        fill(255);
    }
    else{
        fill(0);
    }
    if(curr == 0){
        text("Currently changing R value", 660, 570);
    }
    if(curr == 1){
        text("Currently changing G value", 660, 570);
    }
    if(curr == 2){
        text("Currently changing B value", 660, 570);
    }
}

function keyPressed(){
    if(key == '1'){
        curr = 0;
    }
    if(key == '2'){
        curr = 1;
    }
    if(key == '3'){
        curr = 2;
    }
    if(keyCode == UP_ARROW){
        if(curr == 0 && r < 255){
            r++;
        }
        if(curr == 1 && g < 255){
            g++;
        }
        if(curr == 2 && b < 255){
            b++;
        }
    }
    if(keyCode == DOWN_ARROW){
        if(curr == 0 && r > 0){
            r--;
        }
        if(curr == 1 && g > 0){
            g--;
        }
        if(curr == 2 && b > 0){
            b--;
        }
    }
}
