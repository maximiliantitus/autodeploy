var images = document.querySelectorAll('.image');

 images.forEach(elem =>{
    elem.addEventListener("click", swapImage);
 });

 function swapImage(event){
    var imageClicked = event.target.src;
    var mainImage = document.getElementById('image');
    mainImage.src = imageClicked;
}

