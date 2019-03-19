function changeImage()
{
    var img = document.getElementById("image");
    img.src="images/test2";
    return false;
}

function changeHeading(value)
{
    if(value == 'ship') 
    {
        document.getElementById('heading').innerHTML = "Ship was detected";
    }
    else{
        document.getElementById('heading').innerHTML = "Car was detected";
    }
    
}