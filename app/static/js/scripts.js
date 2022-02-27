function openNav() {
    document.getElementById("nav").style.width = "250px";
}
function closeNav() {
    document.getElementById("nav").style.width = "0";
}


var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
    coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.display === "block") {
        content.style.display = "none";
    } else {
        content.style.display = "block";
    }
    });
}
function copyCode() {
    var copyText = document.getElementById('copyCode')
    console.log(copyText)
    copyText.select()
    copyText.setSelectionRange(0, 99999)
    navigator.clipboard.writeText(copyText.value)
    alert("Copied the Code: " + copyText.value)
}