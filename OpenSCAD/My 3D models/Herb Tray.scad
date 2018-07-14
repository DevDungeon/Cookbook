/* Santa Cruz Shredder
Large 2 piece grinder 2.75"
69mm diamter x 26mm height
*/ 

grinder_radius = 34.5;
grinder_height = 26;
grinder_padding = 1;

tray_width = 200;
tray_height = 100;
tray_depth = 70;

module grinder_with_padding() {
    rotate([90, 0, 90])
    translate([(tray_depth/2) + (grinder_height/2), tray_height - (grinder_radius-7),160])
    cylinder(r1=grinder_radius+grinder_padding, r2=grinder_radius+grinder_padding, h=grinder_height+grinder_padding);
};

module tray_base() {
    cube([tray_width, tray_height, tray_depth]);
}


module brush_with_padding() {
    //cylinder & sphere hole
}


difference() {
  tray_base();
  grinder_with_padding();
}


//(ashtray/masonjar/
//

/* Volcano cleaning brush
https://www.volcanovaporizer.com/us/en/cleaning-brush-set.html
7mm diameter x 90mm full height
*/
// create an object of the size
// cut it out from the tray block


/* Volcano Easy Valve Filling Chamber
https://www.volcanovaporizer.com/us/en/store/easy-valve-filling-chamber-for-herbs.html
42mm diameter x 63mm height
*/



/* TightVac Herb Container
1 oz to 6 ounce Airtight Multi-Use Vacuum Seal Portable Storage Container for Dry Goods, Food, and Herbs - Black Cap & Body
https://www.amazon.com/gp/product/B0049557HI/ref=oh_aui_search_detailpage?ie=UTF8&psc=1
84mm diameter x 143mm height
*/



// weed holding chamber (drawer?)(and cover)

// weed scoop the exact size of volcano bowl

// space for extra screens, gaskets, clips, bags (drawers?