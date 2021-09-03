float x = 400;
float y = 300;
float z = 0;

boolean upKey = false;
boolean downKey = false;
boolean leftKey = false;
boolean rightKey = false;
boolean wKey = false;

void setup(){
  size(800,600,P3D);
}

void draw(){
  background(0);
  push();
  translate(x,y,z);
  lights();
  fill(255);
  noStroke();
  box(100);
  pop();
  push();
  translate(x,y,z);
  lights();
  fill(255);
  noStroke();
  box(100);
  pop();
  if (upKey && y > 100){
    y -= 10;
  }
  if (downKey && y < height - 100){
    y += 10;
  }
  if (leftKey && x > 100){
    x -= 10;
  }
  if (rightKey && x < width - 100){
    x += 10;
  }
  if (wKey && y > 100){
    y -= 10;
  }
}

void keyPressed(){
  if(keyCode == UP){
    upKey = true;
  }
  if(keyCode == DOWN){
    downKey = true;
  }
  if(keyCode == LEFT){
    leftKey = true;
  }
  if(keyCode == RIGHT){
    rightKey = true;
  }
  if(key == 'W' || key == 'w'){
    wKey = true;
  }
}

void keyReleased(){
  if(keyCode == UP){
    upKey = false;
  }
  if(keyCode == DOWN){
    downKey = false;
  }
  if(keyCode == LEFT){
    leftKey = false;
  }
  if(keyCode == RIGHT){
    rightKey = false;
  }
  if(key == 'W' || key == 'w'){
    wKey = false;
  }
}
