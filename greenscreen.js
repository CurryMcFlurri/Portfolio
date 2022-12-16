//start w/ foreground image
var fgimg = new SimpleImage("drewRobert.png");
//and background image
var bgimg = new SimpleImage("dinos.png");
//initialize output image
var output = new SimpleImage (fgimg.getWidth(), fgimg.getHeight());
//look at each pixel of foreground image
for (var pixel of fgimg.values()){
//decide if it is green or not
    if (pixel.getGreen() > pixel.getRed() + pixel.getBlue ()){
        var x = pixel.getX();
        var y = pixel.getY();
//if it is, replace it with background image
        var bgpixel = bgimg.getPixel(x, y);
        output.setPixel(x, y, bgpixel);
    }

// if it is not, leave it as is
     else {
        output.setPixel(pixel.getX(), pixel.getY(), pixel);
    }
}
//print new output image
print (output);
