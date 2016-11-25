onload = function () {
    var td1 = document.getElementsByTagName("tr")[1];
    td1.addEventListener("click", function () {
        location.assign("student_detail.html");
    });
    td1.addEventListener("mouseenter", function () {
        td1.style.backgroundColor = "green";
    });
    td1.addEventListener("mouseout", function () {
        td1.style.backgroundColor = 'transparent';
    });
};
