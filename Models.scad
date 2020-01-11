pip=3.35;
module PPM(pip){
    cube_die=[10,10,20];//the cube dimentions
    difference(){
        cube(cube_die);
        translate([5,5,0])cylinder(r=pip,h=10,$fn=40);
        translate([0,5,15]){
            rotate([0,90,0]){
                cylinder(r=pip,h=10-3,$fn=40);
            }
        }
    }
}

module Pclip(pip){
    difference(){
    union(){
        cylinder(r=pip+3,h=10,$fn=40);
        translate([0,-2.5,0])cube([15,5,10]);
    }

    union(){
        cylinder(r=pip,h=10,$fn=40);
        translate([0,-1,0])cube([15,2,10]);
        rotate([90,0,0]){
            translate([11,5,-2.5]){
                cylinder(r=2,h=5,$fn=40);
              }
            }
          }
        }
}
module pole_grip_claw(pip){
    difference(){
        cube([10,10,30]);
        translate([5,5,0])cylinder(r=pip,h=10,$fn=40);
    }
    translate([0,0,20])cube([10,30,10]);
}

module pole_grip(pip){
    difference(){
        cube([10,10,30]);
        translate([5,5,0])cylinder(r=pip,h=10,$fn=40);
    }
}
pole_grip(pip);
