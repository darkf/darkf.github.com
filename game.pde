int GRIDW = 12;
int GRIDH = 10;
int grid[][] = new int[GRIDH][GRIDW];
int TILEW = 64;
int TILEH = 64;
int gameStatus = 0; // 0 = game, 1 = game over, 2 = win

class Dragon {
    int x = 6;
    int y = 4;
    
    int d(int dx, int dy) {
        int nx = this.x + dx;
        int ny = this.y + dy;
        if(nx < 0 || nx >= GRIDW) return 100;
        if(ny < 0 || ny >= GRIDH) return 100;
        if(grid[ny][nx] == 1) return 100;
        return dist(nx, ny, player.x, player.y);
    }
    
    void updateTurn() {
        int dc = d(0,0);
        //println("dc: " + dc);
        if(d(-1,0) < dc) this.x--;
   else if(d(1,0) < dc) this.x++;
   else if(d(0,-1) < dc) this.y--;
   else if(d(0,1) < dc) this.y++;
    }
}

class Player {
    int x = 4;
    int y = 6;
}

Dragon dragon = new Dragon();
Player player = new Player();

void setup() {  // this is run once.   
    // set the background color
    background(255);
    
    // canvas size (Integers only, please.)
    size(800, 640); 
      
    // smooth edges
    smooth();
    
    textFont(loadFont("Arial"));
    
    // limit the number of frames per second
    frameRate(30);
    
    strokeWeight(0);
    
    //for(int y = 0; y < GRIDH; y++)
    //    for(int x = 0; x < GRIDW; x++)
    //        grid[y][x] = (int)random(0, 2);
    for(int x = 0; x < GRIDW; x++) grid[0][x] = 1;
    for(int x = 0; x < GRIDW; x++) grid[GRIDH-1][x] = 1;
    
    for(int y = 0; y < GRIDH; y++) grid[y][0] = 1;
    for(int y = 0; y < GRIDH; y++) grid[y][GRIDW-1] = 1;
    
    grid[4][5] = 1;
    grid[5][5] = 5; // door
    grid[5][6] = 1;
    grid[6][7] = 1;
    grid[3][4] = 1;
    grid[2][7] = 1;
    grid[1][10] = 4; // keya
}

color colorOf(int tile) {
    if(tile == 0) return #282828; // dark tiles
    if(tile == 1) return #646464; // light tiles (walls)
    if(tile == 2) return #FFFFFF; // player
    if(tile == 3) return #444433; // dragon
    if(tile == 4) return #9F9F00; // key
    if(tile == 5) return #000033; // door
    println("error tile: " + tile);
    return #FF0000;
}

void keyPressed() {
    int x = player.x;
    int y = player.y;
    
    switch(keyCode) {
        case LEFT: x--; break;
        case RIGHT: x++; break;
        case UP: y--; break;
        case DOWN: y++; break;
    }
    
    if(x != player.x || y != player.y) { // moved
        if(grid[y][x] != 1) { // can walk
            player.x = constrain(x, 0, GRIDW-1);
            player.y = constrain(y, 0, GRIDH-1);
            
            if(grid[player.y][player.x] == 4) { // key
                gotKey = true;
                grid[player.y][player.x] = 1;
            }
            else if(grid[player.y][player.x] == 5) { // door
                if(gotKey == true) {
                    gameStatus = 2; // win
                    return;
                }
            }
            
            dragon.updateTurn();
            if(dragon.x == player.x && dragon.y == player.y) {
                gameStatus = 1; // game over
            }
        }
    }
}

void draw() {
    background(255);
    for(int y = 0; y < GRIDH; y++) {
        for(int x = 0; x < GRIDW; x++) {
            int t = grid[y][x];
            if(player.x == x && player.y == y) t = 2;
            if(dragon.x == x && dragon.y == y) t = 3;
            fill(colorOf(t));
            rect(x*TILEW, y*TILEH, TILEW, TILEH);
        }
    }
    
    if(gameStatus == 1 || gameStatus == 2) {
        fill(#7F7F7F, 100);
        rect(0, 0, 800, 640);
        fill(#FFFF00, 255);
        textSize(32);
        text(gameStatus == 2 ? "You win!" : "Game Over", 800/2 - 64, 640/2);
    }
    else {
        fill(255, 255, 0);
        text("x=" + floor(mouseX/TILEW) + ", y=" + floor(mouseY/TILEH), 10, 15);
    }
}
