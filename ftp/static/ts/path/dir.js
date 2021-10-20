var all_files = document.querySelectorAll(".one_file");
all_files.forEach(function (one_file) {
    one_file.addEventListener("click", function () {
        window.location.href = location.href + "/" + one_file.getAttribute("path");
    });
});
