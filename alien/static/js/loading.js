const loadingScreen = document.querySelector(".loading-screen");
const resultPage = document.querySelector(".result-page");
console.log(loadingScreen);

setTimeout(function () {
  loadingScreen.style.display = "none";
  resultPage.style.display = "block";
}, 3000);
