document.addEventListener('DOMContentLoaded', function() {
// set the current banner index to 0
let currentBannerIndex = 0;

// get all the banner elements
const bannerElements = document.querySelectorAll('.bannersection .banner .slider .banner');

// define a function to switch the banner
function switchBanner() {
  // hide all the banner elements
  bannerElements.forEach((banner) => {
    banner.classList.remove('current-banner');
    banner.style.display = 'none';
  });

  // get the current banner element
  const currentBannerElement = bannerElements[currentBannerIndex];

  // show the current banner element
  currentBannerElement.classList.add('current-banner');
  currentBannerElement.style.display = 'block';

  // increment the current banner index
  currentBannerIndex++;

  // reset the current banner index if it exceeds the number of banners
  if (currentBannerIndex >= bannerElements.length) {
    currentBannerIndex = 0;
  }
}
switchBanner();
// switch the banner every 5 seconds
setInterval(switchBanner, 5000);



});




