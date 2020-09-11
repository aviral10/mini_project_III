var s1 = function( f ) {

  f.setup = function() {
    let canvas1 = f.createCanvas(300, 300);
    canvas1.position(600,100);
    f.background(240);
  }
  f.mouseDragged = function (){
    f.fill(0);
    f.circle(f.mouseX, f.mouseY, 30);
  }
};
new p5(s1);

var s2 = function(p) {
class Particle{
    constructor(x,y){
        this.pos = p.createVector(p.random(p.width),p.random(p.height));
        this.target = p.createVector(x,y);
        // this.vel = createVector();
        this.vel = p5.Vector.random2D();
        this.acc = p.createVector();
        this.r = 8;
        this.maxspeed = 10;
        this.maxforce = 1;
        this.col = {
            r: p.random(150,255),
            g: 52,
            b: p.random(150,255),
            a: 100
        }
    }

    behaviour(){
        let arrive = this.arrive(this.target);
        let mouse = p.createVector(p.mouseX, p.mouseY);
        let flee = this.flee(mouse);

        arrive.mult(1);
        flee.mult(5);

        this.applyForce(flee);
        this.applyForce(arrive);
    }
    applyForce(f){
        this.acc.add(f);


    }

    arrive(target){
        let desired = p5.Vector.sub(target, this.pos);
        let d = desired.mag();
        let speed = this.maxspeed;
        if(d < 200){
            speed = p.map(d, 0,100,0, this.maxspeed);
        }
        desired.setMag(speed);
        let steer = p5.Vector.sub(desired, this.vel);
        steer.limit(this.maxforce);
        return steer;
    }


    flee(target){
        let desired = p5.Vector.sub(target, this.pos);
        let d = desired.mag();
        if(d<50){
            desired.setMag(this.maxspeed);
            desired.mult(-1);
            let steer = p5.Vector.sub(desired, this.vel);
            steer.limit(this.maxforce);
            return steer;
        }else{
            return p.createVector(0,0);
        }
    }

    update(){
        this.pos.add(this.vel);
        this.vel.add(this.acc);
        this.acc.mult(0);
    }

    show(){
        // stroke(240,0,0,100);
        p.stroke(this.col.r,this.col.g,this.col.b, 100);
        p.strokeWeight(5);
        p.fill(this.col.r,this.col.g,this.col.b, 100);
        // circle(this.pos.x, this.pos.y, 8);
        p.point(this.pos.x, this.pos.y);
    }


}

let font;
p.preload = function (){
    font = p.loadFont("/static/Handlee-Regular.ttf")
}
let input;
let particles = []
p.setup = function () {
    let canv = p.createCanvas(400,400);
    canv.position(100,50)
    p.background(255);
    input = p.createInput();
    input.position(425,25);
    input.changed(newText);
    let points = font.textToPoints('UwU', p.width/4-100, p.height/2+100,100);
    
    for(let i=0;i<points.length;i++){
        let pt = points[i];
        let particle = new Particle(pt.x, pt.y)
        particles.push(particle);        
    }
}
newText = function (){
    change(input.value());
    // console.log();
}

let arr;
change = function (text){
    arr = []
    let points = font.textToPoints(text, p.width/4-100, p.height/2+100,150);

    for(let i=0;i<points.length;i++){
        let pX;
        if(i<particles.length){
            pX = particles[i];
        }else{
            pX = new Particle(particles[0].pos.x, particles[0].pos.y);
        }
        let ch = points[i];
        pX.target = p.createVector(ch.x, ch.y);
        arr.push(pX) 
    }
    particles = arr;
}



p.draw = function () {
    p.background(240);
    for(let i=0;i<particles.length;i++){
        let par = particles[i];
        par.behaviour();
        par.update();
        par.show();
            
    }
}
};


new p5(s2);
