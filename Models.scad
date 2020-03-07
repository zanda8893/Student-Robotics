pip=3.5;
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
module CM(pip){
    camera = 10;
    cube_die=[10,10,20];//the cube dimentions
    difference(){
        union(){
          cube(cube_die);
          translate([10/2,10,20+camera-0.5])rotate([90,0,0])linear_extrude(10)circle(r=camera);
        }
        translate([5,5,0])cylinder(r=pip,h=10,$fn=40);
        translate([0,5,15]){
            rotate([0,90,0]){
                cylinder(r=pip,h=10-3,$fn=40);
              }
          }
      }
    translate([10/2,10,20+camera-0.5])rotate([90,0,0])linear_extrude(10)circle(r=camera);
}
CM(pip);
