
document.getElementById("img").onchange = function() {
    document.querySelector('.upload-images').classList.remove('active');
    document.querySelector('.upload-button').classList.remove('active');
    document.querySelector('.upload-icon').classList.remove('active');
    document.querySelector('.uploader').classList.remove('active');
    document.querySelector('.container').classList.remove('active');
    document.querySelector('.upload-icon').src = uploadsrc +'icon.png';
    document.querySelector(".upload").submit();
};

var uploadImages = document.querySelector('.upload-images');
var uploadIcon = document.querySelector('.upload-icon');
var uploadIconID = document.getElementById('upload-icon');

uploadImages.addEventListener('click', function(){
    document.querySelector('.upload-images').classList.add('active');
    document.querySelector('.upload-button').classList.add('active');
    document.querySelector('.upload-icon').classList.add('active');
    document.querySelector('.uploader').classList.add('active');
    document.querySelector('.container').classList.add('active');
    document.querySelector('.upload-icon').src = uploadsrc +'drag.png';
});


uploadIconID.addEventListener('click', function(){
    if (uploadIconID.src.substr(uploadIconID.src.length-8)==='icon.png'){
        document.querySelector('.upload-icon').src = uploadsrc +'drag.png';
    }else{
        document.getElementById('upload-icon').src = uploadsrc +'icon.png';
    }
    document.querySelector('.upload-images').classList.toggle('active');
    document.querySelector('.upload-button').classList.toggle('active');
    document.querySelector('.upload-icon').classList.toggle('active');
    document.querySelector('.uploader').classList.toggle('active');
    document.querySelector('.container').classList.toggle('active');
});

var uploadsrc = uploadIconID.src.slice(0, uploadIconID.src.length - 8);


var droparea = document.getElementById('uploader');

droparea.ondragover = function(e){
    e.preventDefault();
    droparea.classList.add('hovering');
}

droparea.ondragleave = function(e){
    e.preventDefault();
    droparea.classList.remove('hovering');
}

droparea.ondrop = function(e){
    e.preventDefault();
    e.stopPropagation();
    
    document.getElementById("img").files = e.dataTransfer.files; 
    document.querySelector(".upload").submit();
    console.log(e.dataTransfer.files);
}
