// add tag
// $("#add-tag").click(function (e) {
//     e.preventDefault();
//     // console.log(this)
//     var $tab = $("#table-tag")
//     var $tr = $("#table-tag tbody > tr");
//     // console.log($tab);
//     console.log($tr);
// })

let tagForm = document.querySelectorAll(".tag-form");
let container = document.querySelector("#new-post");
let addButton = document.querySelector("#add-tag");
let totalForms = document.querySelector("#id_form-TOTAL_FORMS");
// console.log(totalForms);
let formNum = tagForm.length-1;
console.log(formNum);


addButton.addEventListener('click', addForm);

function addForm(e) {
    e.preventDefault();
    let newForm = tagForm[0].cloneNode(true);
    let formRegex = RegExp(`form-(\\d){1}-`,'g')
    // console.log(formRegex);
    formNum++
    newForm.innerHTML = newForm.innerHTML.replace(formRegex, `form-${formNum}-`);
    container.insertBefore(newForm, addButton);
    totalForms.setAttribute('value', `${formNum+1}`);
}

