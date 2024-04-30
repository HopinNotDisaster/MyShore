
//    console.log("123!!!")
//    console.log($(".link_size"))
$(".link_size a").mouseenter(function() {
// 使用jQuery的css方法将字体颜色修改为绿色
$(this).css("color", "#00ce41");
});
$(".link_size a").mouseleave(function() {
// 使用jQuery的css方法将字体颜色修改为绿色
$(this).css("color", "black");
});

