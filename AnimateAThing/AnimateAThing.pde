//AnimateAThing v0.1
//(c) waitblock (Ethan) 2021
//Released under the MIT License

int frameIndex = 0;
int totalFrames = 0;

PImage frame;
PImage playFrame;

int screen = 0;

/*
0 = ANIMATING
1 = PLAYING
*/

void setup(){
  size(800,600);
  background(255);
}

void draw(){
  if(screen == 0){
    frameRate(60);
    textSize(40);
    fill(0);
    text(frameIndex,700,580);
    stroke(0);
    if (mousePressed) {
      line(mouseX, mouseY, pmouseX, pmouseY);
    }
    updateTotalFrames();
  }
  if(screen == 1){
    frameRate(5);
    if (frameIndex+1 < totalFrames){
      displayFrame(frameIndex);
      frameIndex++;
    }
    else{
      frameIndex = 0;
    }
  }
}

void displayFrame(int frameIndex){
  playFrame = loadImage(str(frameIndex)+".jpg");
  image(playFrame,0,0);
}

void updateTotalFrames(){
  if(totalFrames <  frameIndex){
    totalFrames = frameIndex+1;
  }
}

void keyPressed(){
  if(keyCode == RIGHT){
    if(screen == 0){
      frame = get();
      frame.save(str(frameIndex)+".jpg");
      background(255);
      frameIndex++;
    }
  }
  if(keyCode == LEFT && frameIndex > 0){
      if(screen == 0){
        background(255);
        frameIndex--;
        PImage backFrame = loadImage(str(frameIndex)+".jpg");
        image(backFrame,0,0);
      }
  }
  if(key == 'p' || key == 'P'){
    frameIndex = 0;
    screen = 1;
  }
}
