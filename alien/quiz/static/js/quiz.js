// const vheight = document.getElementsByClassName("quiz-contents");
// const nextBtn = document.getElementById("next-btn");
// const prevBtn = document.getElementById("prev-btn");

let position = $(".quiz-contents").position();

let vheight = $(".quiz-contents").height();

$(".option").click(function () {
  position.top += vheight;

  $("body").animate({ scrollTop: position.top }, 0);
});

// $(".result-btn").click(function () {
//   let divs = $(this).parent().parent().parent().children();
//   console.log(divs);
//   let inputs = divs.find("input:checked");
//   console.log(inputs);
//   if (inputs.length < 1) {
//     alert("문항이 선택되지 않았습니다.");
//     return false;
//   } else if (inputs.length > 1) {
//     alert("중복 선택은 불가합니다.");
//   }
// });

// $(".prev-btn").click(function (e) {
//   e.preventDefault();
//   offset.top -= vheight;
//   console.log(offset.top);
//   $("body").animate({ scrollTop: offset.top }, 0);
// });

// function scrollUp() {
//   const vheight = $(".quiz-contents").height();
//   console.log("h1!!uouo");

//   $("html, body").animate(
//     {
//       scrollTop: (Math.floor($(window).scrollTop()) / vheight - 1) * vheight,
//     },
//     0
//   );
// }

// function scrollDown() {
//   const vheight = $(".quiz-contents").height();
//   console.log(vheight);
//   console.log("h1");

//   $("html, body").animate(
//     {
//       scrollTop: (Math.floor($(window).scrollTop()) / vheight + 1) * vheight,
//     },
//     0
//   );
// }

// nextBtn.addEventListener("click", function (e) {
//   e.preventDefault();
//   scrollDown();
// });

// prevBtn.addEventListener("click", function (e) {
//   e.preventDefault();
//   scrollDown();
// });

// // nextBtn.onclick = function(e){
// //     e.preventDefault();
// //     scrollDown();
// // }

// prevBtn.onclick = function (e) {
//   e.preventDefault();
//   scrollUp();
// };

// $(function () {
//   $("#next-btn").click(function (e) {

//     e.preventDefault();
//     scrollDown();
//   });

//   $("#prev-btn").click(function (e) {
//     e.preventDefault();
//     scrollUp();
//   });

//   $("html, body").animate(
//     {
//       scrollTop: 0,
//     },
//    0
//   );
// });
