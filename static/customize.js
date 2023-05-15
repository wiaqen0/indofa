document.addEventListener('DOMContentLoaded', function() {
    const canvas = document.getElementById("myCanvas");
const ctx = canvas.getContext("2d");

let img;

const images = [];

function addImage1(src) {
  const image = new Image();
  image.onload = function() {
    images.push({
      x: 0,
      y: 0,
      width: 700,
      height: 700,
      image: image,
      isResizing: false
    });
    drawImages();
  };
  image.src = src;
}
function addImage(src) {
  const image = new Image();
  image.onload = function() {
    const canvasWidth = canvas.width;
    const canvasHeight = canvas.height;
    
    const centerX = (canvasWidth - 220) / 2;
    const centerY = (canvasHeight - 220) / 2;

    images.push({
      x: centerX+20,
      y: centerY+80,
      width: 220,
      height: 220,
      image: image,
      isResizing: false
    });

    drawImages();
  };
  image.src = src;
}

function drawImages() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  for (let i = 0; i < images.length; i++) {
    const image = images[i];
    ctx.drawImage(image.image, image.x, image.y, image.width, image.height);
    if (image.isResizing) {
      canvas.style.cursor = "nwse-resize";
    } else {
      canvas.style.cursor = "default";
    }
  }
}

function updateImage(index, x, y) {
  const image = images[index];
  image.x = x - image.width / 2;
  image.y = y - image.height / 2;
  drawImages();
}

function updateImageSize(index, width, height) {
  const image = images[index];
  image.width = width;
  image.height = height;
  drawImages();
}

let isDragging = false;
let isResizing = false;
let dragIndex = -1;
let resizeIndex = -1;
const resizeMargin = 30; // Adjust this value to increase or decrease the resize region
canvas.addEventListener("mousedown", function(event) {
  const mouseX = event.clientX - canvas.offsetLeft;
  const mouseY = event.clientY - canvas.offsetTop;
  for (let i = images.length - 1; i >= 0; i--) {
    const image = images[i];
    if (
      mouseX >= image.x &&
      mouseX <= image.x + image.width &&
      mouseY >= image.y &&
      mouseY <= image.y + image.height
    ) {
      if (
        mouseX >= image.x + image.width - resizeMargin &&
        mouseY >= image.y + image.height - resizeMargin
      ) {
        isResizing = true;
        resizeIndex = i;
        break;
      } else {
        isDragging = true;
        dragIndex = i;
        const offsetX = mouseX - image.x;
        const offsetY = mouseY - image.y;
        updateImage(dragIndex, mouseX - offsetX, mouseY - offsetY);
        break;
      }
    }
  }
});

canvas.addEventListener("mousemove", function(event) {
  const mouseX = event.clientX - canvas.offsetLeft;
  const mouseY = event.clientY - canvas.offsetTop;
  if (isDragging && dragIndex >= 0) {
    updateImage(dragIndex, mouseX, mouseY);
  } else if (isResizing && resizeIndex >= 0) {
    const image = images[resizeIndex];
    const newWidth = mouseX - image.x;
    const newHeight = mouseY - image.y;
    updateImageSize(resizeIndex, newWidth, newHeight);
  } else {
    for (let i = images.length - 1; i >= 0; i--) {
      const image = images[i];
      if (
        mouseX >= image.x + image.width - resizeMargin &&
        mouseY >= image.y + image.height - resizeMargin
        ) {
          canvas.style.cursor = "nwse-resize";
          break;
        } else {
          canvas.style.cursor = "default";
        }
      }
    }
  });

  canvas.addEventListener("mouseup", function(event) {
    isDragging = false;
    isResizing = false;
    dragIndex = -1;
    resizeIndex = -1;
  });

  function sleep(ms) {
    return new Promise((resolve) => setTimeout(resolve, ms));
  }
  addImage1("{% static 'chaucustom.png'%}");
  const imgFile = document.getElementById("imgFile");
  imgFile.addEventListener("change", function() {
    const file = imgFile.files[0];
    const reader = new FileReader();
    reader.onload = function(event) {
      addImage(event.target.result);
    };
    reader.readAsDataURL(file);
  });
function saveCanvas() {
    // Get the canvas element
    var canvas = document.getElementById("myCanvas");
    // Create a new image from the canvas
    var image = canvas.toDataURL("image/png");
    // Create a link element with the image as its href
    var link = document.createElement("a");
    link.download = "yourcustomization.png";
    link.href = image;
    // Click the link to download the image
    link.click();
}
function saveCanvasImage() {
const csrfToken = getCookie('csrftoken'); // Get the CSRF token from the cookie

const canvasDataUrl = canvas.toDataURL();
const imageBlob = dataURLtoBlob(canvasDataUrl);

const formData = new FormData();
formData.append('image', imageBlob, 'canvas_image.png');

fetch('/order/customize', {
  method: 'POST',
  headers: {
    'X-CSRFToken': csrfToken  // Include the CSRF token in the request headers
  },
  body: formData
})
.then(response => {
  if (response.ok) {
    console.log('Image saved successfully!');
  } else {
    console.error('Failed to save image!');
  }
})
.catch(error => {
  console.error('Error saving image:', error);
});
}

function getCookie(name) {
const cookieValue = document.cookie.match('(^|;)\\s*' + name + '\\s*=\\s*([^;]+)');
return cookieValue ? cookieValue.pop() : '';
}


// Helper function to convert a data URL to a Blob object
function dataURLtoBlob(dataURL) {
const parts = dataURL.split(';base64,');
const contentType = parts[0].split(':')[1];
const byteCharacters = atob(parts[1]);
const byteArrays = [];
for (let offset = 0; offset < byteCharacters.length; offset += 512) {
  const slice = byteCharacters.slice(offset, offset + 512);
  const byteNumbers = new Array(slice.length);
  for (let i = 0; i < slice.length; i++) {
    byteNumbers[i] = slice.charCodeAt(i);
  }
  const byteArray = new Uint8Array(byteNumbers);
  byteArrays.push(byteArray);
}
return new Blob(byteArrays, { type: contentType });
}
})